# DisclosurePro Weekly SEO & Analytics Feedback Log

This file is updated automatically every Sunday by the **Weekly SEO Feedback Loop** automation using live 28-day metrics from **Google Search Console** and **Google Analytics 4 (`properties/548362622` / `G-V1WBFNJ3ZT`)** via [`scripts/fetch_seo_metrics.py`](../../scripts/fetch_seo_metrics.py).

## One-Time Viewer Access Status
- **Service Account:** `disclosurepro-seo-analytics@project-45afdc2c-be1b-4a48-b04.iam.gserviceaccount.com`
- **Google Analytics 4 (`properties/548362622`):** ✅ Connected & Pulling Live Data
- **Google Search Console (`sc-domain:disclosurepro.ai`):** ✅ Connected & Pulling Live Data (40 ranking pages with impressions, query tables backfilled)

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
