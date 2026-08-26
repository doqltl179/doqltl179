# Git Workflow

## When

- a branch, commit, push, or pull request is about to happen,
- you need to know what may land on `main`.

## Branch Policy

- `main` is the release branch and the branch GitHub renders the profile from. **It takes no direct commit.** Every change arrives through a merged pull request.
- This repository has no `develop`. A task branch is cut from `origin/main` and its pull request goes back into `main`.
- Name a task branch `<type>/<scope>-<summary>` in lowercase, where `<type>` is a Conventional Commit type: `docs`, `fix`, `chore`, `feat`. Most work here is `docs`.
- Being on a branch that does not belong to the current task is a hard stop: inspect and report it before any edit, commit, or push.

## Normal Flow

1. Preflight before editing:

   ```bash
   git status --short --branch
   git fetch origin
   git rev-list --left-right --count origin/main...HEAD
   ```

2. Cut the task branch from `origin/main`, not from whatever is checked out:

   ```bash
   git fetch origin && git switch -c <type>/<scope>-<summary> origin/main
   ```

3. Review `git diff` and `git status --short --untracked-files=all`, then group files by one concern at a time.
4. Stage explicit paths and commit that concern with a focused message. Never use `git add .`.
5. Run `python tools/verify-readmes.py` and keep its output for the pull request body.
6. Push and verify the remote tip: `git push -u origin <branch>`.
7. Open the pull request into `main`. **No CI runs here** — nothing checks the destination, the branch name, or a dead link for you, so confirm them yourself before opening.
8. After it merges, delete the task branch locally and on the remote, then fast-forward local `main` from `origin/main`.

## Pull Request Body

Because a reviewer cannot run anything, the body carries the evidence:

- what changed, per file,
- which facts were re-verified and against what source,
- the URL check output,
- anything a human still has to eyeball, such as rendered layout in both GitHub color modes.

## Language

- Write commit messages, pull request titles, and pull request bodies in **Korean**. The owner reviews in Korean, and a record they have to translate before reading is a record that does not get read.
- Keep version-controlled prose in English: the primary `README.md`, and the agent documentation under `docs/ai-agents/` and `.github/`. That matches the sibling `Mu3Library_ForUnity` documentation set, so an agent moving between the two repositories reads one language.
- `README_ko.md` and `README_ja.md` are translations and follow [readme-sync.md](readme-sync.md) instead.
- Never translate an identifier: branch names, Conventional Commit types and scopes, file paths, commands, and version numbers stay as they are.

## Notes

- Push only what the user asked for. Opening a pull request is a separate action from merging it; never merge without being asked.
- Deleting a merged task branch needs no separate approval once `git log --oneline main..<branch>` is empty. Anything else that deletes or moves a file does.
