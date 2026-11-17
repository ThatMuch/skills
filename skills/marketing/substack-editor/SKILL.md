---
name: substack-editor
description: >-
  Use when turning a topic or a finished text into a Substack post ready to
  paste, or when putting an article into the Substack editor as a draft.
metadata:
  adapted_from: lifegenieai/substack-editor
---
# Substack editor

Adapted from lifegenieai/substack-editor, keeping the author's own voice instead of a generic one.

## 1. Match the author's voice
- Before writing or editing, read 3-5 of the publication's recent posts (public archive: `https://<pub>.substack.com/api/v1/archive?sort=new&limit=10`, full text via `/api/v1/posts/<slug>` field `body_html`). Copy their structure, length, register (tu/vous), and recurring sections; never impose an outside tone.
- Short paragraphs (1-3 sentences), clear H2/H3 hierarchy, varied sentence length.
- No AI-isms (e.g. "delve", "leverage", "tapestry", "plongée au cœur de", "dans un monde où"). Avoid em dashes; use commas, colons or periods.
- Hook with immediate value in the first ~100 words. End with an open question or the author's usual sign-off to invite replies/comments.
- Never invent stats, quotes or cases; source every figure with a link, and label hypothetical examples as such.

## 2. Metadata package (deliver with the draft)
- Title (aim ≤ 60-70 chars for SEO; long titles are fine if that's the author's habit) and 2 alternatives.
- Subtitle: HARD LIMIT 200 characters in Substack.
- URL slug suggestion (3-5 words, keyword included).
- Email subject line if different from the title, and a ~150-char SEO description.
- Target keyword (in title and first 100 words).
- 3-5 internal links to earlier posts.
- Image suggestion with alt text and credit.

## 3. Make the body paste cleanly into Substack
- Produce clean semantic HTML (h2, h3, p, strong, em, a, ul/ol/li, blockquote). No CSS/JS.
- Substack's editor has NO tables: convert every table to bullet lists (one item per row, columns written out in a sentence).
- No code blocks for templates/forms: use bold labels + `<ul><li>` lists. Make sure each line is a real `<li>`, not a `<p>` starting with "- " (in Markdown, leave a blank line between a bold label and its list).
- Leave title and subtitle out of the body HTML; they have their own fields.
- Remove HTML comments/placeholders before pasting.

## 4. Put it in Substack as a draft
- New post: `https://<pub>.substack.com/publish/post?type=newsletter`. Fill title, subtitle, then paste the body (open the HTML in a browser tab served locally, e.g. `python3 -m http.server`, since file:// may be blocked; select all, copy, paste with the real keyboard).
- Wait for the "Saved"/"Enregistré" indicator. Check: headings, links, lists came through, no stray ``` or run-together text, body ends correctly.
- Never click Continue/Publish/Schedule unless the user explicitly approved publishing. Stop any local server afterwards.
- Report the editor URL and anything left to fix (e.g. image).
