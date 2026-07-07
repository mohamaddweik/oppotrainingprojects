---
name: ui-review
description: Use when the user asks to review the UI with Playwright, fix issues, and push the changes.
---

# UI Review (Playwright) -> Fix -> Commit & Push

When this runs:
1. Start a local server for the landing page if one isn't
   already running (e.g. `npx serve .` or similar), or open
   the HTML file directly if no server is needed.
2. Use Playwright to open the page in a browser and take a
   full-page screenshot at both desktop (1440px) and mobile
   (375px) widths.
3. Visually inspect the screenshots against design-reference.png.
   Check for: broken layout, overlapping elements, bad spacing,
   unreadable contrast, missing responsiveness, misaligned text.
4. Fix any issues found directly in the code.
5. Re-run the Playwright screenshot check to confirm the fixes
   actually worked.
6. Once confirmed, run: git add ., git commit with a message
   describing what was fixed, and git push to origin.
7. Reply with a short summary of what was reviewed, what was
   fixed, and confirm the push succeeded.