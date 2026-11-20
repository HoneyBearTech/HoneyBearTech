# Plan: readme-metrics-image

## What Sean asked for

"add the metrics image to the profile README"

## What we found

- The Metrics workflow (`.github/workflows/metrics.yml`) commits `github-metrics.svg` to the `metrics` branch, not to `main`. Its latest run (20 Nov 2026) worked and the image has no errors.
- The README doesn't show the image yet. Because the image lives on another branch, the README has to link to it by its full address: `https://raw.githubusercontent.com/HoneyBearTech/HoneyBearTech/metrics/github-metrics.svg`.
- The image is 480 pixels wide and about 2,070 pixels tall (header, activity, community, repositories and the plugin sections).

## What we'll change

1. **Add a "📊 GitHub metrics" section to `README.md`**, between "Open-source contributions" and "Contribution graph", in the same heading style as the other sections. It shows the image, links to it, and has alt text.
   - Check: the link returns the image (HTTP 200, `image/svg+xml`); the section sits where planned; nothing else in the README changes, including the contributions block the contributions workflow rewrites (between its `CONTRIBUTIONS:START` and `CONTRIBUTIONS:END` markers).

Nothing else changes: no workflow changes.

## Who's on it

Engineer, Security Officer, Auditor.

## Risks

- **The image is tall.** If Sean would rather it be collapsed behind a "Show" toggle (like the latest pull requests list), that's a one-line change; say so on this PR.
- **The image is public.** It now shows two GitHub projects (Homelab and Software) with some item titles. If either should stay out, that's a separate change to the Metrics workflow's settings.
- GitHub caches README images for a short while, so a new render can take a few minutes to show.

## Out of scope

- Changing what the image shows, or the Metrics workflow.
- Any other README wording.
