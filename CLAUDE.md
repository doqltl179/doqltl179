# CLAUDE.md

Work instructions for this repository are owned by one shared entry point. The line below loads it directly.

@.github/copilot-instructions.md

Keep no copy of the rules here. Entry points differ per tool — Codex arrives through [`AGENTS.md`](AGENTS.md), Claude Code through this file, Copilot through [`.github/copilot-instructions.md`](.github/copilot-instructions.md) — and all three must land in the same place. Once instructions split per entry point, only one side gets fixed.

If anything in this file ever conflicts with `.github/copilot-instructions.md`, that file wins.

## Claude Code Specifics

- The shared staleness sweep lives at [`.github/skills/profile-refresh/SKILL.md`](.github/skills/profile-refresh/SKILL.md) so every tool runs the same procedure.
- Claude Code-only commands belong under `.claude/`. Register each one in [docs/ai-agents/README.md](docs/ai-agents/README.md) with the canonical page it walks, so the procedure keeps a single owner.
