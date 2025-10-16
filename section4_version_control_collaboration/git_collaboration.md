# Git Collaboration

## How I Collaborate Using Git

### Common Commands
- `git clone <repo_url>` → Copy repository to local machine.
- `git branch feature-login` → Create new feature branch.
- `git add . && git commit -m "Added feature"` → Save changes.
- `git push origin feature-login` → Push branch to remote repo.

### Typical Workflow
1. Clone repo from GitHub.
2. Create a new branch for a task.
3. Commit changes frequently with clear messages.
4. Push branch and create a Pull Request (PR) for review.

### Common Problem
**Merge Conflict:** Two devs edit the same file lines.
- **Solution:** Use `git pull --rebase origin main`, manually fix conflicts, then `git add` and `git commit` again.