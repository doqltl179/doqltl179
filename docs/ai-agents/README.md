# AI Agent Wiki

This is the wiki root. Use it only when task analysis shows that a wiki route is needed and the next owning page is not already obvious. The way here is the shared entry point [.github/copilot-instructions.md](../../.github/copilot-instructions.md).

## Choose By Question Shape

| Question | Open |
|---|---|
| In what order do I handle this request? | [request-lifecycle.md](request-lifecycle.md) |
| Is this claim true, and where does its value live? | [profile-facts.md](profile-facts.md) |
| What rules apply while writing README content? | [content-rules.md](content-rules.md) |
| How do the three language files stay in sync? | [readme-sync.md](readme-sync.md) |
| How do branches, commits, and pull requests work here? | [git-workflow.md](git-workflow.md) |

## Navigation Rules

- Routing stays shallow: entry point -> this router -> owning page. No third hop.
- Let owning pages hold detailed rules; let this page hold only the question each one answers.
- Replace a repeated rule with a link to the page that owns it.
- Add a page only when it answers a question no existing page answers. Otherwise extend the page that already owns it.

## Executors That Walk These Procedures

The skill below runs a procedure on this wiki. **The canonical page always owns the rule; this file holds only the order.** After changing a page, confirm its executor still walks the same steps.

| Executor | Follows |
|---|---|
| [profile-refresh](../../.github/skills/profile-refresh/SKILL.md) | [profile-facts.md](profile-facts.md), [readme-sync.md](readme-sync.md) |
| [tools/verify-readmes.py](../../tools/verify-readmes.py) | [readme-sync.md](readme-sync.md) «Before You Commit» |

## Why This Repository Has A Wiki At All

Three README files say the same things in three languages, and the facts inside them decay on their own: a version ships, a repository goes public, a link dies. Nothing in the repository fails when that happens — there is no build and no test, so a wrong profile stays wrong until a person notices.

So the rules here target exactly that failure: facts get one owner, claims get verified before they are written, and the three files move together. Everything else stays out.
