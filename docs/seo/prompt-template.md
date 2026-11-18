# DisclosurePro High-Intent SEO & App Conversion Editorial Guidelines

> **North Star Goal:** Every article exists not just to rank on Google, but to **drive qualified click-throughs to the DisclosurePro AI app** (`play_store_click`, `blog_cta_click`, `cta_download_click`, `early_access_click`) from homebuyers, buyer's agents, and investors actively reviewing real estate disclosure & inspection PDFs.

Use these instructions when generating or refreshing articles from [`docs/seo/editorial-queue.csv`](./editorial-queue.csv) and [`docs/seo/active-sprint.json`](./active-sprint.json).

On each scheduled run:
1. **Refresh Existing Pages (`refreshesPerRun` / `refreshQueue`):** If `refreshesPerRun > 0` and `refreshQueue` in `active-sprint.json` is non-empty, take up to `refreshesPerRun` slugs from `refreshQueue`, upgrade those existing `.md` files in `src/content/blog/` (sharpening `title`, `description`, `updatedDate`, opening hook, cost table, editorial product bridge, dual-button `.mid-article-cta`, FAQs, and internal links), and remove the completed slugs from `refreshQueue` in `active-sprint.json`.
2. **Write New Guides (`newArticlesPerRun`):** Select the next `newArticlesPerRun` rows in `editorial-queue.csv` where `Completed` is empty (sorted by ascending numeric `Priority`, so `Priority 0` data-driven topics added by Sunday's feedback loop always run first!), write each article at `src/content/blog/<Slug>.md`, and mark `Completed` as `x` in `editorial-queue.csv`.
3. If no uncompleted rows and no `refreshQueue` items remain, **STOP and do nothing**—never clear the queue or regenerate duplicates.
4. Verify the build with `npm --prefix /Users/danielgeri/Documents/disclosure-app/web run build`, commit, and push to `main`.

---

## Authoring, SEO & App-CTR Conversion Rules

1. **Authoritative Research Team Voice (No Impersonation):**
   - Write from the perspective of the **DisclosurePro Real Estate Research Team**—an objective, deeply researched real estate due-diligence authority.
   - **NEVER** claim first-person licensure (e.g., do NOT write *"As an experienced real estate attorney and managing broker in..."*).

2. **Format & Single `<h1>` Rule:**
   - Return pure Markdown starting with Astro YAML frontmatter:
     ```yaml
     ---
     title: "<Exact or refined high-intent title incorporating target query>"
     description: "<Unique, compelling 140–160 character meta description naturally incorporating the Target Keyword>"
     pubDate: "<Current Date, e.g., Nov 20 2026>"
     heroImage: "../../assets/red_flags_hero.jpg"
     ---
     ```
   - For refreshed articles, always update `updatedDate: "<Current Date, e.g., Nov 20 2026>"`.
   - **Do NOT start the Markdown body with `# Title`**—`BlogPost.astro` already renders `title` as the page's single `<h1>`. Use sequential `##` (H2) and `###` (H3) headings only.
   - Never leave template placeholders like `{city}`, `{state}`, or `[CITY]`.

3. **Immediate Financial Stakes & Active-Escrow Framing (Zero Travel-Guide Fluff):**
   - Open the first paragraph immediately with concrete dollar stakes (`$X,XXX–$XX,XXX`), the ticking inspection/contingency clock, and the exact state statutory form or inspection standard.
   - Even on defect-focused topics (roofs, termites, sewer scopes, foundation cracks), frame the stakes around **reviewing disclosure & inspection PDFs before waiving contingencies** so readers connect their problem directly to using the DisclosurePro AI app.
   - Never begin with travel-brochure introductions about local scenery, culture, or dining.

4. **Genuine Technical, Legal & Financial Depth (1,300–1,800 Words):**
   - Cover every statutory form name, code section, inspection standard, and negotiation nuance listed in the row's `Focus & Statutory / Technical Details` column.
   - Include an **itemized contractor cost breakdown table (`$5,000–$50,000+`)** detailing inspection, remediation, and structural repair ranges—articles with cost tables achieved 4 to 9+ minutes of engaged reading time in GA4.
   - Explain *why* sellers or inspectors phrase defects vaguely inside 100+ page disclosure packets and how contradictions hide across separate PDFs.

5. **In-Copy Editorial Product Bridge (Beat Banner Blindness):**
   - Readers often skim past standalone banners unless the prose itself demonstrates *how* the app solves their exact pain point.
   - Inside the **Cost Breakdown / Repair Credit Negotiation** or **Manual Review** section, weave **one natural contextual Markdown link to `/download`** explaining the workflow win—for example:
     > *"Instead of manually cross-referencing 120+ pages of seller disclosures against buried inspector disclaimers before your contingency deadline, upload your packet to the [DisclosurePro AI app](/download) to flag contradictions, jump to exact PDF page citations, and calculate local repair credits in seconds."*

6. **High-CTR Dual-Button Mid-Article Callout (No Duplicate Bottom CTA):**
   - Halfway through the article (right after uncovering the primary disclosure traps or cost stakes), include one `.mid-article-cta` card tailored to the **exact state form or defect** in the article, offering **1-click Google Play access** AND **iPhone/Web upload access**:
     ```html
     <aside class="mid-article-cta" aria-label="Scan your disclosure packet with DisclosurePro AI">
       <h3>Reviewing a [Exact State Form / Defect Inspection] PDF Right Now?</h3>
       <p>Upload your 100+ page seller disclosures, inspection reports, and WDO/HOA packets to <strong>DisclosurePro AI</strong>—spot buried red flags, verify exact PDF page numbers, and generate your repair credit request in 10 seconds (1st property free).</p>
       <div class="mid-article-cta-buttons">
         <a href="https://play.google.com/store/apps/details?id=ai.disclosurepro.app" target="_blank" rel="noopener noreferrer" class="mid-cta-btn-play" data-gtag-event="play_store_click" data-gtag-label="blog_mid_cta_google_play">Get Free App on Google Play 🚀</a>
         <a href="/download" class="mid-cta-btn-web" data-gtag-event="blog_cta_click" data-gtag-label="blog_mid_cta_ios_web">iPhone &amp; Web Upload &rarr;</a>
       </div>
     </aside>
     ```
   - **Do NOT add a bottom CTA section** at the end of the Markdown file—`BlogPost.astro` automatically renders the above-the-fold quick strip, scroll-aware sticky bar, and bottom `<CallToAction />`.

7. **Conversational Query-Matching FAQ Section:**
   - Include a **3–4 question FAQ section** (`## Frequently Asked Questions About...`) answering exact conversational queries discovered in Search Console (e.g., *"Can termites damage my house structure in one year?"*, *"What is a termite letter and who pays for it?"*, *"What happens if a seller lies on the property disclosure statement?"*).

8. **Internal Linking (Mandatory — 2 to 3 Guide Links Per Article):**
   - Naturally weave **2 to 3 contextual Markdown links** inside the body pointing to relevant existing guides on the site (in addition to the `/download` app link), prioritizing `priorityInternalLinkTargets` from `active-sprint.json`.
