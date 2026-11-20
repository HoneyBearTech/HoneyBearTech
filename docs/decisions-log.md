# Decisions log

Why things are the way they are: each entry gives the decision, the reason and
what was turned down. Newest first. What shipped is in the [pass
map](pass-map.md).

## 2026-11-20: The metrics image goes in the README, shown in full

Job `readme-metrics-image` (#11).

**Decision.** A new "📊 GitHub metrics" section shows `github-metrics.svg` by its
full address on the `metrics` branch, between "Open-source contributions" and
"Contribution graph", shown in full rather than collapsed.

**Why.** The owner asked for the image on the profile. The workflow commits it to
its own branch, so a relative link from `main` wouldn't find it. The owner
approved the plan without asking for the collapsed version.

**Not done.** What the image shows is unchanged. It is public and now includes
two GitHub projects (Homelab and Software); leaving either out would be a
separate change to the Metrics workflow's settings. The image was checked before
embedding: no scripts or outside links, no private names, addresses or emails.

## 2026-11-20: Renovate merges its own pull requests

Job `renovate-automerge` (#9).

**Decision.** Renovate merges its pull requests itself once every check passes,
majors included; new versions wait 3 days, security fixes and image rebuilds
don't, on the model homelab-atlas already uses. Kept manual: the third-party
profile action stays manual (it runs with the deploy key). `platformAutomerge`
is false and `ignoreTests: true`: no checks run on pull requests, so the 3-day
wait is the only gate.

**Why.** The owner asked for every repo with Renovate to merge its updates
automatically (2026-11-20) and chose this model, majors included, over keeping
majors manual.

**Not done.** Repository settings and branch rules (owner only) and workflows
are unchanged. A group merges automatically only when every update in it may, so
each manual exception gets its own pull request.

**Review findings.** Fixed: stale docs that still promised a manual review or
named Dependabot, and (where it applied) exceptions that sat inside the update
group. None declined.
