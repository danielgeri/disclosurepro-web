# DisclosurePro High-Intent SEO Editorial Guidelines

Use these instructions when generating articles from [`docs/seo/editorial-queue.csv`](./editorial-queue.csv).
On each scheduled run, take the **next 3 rows** in `editorial-queue.csv` where `Completed` is empty (in ascending `Priority` order), write each article at `src/content/blog/<Slug>.md`, mark `Completed` as `x` in `editorial-queue.csv`, verify the build with `ASTRO_TELEMETRY_DISABLED=1 npm run build`, and push to `main`.

> **Important:** Once every row in `editorial-queue.csv` is marked `x`, **STOP and do nothing**—do NOT clear the CSV or regenerate duplicate articles.

---

## Authoring & Quality Rules

1. **Authoritative Research Team Voice (No Impersonation):**
   - Write from the perspective of the **DisclosurePro Real Estate Research Team**—an objective, deeply researched real estate due-diligence guide.
   - **NEVER** claim first-person licensure (e.g., do NOT write *"As an experienced real estate attorney and managing broker in..."*).

2. **Format & Single `<h1>` Rule:**
   - Return pure Markdown starting with Astro YAML frontmatter:
     ```yaml
     ---
     title: "<Exact or refined Proposed Title from editorial-queue.csv>"
     description: "<Unique, compelling 140–160 character meta description naturally incorporating the Target Keyword>"
     pubDate: "<Current Date, e.g., Nov 11 2026>"
     heroImage: "../../assets/red_flags_hero.jpg"
     ---
     ```
   - **Do NOT start the Markdown body with `# Title`**—`BlogPost.astro` already renders `title` as the page's single `<h1>`. Use sequential `##` (H2) and `###` (H3) headings only.
   - Never leave template placeholders like `{city}`, `{state}`, or `[CITY]`.

3. **Genuine Technical, Legal & Financial Depth (1,300–1,800 Words):**
   - Cover every statutory form name, code section, inspection standard, and negotiation nuance listed in the row's `Focus & Statutory / Technical Details` column.
   - Include concrete, realistic contractor repair cost ranges in dollars (`$X,XXX – $XX,XXX`) and explain *why* sellers or inspectors phrase defects vaguely inside 100+ page disclosure packets.
   - Include a realistic buyer scenario/case study and a **3–4 question FAQ section** (`## Frequently Asked Questions...`) answering real buyer questions concisely.

4. **Internal Linking (Mandatory — 2 to 3 Links Per Article):**
   - Naturally weave **2 to 3 contextual Markdown links** inside the body pointing to relevant existing guides on the site (verify the target `.md` file exists in `src/content/blog/`), such as:
     - `/blog/california-tds-spq-disclosure-guide/`
     - `/blog/texas-trec-sellers-disclosure-guide/`
     - `/blog/hoa-reserve-study-special-assessment-red-flags/`
     - `/blog/5-disclosure-red-flags/`
     - Or any previously completed guide in `src/content/blog/`.

5. **Mid-Article Callout & No Duplicate Bottom CTA:**
   - Halfway through the article (before the manual-review or negotiation section), include one clean mid-article HTML callout:
     ```html
     <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-left: 4px solid #16a34a; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 2rem 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
       <h3 style="margin-top: 0; color: #166534; font-size: 1.1rem; font-weight: 700;">Reviewing a 100+ page disclosure or inspection packet?</h3>
       <p style="margin-bottom: 0; color: #15803d; font-size: 1rem;">Let <strong style="color: #166534;">DisclosurePro AI</strong> cross-check your seller disclosures, inspection reports, and HOA docs for hidden repair traps in seconds. <a href="/download" style="color: #16a34a; font-weight: 700; text-decoration: underline;">Analyze your 1st property free.</a></p>
     </div>
     ```
   - **Do NOT add a bottom CTA section** at the end of the Markdown file—`BlogPost.astro` automatically appends `<CallToAction />` right after the FAQ section.
