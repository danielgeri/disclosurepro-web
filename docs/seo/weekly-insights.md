# DisclosurePro Weekly SEO & Analytics Feedback Log

This file is updated automatically every Sunday by the **Weekly SEO Feedback Loop** automation using live 28-day metrics from **Google Search Console** and **Google Analytics 4 (`properties/548362622` / `G-V1WBFNJ3ZT`)** via [`scripts/fetch_seo_metrics.py`](../../scripts/fetch_seo_metrics.py).

## One-Time Viewer Access Status
- **Service Account:** `disclosurepro-seo-analytics@project-45afdc2c-be1b-4a48-b04.iam.gserviceaccount.com`
- **Google Analytics 4 (`properties/548362622`):** ✅ Connected & Pulling Live Data
- **Google Search Console (`sc-domain:disclosurepro.ai`):** ✅ Connected & Pulling Live Data (40 top pages tracked, 892 impressions, 6 organic clicks)

---

## Live Snapshot — Nov 22, 2026 (`Last 28d vs. Prior 28d`)

### 1. GA4 28-Day Performance & Conversion Metrics
| Metric | Last 28 Days | Prior 28 Days | Change |
| :--- | :---: | :---: | :---: |
| **Active Users** | **55** | 33 | **+66.7%** |
| **New Users** | **54** | 33 | **+63.6%** |
| **Sessions** | **64** (`50` blog = `78.1%`) | 38 | **+68.4%** |
| **Engaged Sessions** | **23** (`35.9%`) | 17 (`44.7%`) | **+35.3%** |
| **Page Views** | **61** | 51 | **+19.6%** |
| **Event Count** | **222** | 174 | **+27.6%** |
| **Distinct Blog URLs in Top 40** | **38** | — | Steady Breadth |

#### CTA Conversion Funnel Audit (App CTR North Star)
| Event Name | 28-Day Clicks | Rate / Status |
| :--- | :---: | :--- |
| `play_store_click` | **0** | Hardened beacon deployed Nov 18 (4d live) |
| `cta_download_click` | **0** | Tracking Active |
| `early_access_click` | **0** | Tracking Active |
| `blog_cta_click` | **0** | Dual-button `.mid-article-cta` rollout in progress |
| **Total App CTA Clicks** | **0** | **`siteAppCtrPct`: 0.0% / `blogAppCtrPct`: 0.0%** |

