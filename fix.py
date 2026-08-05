import os
import glob
import re

blog_dir = "/Users/danielgeri/Documents/disclosurepro-web/src/content/blog"
files = glob.glob(os.path.join(blog_dir, "*.md"))

duplicate_phrase = "Furthermore, the complex interaction between soil types"

mid_cta_html = """
<div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-left: 4px solid #16a34a; padding: 1.5rem; border-radius: 0 8px 8px 0; margin: 2rem 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
  <h4 style="margin-top: 0; color: #166534; font-size: 1.1rem; font-weight: 700;">Tired of manually reading 200-page disclosures?</h4>
  <p style="margin-bottom: 0; color: #15803d; font-size: 1rem;">Let <strong style="color: #166534;">DisclosurePro AI</strong> scan your documents for hidden termite damage, structural issues, and unpermitted work in 10 seconds. <a href="/download" style="color: #16a34a; font-weight: 700; text-decoration: underline;">Try it free today.</a></p>
</div>
"""

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # 1. Remove duplicate paragraphs
    if duplicate_phrase in content:
        # Split by the duplicate paragraph
        parts = content.split(duplicate_phrase)
        if len(parts) > 2:
            # Reconstruct keeping only the first instance
            # The parts[1] will have the rest of the first paragraph.
            # Actually, let's just find the exact paragraph.
            # Since the paragraph is exact, we can use regex to replace multiple occurrences.
            # Let's find the full paragraph.
            lines = content.split('\n')
            new_lines = []
            found = False
            for line in lines:
                if line.startswith(duplicate_phrase):
                    if not found:
                        new_lines.append(line)
                        found = True
                    else:
                        pass # skip duplicates
                else:
                    new_lines.append(line)
            content = '\n'.join(new_lines)
            
    # 2. Strip bottom CTA
    # The CTA always starts with "## Protect Your"
    cta_index = content.find("## Protect Your")
    if cta_index != -1:
        content = content[:cta_index].strip() + '\n'
        
    # 3. Inject Mid-Article CTA (if not already there)
    if "Tired of manually reading" not in content:
        # Inject after the first H2 that is not the first one.
        # Let's just find "## " and inject before the 2nd one.
        h2_indices = [m.start() for m in re.finditer(r'^## ', content, re.MULTILINE)]
        if len(h2_indices) > 1:
            inject_pos = h2_indices[1]
            content = content[:inject_pos] + mid_cta_html + "\n\n" + content[inject_pos:]

    with open(filepath, 'w') as f:
        f.write(content)

print("Fixed files.")
