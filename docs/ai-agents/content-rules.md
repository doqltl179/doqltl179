# Content Rules

## When

- you are about to write or change README prose, a badge, an image, or a link,
- you need the rule against unverified claims,
- you need the file format required for this repository.

This page owns how a claim is written. It does not own what the claim's value is — that belongs to [profile-facts.md](profile-facts.md).

## Route Away When

- you need a value, a link target, or a version: [profile-facts.md](profile-facts.md),
- you changed one language file and need the other two: [readme-sync.md](readme-sync.md).

## Verify Before You Claim

- State no fact you have not checked this session. Versions, release status, link targets, and feature claims are all facts.
- Read a version from the source it lives in — `package.json`, a tag, a store page — not from the previous README. A stale README is exactly what this rule exists to catch.
- Request every external link and image before shipping it. A non-2xx response is a blocker, not a warning.
- Do not describe a feature you have not seen in the project's own current documentation or code.
- If a claim cannot be verified, drop it. Do not soften it into a vaguer claim that is still unverified.

## No Dead Or Misleading Links

- Do not link a private repository. Name the project and link nothing, or link a public surface such as a store page.
- Do not label a link as something it is not. A page that hosts build artifacts is not a portfolio.
- Prefer a link that survives: a store page over a launcher URL, a repository root over a line-numbered file.

## Voice

- Prefer concise and explicit wording over marketing language. "Custom DI container with three lifetimes" beats "production-ready, battle-tested architecture."
- Describe what the work does, not how impressive it is. Let the reader conclude.
- Keep a feature list to the items a reader can act on. A list nobody finishes is worse than a shorter one.
- Do not inflate scope. "Actively developed" and "released" are different claims; use the one that is true.

## Privacy

- Do not add an email address, phone number, messenger handle, employer, or location unless the user supplies it and asks for it.
- Do not derive a contact detail from Git configuration, commit metadata, or local files.

## File Format

- UTF-8 **without** BOM, LF line endings, in every file in this repository. `.gitattributes` enforces the endings; the BOM is on you.
- `README.md`, `README_ko.md`, and `README_ja.md` stay at the repository root. GitHub reads the profile from the root `README.md`, and the language badges point at siblings.
- Keep the three files structurally identical: same sections, same order, same badges, same images.
- Match the layout of the surrounding file rather than introducing a new style in one place.

## Notes

- If [profile-facts.md](profile-facts.md) contradicts this page on a value, that page wins; this page owns only how the value is presented.
- Add a rule here only when it applies to content generally. A rule about one project belongs in the fact table as a note.
