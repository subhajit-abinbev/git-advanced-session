# Presenter's Quick Cheat Sheet 🎯

*Keep this open during the session for quick reference*

---

## ⏰ Timing Checkpoints

| Time | Phase | Key Command |
|------|-------|------------|
| 0:00 | Welcome & Setup | `git status; pytest --version` |
| 0:15 | .gitignore Demo | `code .gitignore` |
| 0:25 | Create Demo Files | `python scripts/demo_scenarios.py` |
| 0:40 | Pre-commit Failures | `git add config/secrets.yaml; git commit` |
| 1:00 | Merge Conflicts | `python scripts/create_merge_conflicts.py` |
| 1:20 | Resolve Conflicts | `git merge feature/enhanced-config` |
| 1:40 | Interactive Rebase | `python scripts/create_commit_history.py` |
| 2:00 | Revert Demo | `python scripts/revert_scenarios.py` |
| 2:15 | History Navigation | `git log --graph --oneline --all` |
| 2:30 | Best Practices | Show PR templates |
| 2:45 | Q&A | Open floor |

---

## 🚨 Key Demo Commands (Copy-Paste Ready)

### Phase 1: Setup Verification
```bash
cd git-advanced-session
git status
source venv/bin/activate
pytest --version
pre-commit --version
```

### Phase 2: Pre-commit Demo
```bash
# Create demo files
python scripts/demo_scenarios.py

# Show .gitignore
code .gitignore

# Demo secret detection failure
sed -i 's/secrets.yaml/#secrets.yaml/' .gitignore
git add config/secrets.yaml
git commit -m "Add configuration (SHOULD FAIL)"
git checkout -- .gitignore

# Demo file size failure  
sed -i 's/data\/large_file.txt/#data\/large_file.txt/' .gitignore
git add data/large_file.txt
git commit -m "Add large dataset (SHOULD FAIL)"
git checkout -- .gitignore
```

### Phase 3: Merge Conflicts
```bash
# Create and resolve conflicts
python scripts/create_merge_conflicts.py
git log --oneline --graph --all
git merge feature/enhanced-config
git status
code config/app_config.py
# [Manual resolution in editor]
git add config/app_config.py
git commit -m "Resolve merge conflict"
```

### Phase 4: Interactive Rebase
```bash
# Create messy history
python scripts/create_commit_history.py
git log --oneline
git rebase -i HEAD~7
# [Guide through squashing]
git log --oneline
```

### Phase 5: Reverting
```bash
# Create and revert problems
git checkout main
python scripts/revert_scenarios.py
pytest src/test_calculator.py -v
git log --oneline -5
git revert HEAD~1..HEAD
pytest src/test_calculator.py -v
```

---

## 💬 Key Talking Points

### Opening Hook:
> "How many of you have ever been afraid to run `git` commands? Today we'll make Git your friend, not your enemy!"

### Pre-commit Philosophy:
> "Pre-commit hooks are like spell-check for code - catch mistakes before they become problems."

### Merge Conflicts:
> "Merge conflicts aren't failures - they're Git protecting you from losing work!"

### Rebase vs Reset:
> "Remember: Revert for public commits, Reset for private commits. When in doubt, Revert!"

### Best Practices:
> "Good Git habits scale - what works for personal projects works for teams of 100 developers."

---

## 🛑 Emergency Fixes

### If Demo Scripts Fail:
```bash
# Reset to clean state
git reset --hard HEAD
git clean -fd
git checkout main
```

### If Participants Get Lost:
```bash
# Have them reset to main
git stash
git checkout main
git reset --hard origin/main
```

### If Merge Goes Wrong:
```bash
git merge --abort
git reset --hard HEAD
```

### If Rebase Goes Wrong:
```bash
git rebase --abort
git reset --hard HEAD
```

---

## 📱 Troubleshooting Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| "Command not found" | Check PATH, try `python3` |
| "Permission denied" | Run as admin (Windows) |
| "No such file" | Check working directory with `pwd` |
| "Merge conflict" | Show conflict markers, guide resolution |
| "Pre-commit fails" | Run `pre-commit run --all-files` |
| "Tests fail" | Expected! Show why, then fix |

---

## 🎯 Participation Engagement

### Every 15 Minutes, Ask:
- "Everyone with me so far?"
- "Any questions before we move on?"
- "What do you think will happen if...?"

### Encourage Interaction:
- "Raise your hand if you've seen this before"
- "Anyone want to guess what this command does?"
- "Share in chat if you get a different result"

### Handle Questions:
- "Great question! Let me demo that..."
- "I'll circle back to that after this example"
- "Has anyone else encountered this?"

---

## 📊 Success Metrics

By end of session, participants should be able to:
- [ ] Explain what each pre-commit hook does
- [ ] Resolve a merge conflict confidently
- [ ] Use interactive rebase to clean history
- [ ] Safely revert problematic commits
- [ ] Navigate Git history effectively
- [ ] Understand team Git workflows

---

## 🆘 Backup Content (If Ahead of Schedule)

### Extra Demos:
```bash
# Git aliases
git config --global alias.lg "log --oneline --graph --all"
git config --global alias.st "status"

# Cherry picking
git cherry-pick <commit-hash>

# Stashing
git stash
git stash pop
git stash list

# Bisect for bug hunting
git bisect start
git bisect bad HEAD
git bisect good HEAD~10
```

### Advanced Topics to Mention:
- Git hooks (server-side)
- Git LFS for large files
- Submodules for dependencies
- GitHub Actions integration
- GitLab CI/CD pipelines

---

## 📋 Session Wrap-up Checklist

- [ ] Summarize key learnings
- [ ] Share additional resources
- [ ] Mention follow-up opportunities
- [ ] Ask for feedback
- [ ] Thank participants
- [ ] Stay online for individual questions

---

## 🎉 Closing Lines

> "Remember: Git is a powerful tool, but it's also forgiving. Every 'mistake' is a learning opportunity. Keep practicing, keep experimenting, and most importantly - keep committing to better code! Thank you all for a great session!"

**End with confidence and encouragement!** 🚀