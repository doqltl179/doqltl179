# README Sync

## When

- any of `README.md`, `README_ko.md`, or `README_ja.md` is being changed,
- a section is added, removed, or reordered in one language,
- a badge, image, or link changes anywhere in the profile.

This page owns the procedure that keeps the three language files identical in everything but prose.

## Route Away When

- the value being written is in question: [profile-facts.md](profile-facts.md),
- the wording or format of the claim is in question: [content-rules.md](content-rules.md).

## Scope

| File | Language | Role |
|---|---|---|
| `README.md` | English | Primary. Structure changes start here. |
| `README_ko.md` | Korean | Translation of the primary. |
| `README_ja.md` | Japanese | Translation of the primary. |

## Rules

1. **Never change one file alone.** All three move in the same commit. A partial sync is the failure this page exists to prevent, because only the language someone happens to read gets fixed.
2. Structure changes land in `README.md` first, then propagate. Prose fixes may start in any language, but still land in all three.
3. Keep section structure and visual style synchronized, not only the text: same headings, same order, same badges, same images, same collapsed `<details>` blocks.
4. Keep every URL byte-identical across the three files, except a URL that carries a language parameter of its own.
5. Translate the meaning, not the words. A Korean or Japanese sentence that reads like machine output fails this rule even when it is accurate.
6. Keep the language badge row identical in all three files, including the order of the languages.
7. Numbers, versions, and identifiers are never translated or reformatted.

## Before You Commit

```bash
python tools/verify-readmes.py
```

It checks heading skeletons, the shared URL set, that every URL answers 2xx, and that **every SVG parses as XML**. A non-zero exit is a blocker.

That last check is not decoration. A status code alone does not tell you an image works: a generator that interpolates text into SVG emits invalid XML the moment that text contains a bare `&`, answers `200` anyway, and GitHub's image proxy serves a broken image. A banner shipped that way on 2026-08-26 and passed a `2xx`-only check. See [profile-facts.md](profile-facts.md) «Image And Badge Services».

## Notes

- Adding a fourth language means adding a row to «Scope» and a badge to all existing files in the same task.
- If a section genuinely cannot exist in one language, that is a scope decision for the user, not a silent omission.
