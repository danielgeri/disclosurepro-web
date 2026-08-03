# DisclosurePro Programmatic SEO Prompt Template

Copy and paste this prompt into Gemini to generate a hyper-localized blog post. 
Replace `[CITY]`, `[STATE]`, and `[TOPIC]` with the desired targets from the tracking spreadsheet.

---

**Prompt:**

Act as an expert real estate attorney and local real estate agent in [CITY], [STATE]. Write a highly engaging, SEO-optimized blog post about "[TOPIC]" for homebuyers in [CITY]. 

Follow these strict constraints:
1. **Format:** Return ONLY raw markdown. Do not include any conversational filler before or after the markdown. 
2. **Frontmatter:** The markdown must begin with Astro frontmatter exactly matching this structure (fill in the variables):
```yaml
---
title: "[Catchy SEO Title including City and Topic]"
description: "[Compelling 2-3 sentence meta description]"
pubDate: "[Current Date, e.g., Aug 03 2026]"
heroImage: "../../assets/blog-placeholder-1.jpg"
---
```
3. **Localization:** Mention specific local real estate laws, [STATE] disclosure requirements (e.g., TDS in California, Seller's Disclosure Notice in Texas), and specific [CITY] neighborhoods or local housing quirks (e.g., age of homes, weather impacts).
4. **Pain Points:** Emphasize how difficult and risky it is for a homebuyer to manually read through hundreds of pages of disclosure documents to find this specific issue. 
5. **Call to Action (CTA):** Conclude the post with a strong CTA section titled "Protect Your [CITY] Investment with DisclosurePro AI". Explain how DisclosurePro AI instantly analyzes these massive disclosure packets, finds the red flags, and calculates repair credits. Include a Markdown link at the end: `[Try DisclosurePro AI Free Today](/download)`.
6. **Styling:** Use Markdown formatting (bolding, lists, H2 and H3 tags) to make the post highly readable.

---
