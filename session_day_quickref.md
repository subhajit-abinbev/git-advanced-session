# Git Advanced Session - Quick Reference Card

## 🚀 Session Day Commands (Keep This Open!)

### Before We Start
```bash
# Navigate to project
cd git-advanced-session

# Activate environment
source venv/bin/activate          # Mac/Linux
source venv/Scripts/activate      # Windows Git Bash

# Verify setup
git status
pytest --version
pre-commit --version
```

---

## 📋 Commands We'll Use During Session

### Part 1: Pre-Commit Hooks Demo

```bash
# Create demo files (Instructor will guide)
python scripts/demo_scenarios.py

# Try to commit problematic files
git add .
git commit -m "Demo commit with issues"
# Watch pre-commit hooks prevent problems!

# Fix issues and try again
git add .
git commit -m "Clean commit after hooks"
```

### Part 2: Merge Conflicts Demo

```bash
# Create conflict scenario
python scripts/create_merge_conflicts.py

# Try to merge (will create conflicts)
git merge feature/enhanced-config

# View conflict
git status
cat config/app_config.py

# Resolve conflict
# Edit config/app_config.py in your editor
git add config/app_config.py
git commit -m "Resolve merge conflict"
```

### Part 3: Rebase Demo

```bash
# Create messy history
python scripts/create_commit_history.py

# View messy history
git log --oneline

# Interactive rebase to clean up
git rebase -i HEAD~7
# Follow instructor's guidance in the editor
```

### Part 4: Revert Demo

```bash
# Switch back to main
git checkout main

# Create problematic commits
python scripts/revert_scenarios.py

# See tests fail
pytest

# Safely revert
git revert HEAD~1..HEAD

# Verify tests pass
pytest
```

---

## 🔧 Useful Git Commands During Session

### Navigation & Information
```bash
git status                    # Current state
git log --oneline            # Commit history
git log --graph --oneline    # Visual history
git show HEAD                # Latest commit details
git diff                     # Unstaged changes
git diff --staged            # Staged changes
```

### Branch Operations
```bash
git branch                   # List branches
git branch -a               # List all branches
git checkout <branch>       # Switch branch
git checkout -b <branch>    # Create and switch
git merge <branch>          # Merge branch
```

### Troubleshooting
```bash
git reset --hard HEAD       # Discard all changes
git clean -fd               # Remove untracked files
git checkout -- <file>     # Discard file changes
git stash                   # Temporarily save changes
git stash pop               # Restore stashed changes
```

---

## 🛑 Emergency Commands (If You Get Lost)

### Reset to Clean State
```bash
# Nuclear option - start fresh
git reset --hard origin/main
git clean -fd
```

### If Merge Goes Wrong
```bash
git merge --abort           # Cancel merge
```

### If Rebase Goes Wrong
```bash
git rebase --abort          # Cancel rebase
```

---

## 💡 Editor Tips

### VS Code
- `Ctrl+Shift+G` - Git panel
- `Ctrl+Shift+P` → "Git: " for Git commands
- Click line numbers to see git blame

### Command Line Git
- `q` to exit git log/diff
- `Space` to scroll down in git log
- `Ctrl+C` to cancel current command

---

## 📁 Key Files to Watch

During the session, pay attention to these files:
- `.gitignore` - What gets ignored
- `.pre-commit-config.yaml` - Hook configuration
- `config/app_config.py` - Merge conflict demo
- `src/calculator.py` - Revert demo
- `data/large_file.txt` - File size demo
- `config/secrets.yaml` - Secrets detection demo

---

## 🎯 Session Agenda Tracker

### ✅ Part 1: Pre-Commit (45 min)
- [ ] .gitignore demonstration
- [ ] File size limit hook
- [ ] Secrets detection hook  
- [ ] Notebook output stripping
- [ ] Code formatting hooks
- [ ] Test integration

### ✅ Part 2: Post-Commit (75 min)
- [ ] Creating merge conflicts
- [ ] Resolving merge conflicts
- [ ] Interactive rebase
- [ ] Commit reverting
- [ ] History navigation
- [ ] Pull request workflow

### ✅ Part 3: Best Practices (20 min)
- [ ] Team workflow discussion
- [ ] Code review guidelines
- [ ] Branch naming conventions

---

## ❗ Important Notes

- **Don't panic** if commands fail - it's part of learning!
- **Ask questions** immediately if you're lost
- **Follow along** but don't run ahead
- **Take notes** on commands that are new to you
- **Practice** the concepts after the session

---

## 📞 Session Support

- **Raise hand** for immediate help
- **Use chat** for quick questions
- **Stay muted** unless asking questions
- **Share screen** if you need debugging help

**Remember: Everyone learns at different speeds - we'll wait for everyone!** 🤝