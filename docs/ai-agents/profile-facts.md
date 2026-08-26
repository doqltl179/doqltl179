# Profile Facts

## When

- you are about to write a version, a link, a release status, or a project claim into a README,
- a fact in the profile may have decayed since it was written,
- you need to know why a project is present or deliberately absent.

This page owns every value the three READMEs state. The READMEs render these values; they do not decide them. Change a value here first, then carry it into all three files through [readme-sync.md](readme-sync.md).

## Route Away When

- the question is how to word or format the claim: [content-rules.md](content-rules.md),
- the question is how to land the change: [git-workflow.md](git-workflow.md).

## Identity

| Fact | Value |
|---|---|
| GitHub handle | `doqltl179` |
| Display name | mu3 |
| Profile repository | `doqltl179/doqltl179`, default branch `main` |
| Role line | Unity game developer — framework, tooling, and shipped titles |

## Featured Projects

Verified 2026-08-26.

| Project | Link | Status | Notes |
|---|---|---|---|
| Mu3Library For Unity | https://github.com/doqltl179/Mu3Library_ForUnity | Public, actively developed | MIT, Unity 6000.0+ |
| The Echo Escape | https://store.steampowered.com/app/2875300/The_Echo_Escape/ | Released on Steam | Source repository is **private** — link the store page, never the repository |
| PostMV - ghost choir | https://github.com/doqltl179/Post_MV_ghost_choir | Public, archived in practice | Unity-rendered music video |

## Mu3Library Package Versions

Read from `package.json` in the source repository. Verified 2026-08-26.

| Package | Version | Depends on |
|---|---|---|
| `Mu3Library_Base` | 0.26.0 | — |
| `Mu3Library_URP` | 0.3.0 | Base |
| `Mu3Library_Game_WatermelonGame` | 0.6.0 | Base, URP |

Unity requirement is `6000.0` and the target framework is .NET Standard 2.1.

## External Media

| Item | Value |
|---|---|
| Steam app id | `2875300` |
| The Echo Escape trailer | YouTube `rbei7quiAF4` |
| PostMV - ghost choir | YouTube `znUe_MXd8lU` |
| Thumbnail pattern | `https://img.youtube.com/vi/<id>/0.jpg` |

## Image And Badge Services

Each one is a third-party host that can go down and take a README image with it. Confirm a live response before adding or changing a card, and prefer a service already listed here over a fourth one.

| Service | Used for |
|---|---|
| `capsule-render.vercel.app` | Header banner |
| `img.shields.io` | Language, tech, and status badges |
| `img.youtube.com` | Video thumbnails |
| `github-profile-summary-cards.vercel.app` | GitHub statistics cards, `theme=transparent` so one image reads in both GitHub color modes |

**Text interpolated into a generated SVG must be XML-safe.** A bare `&`, `<`, or `>` in a `text` or `desc` parameter produces invalid XML, the service still answers `200`, and GitHub renders a broken image. Write `and` instead of `&`, and percent-encode every non-ASCII character in the URL so each client transmits it the same way. `python tools/verify-readmes.py` catches both.

`github-readme-stats.vercel.app` was evaluated on 2026-08-26 and returned `503` on every attempt, so the statistics cards use the summary-cards service instead. Re-check before switching back.

## Deliberately Absent

Absence is a decision, not an oversight. Do not "restore" one of these without asking.

| Item | Why it is not on the profile |
|---|---|
| `MellowMerge` | Private and unreleased; the user chose not to feature work in progress |
| `UndefinedSpots` | Private and unreleased; same decision |
| `doqltl179.github.io` | Hosts asset bundles, not a portfolio — linking it as one would be false |
| Forked repositories | Not the user's own work |
| Email and other contact details | Add only when the user supplies the address and asks for it |

## Update This Page When

- a package version, Unity requirement, or license changes,
- a project changes visibility, ships, or is retired,
- a link target moves or dies,
- an image service is added, replaced, or found unreliable.

Re-stamp the «Verified» date in the section you touched, and leave the other sections' dates alone.
