# Inaugural Care Drive — photo and verification notes

14 unique photographs from 16 supplied files. Exact SHA-256 duplicates omitted:
- `WhatsApp Image 2026-09-06 at 16.03.20.jpeg777.jpeg` duplicates `WhatsApp Image 2026-09-06 at 16.03.20.jpeg55.jpeg`.
- `gd.jpeg` duplicates `WhatsApp Image 2026-09-06 at 16.03.20.jpeg665.jpeg`.

Images were processed with Pillow: EXIF transpose, RGB, longest edge at most 1600px, Contrast 1.04, Color 1.05, UnsharpMask(1.2, 40, 3), progressive JPEG quality 82. The 800px variants use quality 80. Native aspect ratios are retained throughout the gallery so faces are not cropped. Caption descriptions are limited to visible content.

| Chapter | Original | Output | Caption |
|---|---|---|---|
| I | WhatsApp Image 2026-09-06 at 16.03.16.jpeg | 01-arrival-entrance.jpg | A group holds the foundation banner outside the blue Shanti Daan building. |
| I | WhatsApp Image 2026-09-06 at 16.03.16.jpeg2.jpeg | 02-foundation-banner.jpg | The foundation banner hangs on an indoor wall. |
| II | WhatsApp Image 2026-09-06 at 16.03.16.jpeg 1.jpeg | 03-provisions-table.jpg | Packaged food, vegetables and hygiene products are arranged on a cloth-covered table. |
| II | WhatsApp Image 2026-09-06 at 16.03.21.jpeg99.jpeg | 04-team-with-supplies.jpg | A group stands behind a table of provisions in front of the foundation banner. |
| II | WhatsApp Image 2026-09-06 at 16.03.17.jpeg4.jpeg | 05-provisions-and-banner.jpg | A wide view shows the provisions table beside the foundation banner. |
| III | WhatsApp Image 2026-09-06 at 16.03.17.jpeg34.jpeg | 06-yellow-package.jpg | Two people hold a yellow package together in front of the banner. |
| III | WhatsApp Image 2026-09-06 at 16.03.18.jpeg22.jpeg | 07-red-package.jpg | Two people hold a red package together in front of the banner. |
| III | WhatsApp Image 2026-09-06 at 16.03.18.jpeg23.jpeg | 08-bag-of-potatoes.jpg | Two people hold a clear bag of potatoes together. |
| III | WhatsApp Image 2026-09-06 at 16.03.18.jpeg344.jpeg | 09-yellow-bag-handover.jpg | A standing person and a person seated in a wheelchair hold a yellow bag together. |
| III | WhatsApp Image 2026-09-06 at 16.03.20.jpeg55.jpeg | 10-shared-provisions.jpg | A person wearing a cap holds a package with a seated person as others look on. |
| III | WhatsApp Image 2026-09-06 at 16.03.20.jpeg665.jpeg | 11-green-package-handover.jpg | A standing person and a seated person hold a green package together. |
| IV | WhatsApp Image 2026-09-06 at 16.03.20.jpeg88.jpeg | 12-smiles-together.jpg | Two people stand with their arms around each other and give thumbs-up gestures. |
| IV | WhatsApp Image 2026-09-06 at 16.03.21.jpeg900.jpeg | 13-group-portrait.jpg | A group poses in front of the banner, with several people holding packages. |
| IV | WhatsApp Image 2026-09-06 at 16.03.21.jpeg8908.jpeg | 14-hall-together.jpg | People gather across the hall around a trolley loaded with provisions. |

## Verification

- Python HTTP server + Playwright/Chromium at 1440px and 390px.
- No local 404s, console errors, failed requests or horizontal overflow in the final journal checks.
- All page images decoded successfully, including all 14 gallery photographs.
- All 14 photographs visited in the viewer at both widths; keyboard arrows, wraparound, next/previous buttons, thumbnails, focus containment and return, Escape and close button passed.
- Mobile swipe, mobile navigation and reduced-motion behavior passed.
- Seva Journal footer destinations checked on all 23 root/program pages.
- Homepage story and Impact milestone links checked.
- The standard Google Fonts responses were cached byte-for-byte for browser verification because external font requests were unreliable in this environment; production font links remain unchanged.

## Client review before merge

- Confirm Shanti Daan / the Missionaries of Charity approved publishing these photos, since residents are identifiable.
- Approve or replace the Chapter IV quote: “What stayed with us was not the provisions. It was the time we spent together.” — Ananth Seva team.

The existing production-domain placeholders in Open Graph metadata and sitemap.xml are retained consistently with the site. This change creates a feature PR and does not merge or change PR #1.