**Key GA4 Funnel Leak Findings (15 blog pages with >=3 sessions or >=90s dwell & 0 CTA clicks):**
- **Proof that legacy rewrites fix bounce rate:** After our Nov 9 rewrite of `/blog/el-paso-tx-termites/`, its engagement rate jumped from **14.3%** to **100.0%** (`207.3s` avg dwell)!
- **Top Remaining Funnel Leaks Still Serving Legacy Aug/Sep Templates:**
  1. `/blog/orange-ca-termites` (`5` sessions, `0%` eng, `0` CTA clicks — upgraded Nov 15 with dual-button CTA; monitoring post-Nov 18 window).
  2. `/blog/cambridge-ma-termites/` (`3` sessions, `0%` eng, `3.2s` dwell, `0` CTA clicks — still on legacy template; queued #2 for Monday 9 AM refresh!).
  3. `/blog/ventura-ca-termites/` (`2` sessions, `351.2s` dwell, `0` CTA clicks — queued for refresh).
  4. **Ultra-High-Dwell Legacy Readers (`100%` engaged, `0` CTA clicks):** `/blog/johns-creek-ga-termites/` (`1,461s` / 24.4m), `/blog/rio-rancho-nm-termites/` (`1,325s` / 22.1m), `/blog/columbia-md-termites/` (`966.9s` / 16.1m, 2 pageviews + 24 GSC imp), `/blog/cape-coral-fl-termites/` (`433.2s`), `/blog/overland-park-ks-termites/` (`267.4s`), `/blog/honolulu-hi-termites/` (`241.2s` + 37 GSC imp + 1 click), `/blog/bloomington-in-termites/` (`169.1s` + 23 GSC imp + 1 click), `/blog/termites-new-york-city-ny/` (`115.4s` + pos 6.15 GSC query).

### 2. Google Search Console Overview (Oct 23 – Nov 19, 2026)
- **Top 40 Ranking Pages Totals:** **892 impressions**, **6 organic clicks** (**+100% WoW** vs. 3 clicks on Nov 15), **0.67% CTR**, **10 striking-distance opportunities** (pos 4–20, >=10 imp, <4% CTR).
- **Click-Generating URLs:** `/` (`1` click / `19` imp / `5.26%` CTR / pos `3.16`), `/blog/cambridge-ma-termites/` (`1` / `13` / `7.69%` / pos `13.46`), `/blog/yuma-az-termites/` (`1` / `13` / `7.69%` / pos `6.54`), `/blog/bloomington-in-termites/` (`1` / `23` / `4.35%` / pos `18.74`), `/blog/carlsbad-ca-termites/` (`1` / `30` / `3.33%` / pos `25.10`), `/blog/honolulu-hi-termites/` (`1` / `37` / `2.70%` / pos `15.76`).
- **Critical Diagnostic Audits Uncovered Today:**
  1. **Active Page-1 404 Found:** `https://www.disclosurepro.ai/blog/dallas-tx-termites/` is ranking at **Position 8.0 (7 impressions)** right now while missing from `src/content/blog/`! Promoted to **Priority 0** for Monday 9 AM restoration.
  2. **Legacy Currency Corruption Found (`,000` / `,700` / `,200`):** Aug 20 legacy posts (`tulsa-ok-termites`, `tampa-fl-termites`, `honolulu-hi-termites`) suffered stripped `$XX` dollar figures plus first-person attorney impersonation—killing reader trust and CTR. Fixed Tulsa today; queued Honolulu & Tampa for Mon/Wed refresh.
  3. **Major Keyword Cannibalization Alerts:**
     - `"termite inspection"`: **15 city pages competing** (pos 5.0–17.0, 47+ imp) + 115+ local WDO/inspection queries (`round rock` 38 imp, `roanoke` 22 imp, `salem` 22 imp, `deltona` 14 imp, `lake forest` 13 imp).
     - `"termites in utah"`: **46 impressions split across 3 pages** (`salt-lake-city` 22, `sandy` 22, `sandy-hills` 2) with zero Utah state hub.
     - `"termites in old new england homes"`: **17 impressions split across 4 pages** (`cambridge-ma` pos 4.67, `cranston-ri`, `springfield-ma`, `norwalk-ct`).
- **Surging State Clusters by Impressions:** Texas (`190+` imp: Beaumont 111, Round Rock 38, McAllen 15, Dallas 7, Amarillo 7, Corpus Christi 7, Bryan 6), Illinois (`97+` imp: Chicago Roofs), California (`100+` imp: Carlsbad 30, CA TDS/SPQ 21 @ pos 10.33, Buena Park 17, Oceanside 16 @ pos 4.38, Riverside 38+ query imp, Orange 23+ query imp), North Carolina (`71+` imp: Asheville 57, Cary 14, Fayetteville 9), New York (`62+` imp: Buffalo 31 @ pos 9.77, NYC 13 @ pos 6.15, Brooklyn Roofs 9, Rochester 9), Florida (`60+` imp: Deltona 38, Boca Raton 12, Miami Beach 12, Tampa 10), Indiana (`49` imp: Carmel 26, Bloomington 23 + 1 click), Virginia (`47` imp: Roanoke), Utah (`46` imp), Ohio (`39` imp: Cincinnati 20, Dayton 19), New Jersey (`19` imp striking distance in Edison).

### 3. Immediate Closed-Loop Optimizations Applied Today (Top 3 Unoptimized Striking-Distance / Funnel-Leak Pages)
1. **`/blog/oceanside-ca-termites/` (#1 Unoptimized Striking Distance: `"how to identify termite damage in your home (city: oceanside, state: california)"`, 16 imp @ pos 4.38, 0% CTR):**
   - Retitled from generic *"The Ultimate Guide..."* to *"How to Identify Termite Damage in Oceanside, CA Homes: Section 1 WDO & Disclosure Guide"*.
   - Added dedicated H2 + FAQ matching the exact pos 4.38 query, North County neighborhood risk table, `$125–$42,500+` itemized cost table, editorial `/download` bridge, dual-button `.mid-article-cta`, and upward links to `/blog/california-tds-spq-disclosure-guide/`, `/blog/section-1-vs-section-2-termite-report-california/`, and `/blog/how-to-write-repair-credit-addendum-after-inspection/`.
2. **`/blog/termites-new-york-city-ny/` (Pos 6.15 Striking Distance: `"how do i know if my house has termite damage? (city: new city, state: new york)"`, 13 imp, 0% CTR + 115.4s Engaged GA4 Funnel Leak):**
   - Replaced outdated 89-line Aug 3 post citing the obsolete *"48-question PCDS"* with an accurate **March 2024 N.Y. Real Property Law §§ 460–467 (56-question PCDS / $500 opt-out repealed)** guide covering NYC 5 boroughs + Rockland County/New City.
   - Retitled to *"How to Tell If Your NYC or NY House Has Termite Damage: Mandatory PCDS & WDI Guide"*, added `$150–$55,000+` cost table, dual-button `.mid-article-cta`, editorial `/download` bridge, exact-query FAQs, and internal links to `/blog/buffalo-ny-termites/`, `/blog/buying-house-with-termite-history-disclosure-guide/`, and `/blog/how-to-write-repair-credit-addendum-after-inspection/`.
3. **`/blog/tulsa-ok-termites/` (Striking Distance: `"oklahoma termites"`, 16 imp @ pos 11.62, 0% CTR + Corrupted `,000`/`,700` Currency & Attorney Impersonation):**
   - Retitled to *"Oklahoma Termites & Tulsa Disclosure Guide: OREC Rules, ODAFF-1 Reports & Repair Credits"*, eliminated all broken `,000`/`,700` dollar figures and first-person attorney impersonation.
   - Added Oklahoma 60 O.S. §§ 831–839 Disclosure vs. Disclaimer breakdown, OREC 10-day TRR framing, `$100–$38,000+` Tulsa cost table, dual-button `.mid-article-cta`, editorial `/download` bridge, exact-query FAQs, and 3 internal links.

### 4. Mon/Wed/Fri Pipeline Reprogramming for This Week
1. **Editorial Queue Re-prioritization (`docs/seo/editorial-queue.csv`):**
   - **Placed 3 Priority 0 topics at the VERY TOP of the CSV** so Monday/Wednesday execute them immediately:
     - `dallas-tx-termites` (**URGENT Page-1 404 recovery** — ranking #8.0 in GSC right now).
     - `termite-inspection-wdo-wdi-report-buyer-guide` (**Consolidates 15-page `"termite inspection"` cannibalization** + 115+ local WDO/inspection queries).
     - `utah-termites-real-estate-disclosure-guide` (**Consolidates 46 surging GSC impressions** for `"termites in utah"`).
   - **Re-ordered uncompleted rows (Priorities 14–26)** to directly follow surging GSC/GA4 state clusters: Massachusetts (14), New York (15), New Jersey (16), Indiana (17), Virginia (18), Ohio (19), Maryland (20), Tennessee (21), Georgia (22), Arizona (23), Seller Nondisclosure Remedies (24), Roof Age Unknown/Certification (25), and Miami Termites (26) — and stripped legacy `"The Ultimate Guide..."` titles across all remaining metro entries.
2. **Dynamic Sprint Reprogramming (`docs/seo/active-sprint.json`):**
   - **Doubled `refreshesPerRun` from `1` to `2`** (keeping `newArticlesPerRun: 2`) so Mon/Wed/Fri execute **6 legacy page refreshes + 6 new guides** this week to convert high-impression/high-dwell pages to our dual-button App CTR UX faster.
   - **Rebuilt 10-slug `refreshQueue`** prioritizing broken-dollar & top funnel-leak/striking-distance pages: `honolulu-hi-termites`, `cambridge-ma-termites`, `tampa-fl-termites`, `edison-nj-termites`, `miami-beach-fl-termites`, `columbia-md-termites`, `ventura-ca-termites`, `yuma-az-termites`, `lancaster-ca-termites`, `dayton-oh-termites`.
   - **Updated `priorityInternalLinkTargets`** with exact live URLs currently ranking #4–15 in GSC.
   - **Upgraded `styleAndCtaDirectives`** with the Ban on `"The Ultimate Guide..."` titles, the Refresh Integrity Audit (zero broken `,000` dollars, verified 2024–2026 statutes, dual-button `.mid-article-cta`), and upward hub-linking anti-cannibalization rules.
3. **Prompt & Sidecar Evolution (`docs/seo/prompt-template.md` & `write-blog-posts/sidecar.json`):**
   - Codified the High-CTR Title Formula, Refresh Integrity Audit, and Anti-Cannibalization Hub Routing into both `prompt-template.md` and `sidecar.json` while preserving exact schedule and `agent_permissions`.

---

## Conversion Funnel Upgrade — Nov 18, 2026 (`App CTR North Star`)

- **North Star Mandate:** Every weekly feedback loop and MWF run must optimize for **App Click-Through Rate (`siteAppCtrPct` & `blogAppCtrPct`)**—driving clicks to Google Play (`play_store_click`) and iOS/Web access (`blog_cta_click`, `cta_download_click`, `early_access_click`)—not vanity impressions alone.
- **Sitewide Blog-to-App UX Deployed (`src/layouts/BlogPost.astro`, `src/components/CallToAction.astro`, `src/components/BaseHead.astro`):**
  1. **Above-the-fold Quick Scan Strip** right below every article `<h1>` offering 1-click Google Play + iOS/Web access for skimmers.
  2. **Scroll-aware Sticky Bottom App Bar** (`IntersectionObserver`, auto-hides when bottom CTA enters viewport) capturing 3–20 min engaged readers.
  3. **Dual-button `.mid-article-cta` component** + automatic CSS button styling on all 800+ legacy mid-article `/download` links + `transport_type: 'beacon'` on outbound app store clicks.
- **Closed-Loop Analytics & Pipeline Updates (`scripts/fetch_seo_metrics.py`, `docs/seo/prompt-template.md`, `docs/seo/active-sprint.json`):**
  - Added `appConversionSummary` and `topConvertingPages` to `fetch_seo_metrics.py` and expanded `funnelLeaks` to flag any `/blog/` page with `>=3 sessions` or `>=90s avg dwell` and `0` app clicks.
  - Enforced active-escrow framing, in-copy `/download` editorial bridges, and dual-button mid-article CTAs on all upcoming MWF articles and refreshes (`buffalo-ny-termites`, `cambridge-ma-termites`, `ventura-ca-termites`).

---

## Live Snapshot — Nov 15, 2026 (`Last 28d vs. Prior 28d`)

### 1. GA4 28-Day Performance & Conversion Metrics
| Metric | Last 28 Days | Prior 28 Days | Change |
| :--- | :---: | :---: | :---: |
| **Active Users** | **64** | 14 | **+357.1%** |
| **New Users** | **62** | 14 | **+342.9%** |
| **Sessions** | **71** | 15 | **+373.3%** |
| **Engaged Sessions** | **26** (`36.6%`) | 10 (`66.7%`) | **+160.0%** |
| **Page Views** | **81** | 17 | **+376.5%** |
| **Event Count** | **278** | 66 | **+321.2%** |
| **Blog URLs Receiving Traffic** | **40** | 12 | **+233.3%** |

#### CTA Conversion Funnel Audit
| Event Name | 28-Day Clicks | Status |
| :--- | :---: | :--- |
| `play_store_click` | **0** | Tracking Active |
| `cta_download_click` | **0** | Tracking Active |
| `early_access_click` | **0** | Tracking Active |
| `blog_cta_click` | **0** | Tracking Active |
| **Total CTA Conversions** | **0** (`0.0%`) | ⚠️ Urgent Funnel Leaks Identified |

**Identified Funnel Leaks (>=5 sessions & 0 CTA clicks):**
1. `/blog/el-paso-tx-termites/` (7 sessions, 7 active users, 14.3% engagement rate, 0 CTA clicks)
2. `/blog/orange-ca-termites` (5 sessions, 5 active users, 0.0% engagement rate, 0 CTA clicks)

### 2. Google Search Console Overview (Oct 16 – Nov 12, 2026)
- **Pages Receiving Impressions:** **40 pages**
- **Recorded Organic Clicks:** **3 clicks** (`/blog/honolulu-hi-termites/` CTR 14.3%, `/blog/cambridge-ma-termites/` CTR 11.1%, `/blog/carlsbad-ca-termites/` CTR 7.1%)
- **Top Geographic & Defect Clusters by Impressions:**
  - **Texas Termites & Defect Law:** Beaumont (49 imp), Round Rock (18 imp across inspections & termite damage lawyer queries), McAllen (10 imp), Bryan (6 imp), El Paso (4 imp).
  - **Illinois / Chicago Roofing:** Chicago Roofs (27 imp; 22+ imp across "anatomy of a roof in illinois", "common roofing mistakes in illinois", and "chicago roofing problems").
  - **North Carolina Termites:** Asheville (26 imp, pos 34.8), Cary (7 imp), Fayetteville (7 imp).
  - **California Coastal & Desert:** Orange (16 imp across high-intent queries), El Cajon (15 imp), Carlsbad (14 imp, 1 click), Irvine (12 imp), Riverside (17 imp).
  - **Massachusetts Caveat Emptor:** Boston Roofs (14 imp, pos 5.64, "how do i know if my roof is leaking?"), Cambridge Termites (9 imp, 1 click, 3 GA4 sessions).
  - **Florida WDO & Johnson v. Davis:** Tampa ("tampa termite damage lawyer" 7 imp, pos 9.71), Deltona (9 imp), Fort Lauderdale (5 imp), Gainesville (5 imp).
  - **Pennsylvania PAR Disclosures:** Allentown (14 imp, "termites in pennsylvania" 12 imp).

### 3. Immediate Closed-Loop Optimizations Applied Today
1. **`/blog/murfreesboro-tn-termites/` (Striking Distance: "termite letter murfreesboro" 13 imp @ pos 18.8, "termites murfreesboro" 7 imp @ pos 12.4):**
   - Retitled to *"Termite Letter Murfreesboro, TN: Rutherford County WDI Rules, Costs & Credits"*.
   - Replaced first-person attorney impersonation with objective research team voice, leading with $15,000–$50,000 financial stakes and TCA § 66-5-201 rules.
   - Added specific FAQ addressing *"What is a termite letter in Murfreesboro, TN and who pays for it?"* and local pricing benchmarks ($75–$150).
   - Added contextual internal links to `/blog/how-to-write-repair-credit-addendum-after-inspection/`, `/blog/5-disclosure-red-flags/`, and `/blog/ai-home-inspection-report-analyzer-guide/`.
2. **`/blog/mcallen-tx-termites/` (Striking Distance: "termites in mcallen" 10 imp @ pos 11.6):**
   - Retitled to *"Termites in McAllen, TX: Formosan Risks, Texas Disclosures & Repair Credit Guide"*.
   - Upgraded opening hook with $18,000–$56,500 Formosan structural stakes, Texas Property Code § 5.008, and TDA SPCS WDI reports.
   - Added targeted FAQ coverage answering *"Are termites common in McAllen, TX?"* and local repair cost benchmarks.
   - Added internal links to `/blog/texas-trec-sellers-disclosure-guide/` and `/blog/how-to-write-repair-credit-addendum-after-inspection/`.
3. **`/blog/orange-ca-termites/` (Funnel Leak: 5 sessions, 0 CTA clicks; High-Intent Queries: pos 2.86 & pos 6.8):**
   - Retitled to *"Orange, CA Termite Inspections & Disclosures: Section 1 WDO Guide & Repair Credits"*.
   - Added direct FAQ sections answering exact ranking search queries: *"Can termites damage my house structure in one year in Orange, CA?"* (pos 2.86) and *"Why do I have termites in my house in Orange, CA?"* (pos 6.8).
   - Upgraded mid-article callout headline specifically targeting Orange County TDS/SPQ and Section 1 pest reports.

### 4. Mon/Wed/Fri Pipeline Reprogramming for This Week
1. **Editorial Queue Re-prioritization (`docs/seo/editorial-queue.csv`):**
   - **Inserted 2 high-impression query gap guides at Priority 0:**
     - `illinois-roof-inspection-disclosure-guide` (capturing 22+ impressions across Illinois/Chicago roof anatomy & defect queries).
     - `buying-house-with-termite-history-disclosure-guide` (capturing surging "termite damage lawyer" / undisclosed termite damage searches across TX, FL, AL).
   - **Promoted surging state disclosure guides** for high-impression states: Florida (`florida-johnson-v-davis-sellers-disclosure-guide`), Illinois (`illinois-residential-real-property-disclosure-guide`), North Carolina (`north-carolina-rpoads-mineral-oil-gas-disclosure-guide`), Pennsylvania (`pennsylvania-sellers-property-disclosure-statement-guide`), and Massachusetts (`massachusetts-caveat-emptor-title-5-lead-disclosure-guide`).
2. **Dynamic Sprint Tuning (`docs/seo/active-sprint.json`):**
   - Set `newArticlesPerRun: 2` and `refreshesPerRun: 1` so MWF runs balance high-velocity content production with existing page refresh optimization.
   - Queued 3 striking-distance slugs in `refreshQueue`: `boston-ma-roofs` (pos 5.64, 14 imp), `albuquerque-nm-termites` (pos 4.82, 11 imp), and `buffalo-ny-termites` (pos 8.44, 9 imp).
   - Populated `priorityInternalLinkTargets` with exact URLs ranking #4–15 in GSC.
   - Updated `styleAndCtaDirectives` with winning title, hook, cost table, and tailored CTA patterns.
3. **Prompt Evolution (`docs/seo/prompt-template.md`):**
   - Codified exact query matching in FAQ sections, dollar-stakes opening hooks, and tailored mid-article callout headings.

---

## Live Snapshot — Nov 09, 2026 (`Last 28d vs. Prior 28d`)

### 1. GA4 Site-Wide Growth
| Metric | Last 28 Days | Prior 28 Days | Change |
| :--- | :---: | :---: | :---: |
| **Active Users** | **64** | 3 | **+2,033%** |
| **New Users** | **63** | 3 | **+2,000%** |
| **Sessions** | **71** | 3 | **+2,267%** |
| **Engaged Sessions** | **29** (`40.8%`) | 2 (`66.7%`) | **+1,350%** |
| **Page Views** | **83** | 3 | **+2,667%** |
| **Blog URLs Receiving Organic Visits** | **38** | 0 | **New** |

### 2. Key Findings & Immediate Closed-Loop Optimizations Applied
1. **Top Organic Landing Page (`/blog/el-paso-tx-termites/` — 8 sessions, `12.5%` engagement rate):**
   - Previously served one of the Aug 3 generic Mad-Libs clones, explaining its `87.5%` immediate bounce rate.
   - **Action taken:** Replaced with a hyper-localized Chihuahuan Desert / Fort Bliss VA WDI / Texas TREC OP-H guide with custom hero imagery and internal links to the Texas Seller's Disclosure & Repair Credit playbooks. Also restored localized guides for `/blog/las-vegas-nv-termites/` (533s engaged session) and `/blog/memphis-tn-termites/` (137s engaged session) so zero live ranking URLs 404.
2. **Second Funnel Leak (`/blog/orange-ca-termites/` — 5 sessions, `0%` engagement rate):**
   - **Action taken:** Upgraded `<title>`, `<meta description>`, and opening hook (`Orange, CA` + Old Towne + Section 1 WDO internal link), removing slow generic intro filler.
3. **Strong Dwell Time on Localized Guides:**
   - Readers on non-cloned guides are showing **2 to 9+ minutes of engaged dwell time** (`/blog/cary-nc-termites/` `594s`, `/blog/cape-coral-fl-termites/` `433s`, `/blog/norfolk-va-termites/` `317s`, `/blog/overland-park-ks-termites/` `267s`, `/blog/irvine-ca-termites/` `253s`). Newly deployed GA4 CTA events (`play_store_click`, `cta_download_click`, `early_access_click`, `blog_cta_click`) will track conversions on these pages going forward.
