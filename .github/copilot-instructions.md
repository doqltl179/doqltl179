# doqltl179 Profile — Work Entry Point

This file is the **shared entry point**. Copilot reads it directly, Codex arrives through [`AGENTS.md`](../AGENTS.md), Claude Code through [`CLAUDE.md`](../CLAUDE.md); those two carry directions only, never a copy. **This file only lays out routes** — each rule's body belongs to the canonical page beside it. Read this once, analyze the task, then open only the smallest route it selects, and stop at the first owning page.

This repository ships one product: the GitHub profile README, in three languages. Everything here exists to keep those three files true and in sync.

## Where To Go

| What you are doing | Open |
|---|---|
| Handling one request from start to report | [request-lifecycle.md](../docs/ai-agents/request-lifecycle.md) |
| Stating a fact about a project, version, link, or status | [profile-facts.md](../docs/ai-agents/profile-facts.md) |
| Writing or editing README prose, badges, or images | [content-rules.md](../docs/ai-agents/content-rules.md) |
| Changing one README and carrying it into the other two | [readme-sync.md](../docs/ai-agents/readme-sync.md) |
| Branch, commit, push, or pull request work | [git-workflow.md](../docs/ai-agents/git-workflow.md) |
| Running the periodic staleness sweep | [profile-refresh](skills/profile-refresh/SKILL.md) |

Sections not named above are reached through [docs/ai-agents/README.md](../docs/ai-agents/README.md).

## Stop First

Hold these before the canonical pages are read. Each line's body and exceptions live on the page after the dash.

- **Do not commit on `main`.** It receives changes only through a merged pull request — git-workflow
- **Cut a task branch from `origin/main` before the first edit,** named `<type>/<scope>-<summary>` — git-workflow
- **Do not state a fact you have not verified this session.** A version number, a release status, a link target, and a feature claim are all facts — content-rules, profile-facts
- **Do not link a private repository.** Name the project without a link instead; a 404 on a profile page is worse than no link — content-rules
- **Never edit one README alone.** `README.md`, `README_ko.md`, and `README_ja.md` change in the same commit — readme-sync
- **One fact has one owner.** The fact table owns values; the three READMEs render them — profile-facts
- **Ask before adding a person's contact details.** Email, phone, and messenger handles are the user's call, not yours — content-rules

## When You Edit Docs

- One fact has one owner; every other page links to it instead of restating it.
- Adding a route here means adding a row, not a rule body. If a new rule has nowhere to live, create or extend its canonical page first, then link it.
- Keep this file under 45 lines, UTF-8 without BOM, LF endings — [content-rules.md](../docs/ai-agents/content-rules.md).
