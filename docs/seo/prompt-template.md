# DisclosurePro High-Intent SEO Editorial Guidelines

Use these instructions when generating or refreshing articles from [`docs/seo/editorial-queue.csv`](./editorial-queue.csv) and [`docs/seo/active-sprint.json`](./active-sprint.json).

On each scheduled run:
1. **Refresh Existing Pages (`refreshesPerRun` / `refreshQueue`):** If `refreshesPerRun > 0` and `refreshQueue` in `active-sprint.json` is non-empty, take up to `refreshesPerRun` slugs from `refreshQueue`, upgrade those existing `.md` files in `src/content/blog/` (sharpening `title`, `description`, `updatedDate`, opening hook, cost table, FAQs, and internal links), and remove the completed slugs from `refreshQueue` in `active-sprint.json`.
2. **Write New Guides (`newArticlesPerRun`):** Select the next `newArticlesPerRun` rows in `editorial-queue.csv` where `Completed` is empty (sorted by ascending numeric `Priority`, so `Priority 0` data-driven topics added by Sunday's feedback loop always run first!), write each article at `src/content/blog/<Slug>.md`, mark `Completed` as `x` in `editorial-queue.csv`.
3. If no uncompleted rows and no `refreshQueue` items remain, **STOP and do nothing**—never clear the queue or regenerate duplicates.
4. Verify the build with `npm --prefix /Users/danielgeri/Documents/disclosure-app/web run build`, commit, and push to `main`.

---

## Authoring & Quality Rules Proven by GA4 & GSC Data

1. **Authoritative Research Team Voice (No Impersonation):**
   - Write from the perspective of the **DisclosurePro Real Estate Research Team**—an objective, deeply researched real estate due-diligence authority.
   - **NEVER** claim first-person licensure (e.g., do NOT write *"As an experienced real estate attorney and managing broker in..."*).

2. **Format & Single `<h1>` Rule:**
   - Return pure Markdown starting with Astro YAML frontmatter:
     ```yaml
     ---
     title: "<Exact or refined high-intent title incorporating target query>"
     description: "<Unique, compelling 140–160 character meta description naturally incorporating the Target Keyword>"
     pubDate: "<Current Date, e.g., Nov 16 2026>"
     heroImage: "../../assets/red_flags_hero.jpg"
     ---
     ```
   - For refreshed articles, always update `updatedDate: "<Current Date, e.g., Nov 16 2026>"`.
   - **Do NOT start the Markdown body with `# Title`**—`BlogPost.astro` already renders `title` as the page's single `<h1>`. Use sequential `##` (H2) and `###` (H3) headings only.
   - Never leave template placeholders like `{city}`, `{state}`, or `[CITY]`.

3. **Immediate Financial Stakes & Zero Travel-Guide Fluff:**
   - Open the first paragraph immediately with concrete dollar stakes ($X,XXX–$XX,XXX) and the exact state statutory form or inspection standard.
   - Never begin with travel-brochure introductions about local scenery, culture, or dining (which GA4 demonstrated caused immediate 85%+ bounce rates).

4. **Genuine Technical, Legal & Financial Depth (1,300–1,800 Words):**
   - Cover every statutory form name, code section, inspection standard, and negotiation nuance listed in the row's `Focus & Statutory / Technical Details` column.
   - Include an **itemized contractor cost breakdown table ($5,000–$50,000+)** detailing inspection, remediation, and structural repair ranges—articles with cost tables achieved 4 to 9+ minutes of engaged reading time in GA4.
   - Explain *why* sellers or inspectors phrase defects vaguely inside 100+ page disclosure packets.

5. **Conversational Query-Matching FAQ Section:**
   - Include a **3–4 question FAQ section** (`## Frequently Asked Questions About...`) answering exact conversational queries discovered in Search Console (e.g., *"Can termites damage my house structure in one year?"*, *"What is a termite letter and who pays for it?"*, *"Are termite inspections legally mandatory in [State]?"*).

6. **Internal Linking (Mandatory — 2 to 3 Links Per Article):**
   - Naturally weave **2 to 3 contextual Markdown links** inside the body pointing to relevant existing guides on the site, prioritizing `priorityInternalLinkTargets` from `active-sprint.json` (such as `/blog/texas-trec-sellers-disclosure-guide/`, `/blog/california-tds-spq-disclosure-guide/`, `/blog/how-to-write-repair-credit-addendum-after-inspection/`, `/blog/5-disclosure-red-flags/`, or ranking city guides).

7. **Tailored Mid-Article Callout (No Duplicate Bottom CTA):**
   - Halfway through the article (before the manual-review or negotiation section), include one clean mid-article HTML callout with an `<h3>` heading specifically tailored to the exact document or defect:
     ```html
     <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-left: 4px solid #16a34a; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 2rem 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
       <h3 style="margin-top: 0; color: #166534; font-size: 1.1rem; font-weight: 700;">Reviewing a [State / Defect] Disclosure or Inspection Packet?</h3>
       <p style="margin-bottom: 0; color: #15803d; font-size: 1rem;">Let <strong style="color: #166534;">DisclosurePro AI</strong> cross-check your seller disclosures, inspection reports, and repair credit limits in seconds. <a href="/download" style="color: #16a34a; font-weight: 700; text-decoration: underline;">Analyze your 1st property free.</a></p>
     </div>
     ```
   - **Do NOT add a bottom CTA section** at the end of the Markdown file—`BlogPost.astro` automatically appends `<CallToAction />` right after the FAQ section.
