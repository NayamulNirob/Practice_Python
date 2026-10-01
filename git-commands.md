# Git Commands Cheat Sheet

A practical reference of Git commands, grouped by task.

---

## Table of Contents

1. [Setup & Configuration](#1-setup--configuration)
2. [Creating Repositories](#2-creating-repositories)
3. [Basic Snapshotting](#3-basic-snapshotting)
4. [Branching](#4-branching)
5. [Merging](#5-merging)
6. [Remote Repositories (push, pull, fetch)](#6-remote-repositories)
7. [Viewing History & Inspecting](#7-viewing-history--inspecting)
8. [Undoing Changes](#8-undoing-changes)
9. [Stashing](#9-stashing)
10. [Rebasing](#10-rebasing)
11. [Tagging](#11-tagging)
12. [Cherry-pick](#12-cherry-pick)
13. [Submodules](#13-submodules)
14. [Worktrees](#14-worktrees)
15. [Debugging (bisect, blame)](#15-debugging)
16. [Cleaning & Maintenance](#16-cleaning--maintenance)
17. [Aliases & Useful Shortcuts](#17-aliases--useful-shortcuts)
18. [Common Workflows](#18-common-workflows)

---

## 1. Setup & Configuration

```bash
git --version                                   # Show installed Git version
git help <command>                              # Open help for a command
git <command> --help                            # Same as above

git config --global user.name "Your Name"       # Set your name
git config --global user.email "you@example.com" # Set your email
git config --global init.defaultBranch main     # Default branch name for new repos
git config --global core.editor "code --wait"   # Set editor (VS Code)
git config --global color.ui auto               # Enable colored output
git config --global pull.rebase false           # Pull = fetch + merge (default)
git config --global pull.rebase true            # Pull = fetch + rebase
git config --global credential.helper store     # Store credentials

git config --list                               # List all settings
git config --global --list                      # List global settings
git config user.name                            # Show a specific setting
git config --global --unset user.name           # Remove a setting
git config --global --edit                      # Edit global config file
```

---

## 2. Creating Repositories

```bash
git init                                        # Initialize a new repo in current folder
git init <folder-name>                          # Initialize a new repo in a new folder
git init --bare                                 # Create a bare repository (no working dir)

git clone <url>                                 # Clone a remote repository
git clone <url> <folder>                        # Clone into a specific folder
git clone -b <branch> <url>                     # Clone a specific branch
git clone --depth 1 <url>                       # Shallow clone (latest commit only)
git clone --recurse-submodules <url>            # Clone including submodules
```

---

## 3. Basic Snapshotting

```bash
git status                                      # Show working tree status
git status -s                                   # Short status

git add <file>                                  # Stage a file
git add <folder>/                               # Stage a folder
git add .                                       # Stage all changes in current dir
git add -A                                      # Stage all changes (new, modified, deleted)
git add -u                                      # Stage modified and deleted only
git add -p                                      # Interactively stage chunks (hunks)

git commit -m "message"                         # Commit staged changes
git commit -am "message"                        # Stage tracked files + commit
git commit --amend                              # Edit the last commit
git commit --amend --no-edit                    # Add staged changes to last commit, keep message
git commit --allow-empty -m "message"           # Create an empty commit

git diff                                        # Unstaged changes
git diff --staged                               # Staged changes (same as --cached)
git diff <branch1>..<branch2>                   # Compare two branches
git diff <commit1> <commit2>                    # Compare two commits
git diff --stat                                 # Summary of changes

git rm <file>                                   # Delete a file and stage the deletion
git rm --cached <file>                          # Untrack a file but keep it locally
git rm -r <folder>                              # Remove a folder
git mv <old> <new>                              # Rename/move a file
```

---

## 4. Branching

```bash
git branch                                      # List local branches
git branch -a                                   # List all branches (local + remote)
git branch -r                                   # List remote branches
git branch -v                                   # List with last commit info
git branch --merged                             # Branches merged into current
git branch --no-merged                          # Branches not yet merged

git branch <name>                               # Create a branch
git branch <name> <commit>                      # Create a branch from a commit
git checkout <name>                             # Switch to a branch
git checkout -b <name>                          # Create and switch to a branch
git switch <name>                               # Switch to a branch (modern)
git switch -c <name>                            # Create and switch (modern)
git switch -                                    # Switch to previous branch

git branch -m <new-name>                        # Rename current branch
git branch -m <old> <new>                       # Rename a branch
git branch -d <name>                            # Delete a merged branch
git branch -D <name>                            # Force delete a branch
git push origin --delete <name>                 # Delete a remote branch

git branch -u origin/<name>                     # Set upstream for current branch
git branch --set-upstream-to=origin/<name>      # Same as above
```

---

## 5. Merging

```bash
git merge <branch>                              # Merge branch into current branch
git merge --no-ff <branch>                      # Always create a merge commit
git merge --squash <branch>                     # Squash all commits into one (not committed)
git merge --abort                               # Abort a merge in progress
git merge --continue                            # Continue after resolving conflicts

git mergetool                                   # Open the configured merge tool
git checkout --ours <file>                      # Resolve conflict: keep your version
git checkout --theirs <file>                    # Resolve conflict: keep their version
```

**Resolving conflicts:**

1. Run `git status` to see conflicted files.
2. Open the files and edit the sections between `<<<<<<<`, `=======`, `>>>>>>>`.
3. `git add <file>` to mark as resolved.
4. `git commit` (or `git merge --continue`) to finish.

---

## 6. Remote Repositories

### Managing remotes

```bash
git remote                                      # List remotes
git remote -v                                   # List remotes with URLs
git remote add origin <url>                     # Add a remote
git remote remove <name>                        # Remove a remote
git remote rename <old> <new>                   # Rename a remote
git remote set-url origin <new-url>             # Change remote URL
git remote show origin                          # Show details about a remote
git remote prune origin                         # Remove stale remote-tracking branches
```

### Push

```bash
git push                                        # Push current branch to its upstream
git push origin <branch>                        # Push a branch to origin
git push -u origin <branch>                     # Push and set upstream
git push origin main                            # Push main to origin
git push --all                                  # Push all branches
git push --tags                                 # Push all tags
git push origin <tag>                           # Push a single tag
git push origin --delete <branch>               # Delete a remote branch
git push --force-with-lease                     # Safer force push
git push --force                                # Force push (dangerous!)
git push origin <local-branch>:<remote-branch>  # Push to a differently named branch
```

### Pull & Fetch

```bash
git fetch                                       # Download changes from origin (no merge)
git fetch --all                                 # Fetch from all remotes
git fetch origin <branch>                       # Fetch a specific branch
git fetch --prune                               # Fetch and remove deleted remote branches

git pull                                        # Fetch + merge into current branch
git pull origin <branch>                        # Pull a specific branch
git pull --rebase                               # Fetch + rebase instead of merge
git pull --ff-only                              # Only fast-forward, otherwise fail
```

---

## 7. Viewing History & Inspecting

```bash
git log                                         # Full commit history
git log --oneline                               # One line per commit
git log --oneline --graph --all --decorate      # Visual branch graph
git log -n 5                                    # Last 5 commits
git log --author="Name"                         # Commits by an author
git log --since="2 weeks ago"                   # Commits since a date
git log --until="2026-01-01"                    # Commits until a date
git log --grep="keyword"                        # Search commit messages
git log -S "code"                               # Search for code changes (pickaxe)
git log -p                                      # Show patches (diffs)
git log --stat                                  # Show changed files summary
git log <file>                                  # History of a file
git log --follow <file>                         # History of a file including renames
git log main..feature                           # Commits in feature not in main
git log --pretty=format:"%h %an %s"             # Custom format

git show <commit>                               # Show a commit's details
git show <commit>:<file>                        # Show a file at a specific commit
git show HEAD                                   # Show the latest commit
git show HEAD~2                                 # Show 2 commits before HEAD

git shortlog -sn                                # Commit count per author
git reflog                                      # History of HEAD movements (recovery!)
git ls-files                                    # List tracked files
git ls-tree HEAD                                # List files in the tree
git cat-file -p <hash>                          # Show object contents
git describe --tags                             # Describe commit using nearest tag
git rev-parse HEAD                              # Get full hash of HEAD
```

---

## 8. Undoing Changes

### Discard working directory changes

```bash
git restore <file>                              # Discard changes in a file
git restore .                                   # Discard all unstaged changes
git checkout -- <file>                          # Old way to discard changes
git checkout .                                  # Old way: discard all changes
```

### Unstage files

```bash
git restore --staged <file>                     # Unstage a file
git reset HEAD <file>                           # Old way to unstage
git reset                                       # Unstage everything
```

### Reset (moves branch pointer)

```bash
git reset --soft HEAD~1                         # Undo last commit, keep changes staged
git reset --mixed HEAD~1                        # Undo last commit, keep changes unstaged (default)
git reset --hard HEAD~1                         # Undo last commit, DISCARD changes
git reset --hard <commit>                       # Reset to a specific commit
git reset --hard origin/<branch>                # Reset to match remote
```

### Revert (creates a new "undo" commit — safe for shared branches)

```bash
git revert <commit>                             # Revert a commit
git revert HEAD                                 # Revert the latest commit
git revert -m 1 <merge-commit>                  # Revert a merge commit
git revert --no-commit <commit>                 # Revert without committing
git revert --abort                              # Abort revert
```

### Recover lost commits

```bash
git reflog                                      # Find the lost commit hash
git checkout <hash>                             # Inspect it
git branch recovered <hash>                     # Save it to a new branch
git reset --hard <hash>                         # Or reset to it
```

---

## 9. Stashing

```bash
git stash                                       # Stash tracked changes
git stash push -m "message"                     # Stash with a message
git stash -u                                    # Include untracked files
git stash -a                                    # Include untracked + ignored files
git stash list                                  # List stashes
git stash show                                  # Summary of the latest stash
git stash show -p stash@{0}                     # Full diff of a stash
git stash apply                                 # Apply latest stash (keep it)
git stash apply stash@{2}                       # Apply a specific stash
git stash pop                                   # Apply latest stash and remove it
git stash drop stash@{0}                        # Delete a stash
git stash clear                                 # Delete all stashes
git stash branch <name>                         # Create a branch from a stash
```

---

## 10. Rebasing

```bash
git rebase <branch>                             # Rebase current branch onto <branch>
git rebase main                                 # Rebase onto main
git rebase -i HEAD~3                            # Interactive rebase last 3 commits
git rebase -i <commit>                          # Interactive rebase from a commit
git rebase --onto <new-base> <old-base> <branch>  # Transplant commits
git rebase --continue                           # Continue after resolving conflicts
git rebase --skip                               # Skip the current commit
git rebase --abort                              # Abort the rebase
git pull --rebase                               # Pull using rebase
```

**Interactive rebase commands:**

| Command  | Meaning                                  |
| -------- | ---------------------------------------- |
| `pick`   | Use the commit as is                     |
| `reword` | Use the commit but edit the message      |
| `edit`   | Pause to amend the commit                |
| `squash` | Combine with previous commit, edit msg   |
| `fixup`  | Combine with previous commit, drop msg   |
| `drop`   | Remove the commit                        |

> ⚠️ Never rebase commits that have already been pushed to a shared branch.

---

## 11. Tagging

```bash
git tag                                         # List tags
git tag -l "v1.*"                               # List tags matching a pattern
git tag <name>                                  # Create a lightweight tag
git tag -a v1.0 -m "Release 1.0"                # Create an annotated tag
git tag -a v1.0 <commit>                        # Tag a specific commit
git show v1.0                                   # Show tag details
git push origin v1.0                            # Push a tag
git push origin --tags                          # Push all tags
git tag -d v1.0                                 # Delete a local tag
git push origin --delete v1.0                   # Delete a remote tag
git checkout v1.0                               # Check out a tag
```

---

## 12. Cherry-pick

```bash
git cherry-pick <commit>                        # Apply a commit to current branch
git cherry-pick <c1> <c2>                       # Apply multiple commits
git cherry-pick <c1>..<c3>                      # Apply a range
git cherry-pick -n <commit>                     # Apply without committing
git cherry-pick --continue                      # Continue after resolving conflicts
git cherry-pick --abort                         # Abort cherry-pick
```

---

## 13. Submodules

```bash
git submodule add <url> <path>                  # Add a submodule
git submodule init                              # Initialize submodules
git submodule update                            # Update submodules
git submodule update --init --recursive         # Init + update all (nested too)
git submodule update --remote                   # Pull latest from submodule remotes
git submodule status                            # Show submodule status
git submodule foreach 'git pull origin main'    # Run a command in every submodule
```

---

## 14. Worktrees

```bash
git worktree add ../<folder> <branch>           # Check out a branch in a new folder
git worktree add -b <new-branch> ../<folder>    # Create a new branch in a new folder
git worktree list                               # List worktrees
git worktree remove ../<folder>                 # Remove a worktree
git worktree prune                              # Clean up stale worktree info
```

---

## 15. Debugging

```bash
git blame <file>                                # Who changed each line
git blame -L 10,20 <file>                       # Blame specific lines
git grep "text"                                 # Search tracked files
git grep -n "text"                              # Search with line numbers

git bisect start                                # Start binary search for a bug
git bisect bad                                  # Mark current commit as bad
git bisect good <commit>                        # Mark a known good commit
git bisect good / git bisect bad                # Keep marking until the culprit is found
git bisect reset                                # End bisect session
git bisect run <script>                         # Automate bisect with a test script
```

---

## 16. Cleaning & Maintenance

```bash
git clean -n                                    # Dry run: show files that would be removed
git clean -f                                    # Remove untracked files
git clean -fd                                   # Remove untracked files and folders
git clean -fdx                                  # Also remove ignored files

git gc                                          # Garbage collect / optimize repo
git fsck                                        # Check repository integrity
git prune                                       # Remove unreachable objects
git count-objects -vH                           # Show repo size info
git remote prune origin                         # Remove stale remote branches
```

### .gitignore

```bash
echo "node_modules/" >> .gitignore              # Ignore a folder
git rm -r --cached .                            # Re-apply .gitignore to tracked files
git add . && git commit -m "Apply .gitignore"
git check-ignore -v <file>                      # Why is a file ignored?
git update-index --assume-unchanged <file>      # Temporarily ignore changes to a tracked file
git update-index --no-assume-unchanged <file>   # Undo the above
```

---

## 17. Aliases & Useful Shortcuts

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.unstage "reset HEAD --"
git config --global alias.last "log -1 HEAD"
```

Usage: `git st`, `git co main`, `git lg`

---

## 18. Common Workflows

### First-time project setup & push

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <url>
git push -u origin main
```

### Daily workflow

```bash
git pull                        # Get latest changes
git switch -c feature/my-work   # Create a feature branch
# ...make changes...
git add .
git commit -m "Add my feature"
git push -u origin feature/my-work
```

### Update a feature branch with latest main

```bash
git fetch origin
git rebase origin/main          # or: git merge origin/main
```

### Squash the last 3 commits into one

```bash
git reset --soft HEAD~3
git commit -m "Combined commit message"
```

### Undo the last commit but keep the changes

```bash
git reset --soft HEAD~1
```

### Change the last commit message

```bash
git commit --amend -m "New message"
```

### Fix a wrong commit on the wrong branch

```bash
git switch correct-branch
git cherry-pick <commit>
git switch wrong-branch
git reset --hard HEAD~1
```

### Sync a fork with the upstream repo

```bash
git remote add upstream <original-repo-url>
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```

### Rename a branch locally and on remote

```bash
git branch -m old-name new-name
git push origin -u new-name
git push origin --delete old-name
```

### Delete all merged local branches (except main)

```bash
git branch --merged | grep -v "main" | xargs git branch -d
```

---

## Quick Reference Table

| Task                        | Command                              |
| --------------------------- | ------------------------------------ |
| Start a repo                | `git init`                           |
| Copy a repo                 | `git clone <url>`                    |
| Check status                | `git status`                         |
| Stage everything            | `git add .`                          |
| Commit                      | `git commit -m "msg"`                |
| Push                        | `git push`                           |
| Pull                        | `git pull`                           |
| Fetch only                  | `git fetch`                          |
| New branch                  | `git switch -c <name>`               |
| Switch branch               | `git switch <name>`                  |
| Merge                       | `git merge <branch>`                 |
| Rebase                      | `git rebase <branch>`                |
| Stash                       | `git stash`                          |
| Undo last commit (keep)     | `git reset --soft HEAD~1`            |
| Undo last commit (discard)  | `git reset --hard HEAD~1`            |
| Safe undo (shared branch)   | `git revert <commit>`                |
| View history                | `git log --oneline --graph`          |
| Recover lost work           | `git reflog`                         |

---

*Tip: Run `git help <command>` for full details on any command.*
