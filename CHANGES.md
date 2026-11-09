# Ananth Sarth Seva Foundation - Updates & Client Action Required

This document logs the changes made to achieve the launch-ready state and highlights client decisions needed before going live.

## Changes Completed
- **7 New Pages Built:** Added `impact.html`, `partner.html`, `privacy.html`, `terms.html`, `donation-policy.html`, `refund-policy.html`, and `accessibility.html`.
- **33 New Initiatives Added:** The 6 core pillar pages now contain 10 distinct, action-oriented initiatives each (60 total), as per the requirements document.
- **Unique Icons:** Every single initiative card now has a distinct, semantically meaningful Lucide SVG icon, completely removing the "template" look.
- **Spelling Corrected:** Enforced "Ananth Sarth Seva Foundation" consistently across all user-facing copy on the site.
- **Visual Polish:** Fixed the watermark bleed issue, added consistent section vertical rhythm (96px desktop / 56px mobile), implemented scroll-reveal animations, and added image blocks with premium styling to program pages.
- **Accessibility:** Semantic structure improved, contrast ensured, and an accessibility statement added.

---

## 🛑 CLIENT ACTION REQUIRED: Placeholders to Fill

Please search the codebase for the exact string `[CLIENT:` and replace these placeholders with your official information before launching:

### Footer & Legal Pages (`privacy.html`, `terms.html`, etc.)
- `[CLIENT: REGISTERED OFFICE ADDRESS]`
- `[CLIENT: PHONE NUMBER]`
- `[CLIENT: OFFICIAL EMAIL]`
- `[CLIENT: REGISTRATION NUMBER]`
- `[CLIENT: 80G CERTIFICATE NUMBER]`
- `[CLIENT: 12A REGISTRATION NUMBER]`
- `[CLIENT: PAN]`
- `[CLIENT: GRIEVANCE OFFICER NAME/CONTACT]` (in `privacy.html`)

### Impact Page (`impact.html`)
- `[CLIENT: NUMBER OF COMMUNITIES REACHED]`
- `[CLIENT: NUMBER OF LEARNERS SUPPORTED]`
- `[CLIENT: NUMBER OF WOMEN ENTREPRENEURS]`
- `[CLIENT: HECTARES RESTORED]`
- `[CLIENT: LINK TO FINANCIALS]`

---

## 🛑 DOMAIN & SPELLING DISCREPANCY

While we have corrected all **user-facing text** to say "Ananth Sarth Seva Foundation" (matching the logo), there are hardcoded inconsistencies in the infrastructure that you need to make a decision on:

1. **GitHub Repository Name:** Currently named `anath-sarth-seva-foundation` (missing the "n" in Ananth).
2. **Current Official Email Link:** `contact@anathsarthsevafoundation.org` (missing the "n").

**Decision Needed:** If the official registered name and domain is meant to be **Ananth**, you should update the domain registration and email addresses to match, and then update the `mailto:` links in the footer and contact pages. If the domain is intentionally registered as `anath...`, let us know if we should revert the spelling.

---

## Mobile UX & accessibility pass (Nov 2026)

Based on the mobile UX / accessibility / conversion audit.

### Done in code
- **Forms now deliver.** Volunteer, contact, careers and newsletter forms no longer POST to the static server (which returned 405). Without a backend, they open the visitor's email app pre-filled to the foundation's address and show an on-page "What happens next" message. Set `FORM_ENDPOINT` in `assets/js/utils.js` (Formspree, Web3Forms or a Google Apps Script URL) to switch to direct submission with in-page success/error states.
- **Donate is reachable on phones.** Compact Donate button in the mobile header on every page; hero primary CTA is now "Donate via UPI"; drawer shows Donate/Volunteer at the top.
- **Hero copy** says who is helped and what the foundation does; links to the 30 Aug 2026 field story.
- **Donate page:** artwork hidden on phones so amounts appear sooner; "Did your payment go through?" panel after returning from the UPI app; sticky bar hides while typing or when the main pay button is visible; safe-area offset for iPhones; step numbers visible again; no-JS fallback with UPI ID.
- **Trust:** removed live placeholder team cards, placeholder phone/address lines, the Reg/80G/12A/PAN strip with blank values, and social icons linking to `#`.
- **Accessibility:** eyebrow gold darkened on light backgrounds (≥4.5:1); `--muted-light` darkened; primary button fill lightened (navy text 5.3:1); drawer traps focus and Escape only acts when open; 44px+ drawer rows; content visible without JavaScript; corrected misleading image alt text.
- **Performance:** hero image no longer downloaded on mobile; 800px programme images (~30–80 KB instead of 400–600 KB) and a 256px logo via `srcset`.

### Still needs the foundation
- Registration type/number, PAN, registered address, phone, named trustees (then restore the team section and a "Who you're paying" block on Donate).
- Decide Ananth vs Anath domain/email; the site still uses `contact@anathsarthsevafoundation.org`.
- `[CLIENT: JURISDICTION]` in `terms.html` and `[CLIENT: PRODUCTION DOMAIN]` in meta tags/sitemap.
- Written photo consent from Shanti Daan before promoting resident photos further.
- Real social profile URLs, if wanted back in the footer.
- Test the UPI deep link on real Android/iOS phones with ₹1 payments.
