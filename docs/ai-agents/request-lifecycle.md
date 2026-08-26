# Request Lifecycle

## When

- any request against this repository starts and the order of work is the question,
- you need the stop-or-pause rule before editing.

This page owns the order in which one request is handled. It does not own content rules, fact values, or branch mechanics; each step links to the page that does.

## Required Order

1. Extract scope, exclusions, and completion conditions from the request. The current user request is authoritative.
2. Assess feasibility before editing.
   - If the outcome is impossible, stop and report why.
   - If it needs a scope expansion or a choice that is not yours — which projects to feature, whether to publish a contact detail, whether to add a language — pause and ask.
   - Do not invent a workaround to make an underspecified request look complete.
3. Run the branch preflight and cut the task branch from `origin/main`. See [git-workflow.md](git-workflow.md). `main` takes no direct commit.
4. Verify every fact the change will state, and update [profile-facts.md](profile-facts.md) first when a value moved. Verification rules are in [content-rules.md](content-rules.md).
5. Edit all three READMEs together, following [readme-sync.md](readme-sync.md).
6. Run `python tools/verify-readmes.py` and record its output. See [readme-sync.md](readme-sync.md).
7. Open the pull request into `main` with that evidence in the body. See [git-workflow.md](git-workflow.md).
8. Report what changed, what you verified, and every claim you dropped for being unverifiable.

## Keep The Work Bounded

- Answer with the smallest clear result that completes the request.
- This repository has no build and no test. `tools/verify-readmes.py` **is** the verification — skipping it means shipping unverified.
- Rendering is only checked by a person looking at the pull request. Say so plainly instead of implying the layout was confirmed.

## Notes

- If a step's canonical page contradicts this order, the canonical page owns the detail and this page owns only the sequence.
