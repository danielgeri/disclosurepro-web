# DisclosurePro Programmatic SEO Prompt Template

Copy and paste this prompt into Gemini to generate a highly comprehensive, long-form, hyper-localized SEO blog post (1,000+ words). 
Replace `[CITY]`, `[STATE]`, and `[TOPIC]` with the desired targets from the tracking spreadsheet.

> **Important:** After you generate and save the blog post, make sure to open `docs/seo/tracking.csv` and mark an 'x' in the corresponding cell to track our progress!

---

**Prompt:**

Act as an expert real estate attorney and top-producing local real estate agent in [CITY], [STATE]. Write a highly engaging, long-form, SEO-optimized comprehensive guide (at least 1,000 to 1,500 words) about "[TOPIC]" for homebuyers in [CITY]. 

Follow these strict constraints:
1. **Format:** Return ONLY raw markdown. Do not include any conversational filler before or after the markdown. 
2. **No Repetition:** Ensure there is zero duplicated content. Do NOT repeat the same paragraphs, sentences, or phrases anywhere in the article. Double-check your output to prevent repetition loops.
3. **Frontmatter:** The markdown must begin with Astro frontmatter exactly matching this structure (fill in the variables):
```yaml
---
title: "[Catchy SEO Title including City and Topic - e.g. The Ultimate Guide to Spotting Termite Damage in Chicago Real Estate Disclosures]"
description: "[Compelling 2-3 sentence meta description]"
pubDate: "[Current Date, e.g., Aug 03 2026]"
heroImage: "../../assets/red_flags_hero.jpg"
---
```
3. **Comprehensive Depth (1000+ Words):** The post MUST be highly detailed. Use an introductory hook, deep explanations of the specific [TOPIC], the biology/mechanics of why it happens, and how the climate or housing stock in [CITY] (e.g. historical districts, weather patterns) exacerbates it.
4. **Local Laws & Regulations:** Dedicate a specific H2 section to [STATE] real estate disclosure laws. Explain the exact forms a buyer receives (e.g., California TDS, Texas Seller's Disclosure Notice, New York Property Condition Disclosure Statement) and what sellers are legally obligated to reveal vs. conceal.
5. **The Manual Review Problem:** Emphasize how difficult and risky it is for a homebuyer to manually read through hundreds of pages of disclosure documents to find this specific issue. Explain how sellers use vague language (e.g., "prior treatment", "settlement cracks").
6. **Financial Impact & Case Study:** Include a hypothetical (but realistic) case study of a homebuyer in a specific [CITY] neighborhood who missed this red flag in the disclosures and the resulting financial devastation (provide specific estimated repair costs in dollars).
7. **FAQ Section:** Include an H2 titled "Frequently Asked Questions about [TOPIC] in [CITY]" with 3-4 common questions and detailed answers.
8. **Mid-Article Callout:** Halfway through the article (before discussing the manual review problem), inject this exact HTML block to serve as a pattern-interrupt CTA:
```html
<div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-left: 4px solid #16a34a; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 2rem 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
  <h4 style="margin-top: 0; color: #166534; font-size: 1.1rem; font-weight: 700;">Tired of manually reading 200-page disclosures?</h4>
  <p style="margin-bottom: 0; color: #15803d; font-size: 1rem;">Let <strong style="color: #166534;">DisclosurePro AI</strong> scan your documents for hidden termite damage, structural issues, and unpermitted work in 10 seconds. <a href="/download" style="color: #16a34a; font-weight: 700; text-decoration: underline;">Try it free today.</a></p>
</div>
```
9. **No Bottom CTA:** Do NOT include a concluding CTA section at the bottom of the article. The site's global layout will automatically append a highly-stylized CallToAction Astro component at the bottom of every blog post. End the article directly after the FAQ section.
10. **Styling:** Use rich Markdown formatting (bolding, lists, blockquotes, H2 and H3 tags) to make the post highly readable and scannable for SEO.

---
