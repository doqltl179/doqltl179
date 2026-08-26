---
name: profile-refresh
description: "Use when the profile README may have gone stale — a periodic sweep that re-verifies every fact, link, and image in the three language files and reports what decayed."
---

# Profile Refresh

## Purpose

Nothing in this repository fails when the profile goes stale. There is no build and no test, so a wrong version number or a dead link sits there until a person happens to notice — which is how a profile goes a year without an update. This sweep is the thing that notices.

Canonical rules: `../../../docs/ai-agents/profile-facts.md` owns the values, `../../../docs/ai-agents/readme-sync.md` owns the three-file sync, `../../../docs/ai-agents/content-rules.md` owns how a claim is written.

## Use This Skill When

- the profile has not been touched in months,
- a featured project shipped, changed visibility, or was retired,
- a link or an image on the profile may have died,
- the user asks whether the profile is still accurate.

## Sweep

Report findings; do not edit until the user has seen them.

1. **Inventory the account.** `gh repo list <handle> --json name,isPrivate,isFork,updatedAt,description` — look for a repository that went public, a new project worth featuring, and a featured project that went private.
2. **Re-read every version.** Pull each value in the fact table from where it actually lives — `package.json`, a Git tag, a store page — never from the README.
3. **Request every URL.** Extract them with the command in `readme-sync.md` and check each for a 2xx response. Include image URLs; a badge host that started failing is the most common silent break.
4. **Check the image services.** Confirm each card and banner still renders, not merely that the host answers. A service that returns an error card still returns `200`.
5. **Compare the three files.** Heading counts, section order, and URL sets must match.
6. **Check the deliberately-absent list.** A project listed there may have changed status — that is a question for the user, not a decision to make.

## Report

State, in this order: facts that moved, links that broke, sync gaps between the three files, and candidates the user may want to add or drop. Name the source you checked each fact against. Then stop and let the user choose what changes.

## Local Guardrails

- Verification only. Do not rewrite the profile inside this sweep.
- Do not add or remove a featured project on your own; absence is usually a decision already recorded in the fact table.
- Do not replace a working image service with a fashionable one. Replace it only when it actually failed, and record why in the fact table.
