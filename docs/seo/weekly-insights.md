# DisclosurePro Weekly SEO & Analytics Feedback Log

This file is updated automatically every Sunday by the **Weekly SEO Feedback Loop** automation using live 28-day metrics from **Google Search Console** and **Google Analytics 4 (`properties/548362622` / `G-V1WBFNJ3ZT`)** via [`scripts/fetch_seo_metrics.py`](../../scripts/fetch_seo_metrics.py).

## One-Time Viewer Access Status
- **Service Account:** `disclosurepro-seo-analytics@project-45afdc2c-be1b-4a48-b04.iam.gserviceaccount.com`
- **Google Analytics 4 (`properties/548362622`):** ✅ Connected & Pulling Live Data
- **Google Search Console:** ⏳ Pending Viewer Access (Settings → Users and permissions → Add user → `disclosurepro-seo-analytics@project-45afdc2c-be1b-4a48-b04.iam.gserviceaccount.com`)

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
