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
