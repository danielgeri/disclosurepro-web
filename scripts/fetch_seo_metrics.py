#!/usr/bin/env python3
"""
DisclosurePro Closed-Loop SEO & Conversion Metrics Fetcher
----------------------------------------------------------
Authenticates via Zero-JSON-Key GCP Service Account impersonation
(`disclosurepro-seo-analytics@project-45afdc2c-be1b-4a48-b04.iam.gserviceaccount.com`)
and pulls 28-day performance data from:
  1. Google Analytics 4 (GA4 Admin + Data API v1)
  2. Google Search Console (Search Analytics API v1)

Outputs structured JSON to `/tmp/seo_metrics_latest.json` and prints an
actionable diagnostic digest for the weekly SEO optimization agent.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from typing import Any

DEFAULT_SA = "disclosurepro-seo-analytics@project-45afdc2c-be1b-4a48-b04.iam.gserviceaccount.com"
GA4_MEASUREMENT_ID = "G-V1WBFNJ3ZT"
SITE_DOMAIN = "disclosurepro.ai"
SITE_URL_PREFIX = "https://www.disclosurepro.ai/"
OUTPUT_JSON_PATH = "/tmp/seo_metrics_latest.json"

SCOPES = ",".join([
    "https://www.googleapis.com/auth/analytics.readonly",
    "https://www.googleapis.com/auth/webmasters.readonly",
])

CONVERSION_EVENTS = {
    "play_store_click",
    "cta_download_click",
    "early_access_click",
    "early_access_or_contact_click",
    "blog_cta_click",
    "demo_explore_click",
}


def get_access_token(sa_email: str) -> str:
    cmd = [
        "gcloud",
        "auth",
        "print-access-token",
        f"--impersonate-service-account={sa_email}",
        f"--scopes={SCOPES}",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        raise RuntimeError(
            f"Failed to obtain impersonated token for {sa_email}:\n{proc.stderr.strip()}"
        )
    return proc.stdout.strip()


def api_request(
    url: str,
    token: str,
    method: str = "GET",
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    data = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as err:
        body = err.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {err.code} calling {url}: {body}") from err


def discover_ga4_property(token: str) -> tuple[str | None, str | None]:
    override = os.environ.get("GA4_PROPERTY_ID", "").strip()
    if override:
        prop = override if override.startswith("properties/") else f"properties/{override}"
        return prop, "env_override"

    summaries = api_request(
        "https://analyticsadmin.googleapis.com/v1beta/accountSummaries?pageSize=200",
        token,
    )
    candidates: list[tuple[str, str]] = []
    for acct in summaries.get("accountSummaries", []):
        for prop_sum in acct.get("propertySummaries", []):
            prop_name = prop_sum.get("property", "")
            disp = prop_sum.get("displayName", "")
            candidates.append((prop_name, disp))
            # Check data streams to match exact G-V1WBFNJ3ZT measurement ID
            try:
                streams = api_request(
                    f"https://analyticsadmin.googleapis.com/v1beta/{prop_name}/dataStreams",
                    token,
                )
                for st in streams.get("dataStreams", []):
                    web_data = st.get("webStreamData", {})
                    if web_data.get("measurementId") == GA4_MEASUREMENT_ID:
                        return prop_name, disp
            except Exception:
                continue

    for prop_name, disp in candidates:
        if "disclosure" in disp.lower():
            return prop_name, disp
    return (candidates[0] if candidates else (None, None))


def fetch_ga4_metrics(token: str, prop_name: str) -> dict[str, Any]:
    url = f"https://analyticsdata.googleapis.com/v1beta/{prop_name}:runReport"

    # 1. Site-wide 28d summary vs prior 28d
    overview_resp = api_request(
        url,
        token,
        method="POST",
        payload={
            "dateRanges": [
                {"startDate": "28daysAgo", "endDate": "yesterday", "name": "last_28d"},
                {"startDate": "56daysAgo", "endDate": "29daysAgo", "name": "prev_28d"},
            ],
            "metrics": [
                {"name": "activeUsers"},
                {"name": "newUsers"},
                {"name": "sessions"},
                {"name": "engagedSessions"},
                {"name": "engagementRate"},
                {"name": "screenPageViews"},
                {"name": "eventCount"},
            ],
        },
    )

    # 2. Top landing pages (last 28d)
    landing_resp = api_request(
        url,
        token,
        method="POST",
        payload={
            "dateRanges": [{"startDate": "28daysAgo", "endDate": "yesterday"}],
            "dimensions": [{"name": "pagePath"}],
            "metrics": [
                {"name": "sessions"},
                {"name": "activeUsers"},
                {"name": "screenPageViews"},
                {"name": "engagementRate"},
                {"name": "averageSessionDuration"},
            ],
            "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}],
            "limit": 100,
        },
    )

    # 3. Conversion CTA events by pagePath (last 28d)
    events_resp = api_request(
        url,
        token,
        method="POST",
        payload={
            "dateRanges": [{"startDate": "28daysAgo", "endDate": "yesterday"}],
            "dimensions": [{"name": "pagePath"}, {"name": "eventName"}],
            "metrics": [{"name": "eventCount"}],
            "dimensionFilter": {
                "filter": {
                    "fieldName": "eventName",
                    "inListFilter": {"values": sorted(CONVERSION_EVENTS)},
                }
            },
            "limit": 500,
        },
    )

    metric_names = [
        "activeUsers",
        "newUsers",
        "sessions",
        "engagedSessions",
        "engagementRate",
        "screenPageViews",
        "eventCount",
    ]
    overview: dict[str, dict[str, float]] = {}
    for row in overview_resp.get("rows", []):
        dr_name = row.get("dimensionValues", [{}])[0].get("value", "last_28d")
        vals = row.get("metricValues", [])
        overview[dr_name] = {
            metric_names[i]: float(vals[i]["value"])
            for i in range(min(len(metric_names), len(vals)))
        }

    cta_by_page: dict[str, dict[str, int]] = defaultdict(dict)
    cta_totals: dict[str, int] = defaultdict(int)
    for row in events_resp.get("rows", []):
        dims = row.get("dimensionValues", [])
        val = int(float(row.get("metricValues", [{"value": "0"}])[0]["value"]))
        page_path = dims[0]["value"]
        ev_name = dims[1]["value"]
        cta_by_page[page_path][ev_name] = cta_by_page[page_path].get(ev_name, 0) + val
        cta_totals[ev_name] += val

    pages = []
    funnel_leaks = []
    for row in landing_resp.get("rows", []):
        page_path = row["dimensionValues"][0]["value"]
        m = row["metricValues"]
        sessions = int(float(m[0]["value"]))
        users = int(float(m[1]["value"]))
        views = int(float(m[2]["value"]))
        eng_rate = round(float(m[3]["value"]), 4)
        avg_dur = round(float(m[4]["value"]), 1)
        page_ctas = sum(cta_by_page.get(page_path, {}).values())

        entry = {
            "pagePath": page_path,
            "sessions": sessions,
            "activeUsers": users,
            "pageViews": views,
            "engagementRate": eng_rate,
            "avgSessionDurationSec": avg_dur,
            "ctaClicks": page_ctas,
            "ctaBreakdown": dict(cta_by_page.get(page_path, {})),
        }
        pages.append(entry)
        if sessions >= 5 and page_ctas == 0 and page_path.startswith("/blog/"):
            funnel_leaks.append(entry)

    return {
        "property": prop_name,
        "overview": overview,
        "ctaTotals": dict(cta_totals),
        "topPages": pages[:40],
        "funnelLeaks": funnel_leaks[:15],
    }


def discover_gsc_site(token: str) -> str | None:
    sites_resp = api_request("https://www.googleapis.com/webmasters/v3/sites", token)
    entries = [s.get("siteUrl", "") for s in sites_resp.get("siteEntry", [])]
    preferred = [
        f"sc-domain:{SITE_DOMAIN}",
        SITE_URL_PREFIX,
        f"https://{SITE_DOMAIN}/",
    ]
    for p in preferred:
        if p in entries:
            return p
    for e in entries:
        if SITE_DOMAIN in e:
            return e
    return None


def fetch_gsc_metrics(token: str, site_url: str) -> dict[str, Any]:
    end_date = (dt.date.today() - dt.timedelta(days=3)).isoformat()
    start_date = (dt.date.today() - dt.timedelta(days=30)).isoformat()
    encoded_site = urllib.parse.quote(site_url, safe="")
    query_url = f"https://www.googleapis.com/webmasters/v3/sites/{encoded_site}/searchAnalytics/query"

    pair_resp = api_request(
        query_url,
        token,
        method="POST",
        payload={
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ["query", "page"],
            "rowLimit": 500,
        },
    )

    page_resp = api_request(
        query_url,
        token,
        method="POST",
        payload={
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ["page"],
            "rowLimit": 100,
        },
    )

    striking_distance = []
    query_to_pages: dict[str, list[dict[str, Any]]] = defaultdict(list)
    top_queries = []

    for row in pair_resp.get("rows", []):
        query_text, page_url = row["keys"][0], row["keys"][1]
        clicks = int(row.get("clicks", 0))
        impressions = int(row.get("impressions", 0))
        ctr = round(float(row.get("ctr", 0.0)), 4)
        pos = round(float(row.get("position", 0.0)), 2)

        item = {
            "query": query_text,
            "page": page_url,
            "clicks": clicks,
            "impressions": impressions,
            "ctr": ctr,
            "position": pos,
        }
        top_queries.append(item)
        query_to_pages[query_text].append(item)

        if 4.0 <= pos <= 20.0 and impressions >= 10 and ctr < 0.04:
            striking_distance.append(item)

    striking_distance.sort(key=lambda x: (-x["impressions"], x["position"]))
    top_queries.sort(key=lambda x: (-x["impressions"], -x["clicks"]))

    cannibalization = []
    for q, items in query_to_pages.items():
        if len(items) >= 2 and sum(i["impressions"] for i in items) >= 15:
            cannibalization.append({"query": q, "pages": items})

    top_pages = [
        {
            "page": r["keys"][0],
            "clicks": int(r.get("clicks", 0)),
            "impressions": int(r.get("impressions", 0)),
            "ctr": round(float(r.get("ctr", 0.0)), 4),
            "position": round(float(r.get("position", 0.0)), 2),
        }
        for r in page_resp.get("rows", [])
    ]
    top_pages.sort(key=lambda x: (-x["impressions"], -x["clicks"]))

    return {
        "siteUrl": site_url,
        "dateRange": {"startDate": start_date, "endDate": end_date},
        "topPages": top_pages[:40],
        "topQueryPagePairs": top_queries[:50],
        "strikingDistanceOpportunities": striking_distance[:20],
        "cannibalizationAlerts": cannibalization[:15],
    }


def main() -> int:
    sa_email = os.environ.get("SEO_SA_EMAIL", DEFAULT_SA)
    report: dict[str, Any] = {
        "generatedAt": dt.datetime.now(dt.timezone.utc).isoformat(),
        "serviceAccount": sa_email,
        "ga4": None,
        "gsc": None,
        "warnings": [],
    }

    try:
        token = get_access_token(sa_email)
    except Exception as exc:
        report["warnings"].append(str(exc))
        with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(json.dumps(report, indent=2))
        return 1

    # 1. GA4
    try:
        prop_name, prop_disp = discover_ga4_property(token)
        if not prop_name:
            report["warnings"].append(
                f"No GA4 property visible yet. Grant Viewer access to {sa_email} in GA4 -> Admin -> Property Access Management."
            )
        else:
            ga4_data = fetch_ga4_metrics(token, prop_name)
            ga4_data["displayName"] = prop_disp
            report["ga4"] = ga4_data
    except Exception as exc:
        report["warnings"].append(f"GA4 fetch error: {exc}")

    # 2. Google Search Console
    try:
        gsc_site = discover_gsc_site(token)
        if not gsc_site:
            report["warnings"].append(
                f"No Search Console site visible yet. Grant Restricted/Full Viewer access to {sa_email} in Search Console -> Settings -> Users and permissions."
            )
        else:
            report["gsc"] = fetch_gsc_metrics(token, gsc_site)
    except Exception as exc:
        report["warnings"].append(f"Search Console fetch error: {exc}")

    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"Saved full SEO & GA4 report to {OUTPUT_JSON_PATH}")
    if report["warnings"]:
        print("WARNINGS:")
        for w in report["warnings"]:
            print(f"  - {w}")
    if report["ga4"]:
        ov = report["ga4"].get("overview", {})
        print(f"GA4 ({report['ga4']['property']}): {json.dumps(ov)}")
        print(f"GA4 CTA Totals: {json.dumps(report['ga4']['ctaTotals'])}")
        print(f"GA4 Funnel Leaks ({len(report['ga4']['funnelLeaks'])} pages with >=5 sessions & 0 CTA clicks)")
    if report["gsc"]:
        print(
            f"GSC ({report['gsc']['siteUrl']}): "
            f"{len(report['gsc']['topPages'])} pages with impressions, "
            f"{len(report['gsc']['strikingDistanceOpportunities'])} striking-distance opportunities"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
