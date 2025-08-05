# Git Advanced Session - Complete Presenter Flow Guide

## 🎬 Session Overview (2.5 Hours Total)

**Format:** Interactive hands-on workshop
**Style:** Demo-first, then participants follow
**Approach:** Problem → Solution → Practice

---

## 🚀 Pre-Session Setup (15 minutes before start)

### Presenter Preparation Checklist:

- [ ] Test screen sharing and audio
- [ ] Have repository cloned and ready
- [ ] Terminal/command prompt ready
- [ ] Code editor open (VS Code recommended)
- [ ] Backup slides ready (if network fails)
- [ ] Session recording started (if recording)

### Quick Environment Check:

```bash
cd git-advanced-session
git status
source venv/bin/activate
pytest --version
pre-commit --version
```

---

## 📋 PHASE 1: Welcome & Environment Verification (15 min)

### Opening (5 min)

**SAY:**

> "Welcome to Git Advanced Session! Today we'll learn advanced Git workflows through hands-on practice. We'll simulate real-world scenarios you encounter daily as developers."

**SHOW AGENDA:**

```
1. Pre-commit best practices (45 min)
2. Post-commit operations (75 min)
3. Team workflows & best practices (20 min)
4. Q&A (15 min)
```

### Participant Setup Verification (10 min)

**SAY:**

> "Let's verify everyone's setup. Please run these commands and raise your hand if anything fails:"

**GUIDE PARTICIPANTS:**

```bash
# Everyone run these:
cd git-advanced-session
git status
source venv/bin/activate    # or venv/Scripts/activate on Windows
pytest --version
pre-commit --version
```

**TROUBLESHOOT:** Help anyone with issues. Have backup cloud environments ready.

---

## 📋 PHASE 2: Pre-Commit Best Practices (45 min)

### 2.1 Introduction to Pre-Commit (5 min)

**SAY:**

> "Pre-commit hooks are your first line of defense against bad code entering your repository. Let's see what happens when we try to commit problematic code."

**EXPLAIN THE PHILOSOPHY:**

- Catch issues before they become problems
- Enforce team standards automatically
- Save time in code reviews

### 2.2 .gitignore Deep Dive (10 min)

**DEMO:** Show the comprehensive .gitignore file

**SAY:**

> "Let's examine our .gitignore file and understand what each section does."

**SHOW IN EDITOR:**

```bash
code .gitignore
```

**EXPLAIN SECTIONS:**

- Python-specific ignores
- IDE files
- OS files
- Secrets and sensitive data
- Large files
- Build artifacts

**INTERACTIVE MOMENT:**
**SAY:**

> "What files do you think should NEVER be committed in your projects?"

_Take 2-3 answers from participants_

### 2.3 Creating Problematic Files Demo (15 min)

**SAY:**

> "Now let's create some files that demonstrate why we need pre-commit hooks. Everyone follow along:"

**STEP 1: Create Demo Files**

```bash
# Everyone run this:
python scripts/demo_scenarios.py
```

**EXPLAIN WHAT WAS CREATED:**

- Large file (15MB) - will trigger size limit
- Secrets file - will trigger secret detection
- Sample data - for our demos

**STEP 2: Show Git Status**

```bash
git status
```

**POINT OUT:**

- Large file not shown (ignored by .gitignore)
- Secrets file not shown (ignored by .gitignore)
- Some files are tracked

### 2.4 Pre-Commit Hooks in Action (15 min)

**SAY:**

> "Now let's see what happens when we try to commit files that violate our rules."

**STEP 1: Try to Commit Secrets (Demo Failure)**

```bash
# Temporarily remove secrets.yaml from .gitignore
sed -i 's/secrets.yaml/#secrets.yaml/' .gitignore

# Try to add and commit
git add config/secrets.yaml
git commit -m "Add configuration (THIS SHOULD FAIL)"
```

**EXPECTED RESULT:** Detect-secrets hook should fail

**EXPLAIN:**

- Hook scanned for secrets
- Found API keys, passwords
- Prevented commit
- Show the detected secrets

**STEP 2: Try Large File (Demo Failure)**

```bash
# Temporarily remove large file from .gitignore
sed -i 's/data\/large_file.txt/#data\/large_file.txt/' .gitignore

# Try to add large file
git add data/large_file.txt
git commit -m "Add large dataset (THIS SHOULD FAIL)"
```

**EXPECTED RESULT:** File size hook should fail

**EXPLAIN:**

- Custom hook checked file sizes
- 15MB exceeds 10MB limit
- Show the error message

**STEP 3: Fix .gitignore**

```bash
# Restore .gitignore
git checkout -- .gitignore
```

**STEP 4: Create Jupyter Notebook with Outputs**

```bash
# Create a notebook with outputs
jupyter lab notebooks/data_analysis.ipynb
# Add some code and run cells to create outputs
# Save and exit
```

**STEP 5: Try to Commit Notebook**

```bash
git add notebooks/data_analysis.ipynb
git commit -m "Add data analysis notebook"
```

**EXPECTED RESULT:** nbstripout should clean the outputs

**EXPLAIN:**

- Notebook outputs removed automatically
- Only code and markdown preserved
- Show the cleaned notebook

---

## 📋 PHASE 3: Post-Commit Operations (75 min)

### 3.1 Creating Merge Conflicts (20 min)

**SAY:**

> "Now let's learn how to handle situations after committing. First, merge conflicts - the bane of every developer's existence!"

**STEP 1: Set Up Conflict Scenario**

```bash
# Everyone run:
python scripts/create_merge_conflicts.py
```

**EXPLAIN WHAT HAPPENED:**

- Created initial config file
- Made feature branch with changes
- Made different changes on main
- Now branches have conflicting changes

**STEP 2: Show the Branches**

```bash
git log --oneline --graph --all
```

**POINT OUT:**

- Divergent history
- Both branches modified same file
- Conflict is inevitable

**STEP 3: Attempt the Merge**

```bash
git merge feature/enhanced-config
```

**EXPECTED RESULT:** Merge conflict!

**STEP 4: Examine the Conflict**

```bash
git status
code config/app_config.py
```

**EXPLAIN CONFLICT MARKERS:**

```
<<<<<<< HEAD
version = "1.0.1"
author = "Main Team Lead"
=======
version = "1.1.0"
author = "Feature Team"
>>>>>>> feature/enhanced-config
```

**STEP 5: Resolve the Conflict**
**SAY:**

> "Let's resolve this by taking the best from both versions:"

**GUIDE PARTICIPANTS TO EDIT:**

```python
# Combined resolution
version = "1.1.0"  # Take higher version from feature
author = "Main Team Lead"  # Keep main author
description = "Advanced data processing application with ML and bug fixes"
# ... combine other conflicting sections
```

**STEP 6: Complete the Merge**

```bash
git add config/app_config.py
git commit -m "Resolve merge conflict: combine features and fixes"
```

**STEP 7: Verify Resolution**

```bash
git log --oneline --graph
```

### 3.2 Interactive Rebase Demo (20 min)

**SAY:**

> "Great! Now let's learn how to clean up messy commit history with interactive rebase."

**STEP 1: Create Messy History**

```bash
python scripts/create_commit_history.py
```

**STEP 2: Show Messy History**

```bash
git log --oneline
```

**POINT OUT:**

- Multiple tiny commits
- Typo fixes
- "Oops" commits
- Would be better as single clean commit

**STEP 3: Interactive Rebase**

```bash
git rebase -i HEAD~7
```

**GUIDE PARTICIPANTS THROUGH EDITOR:**

```
pick abc1234 Add basic calculator function
squash def5678 Fix typo in add function
squash ghi9012 Add subtract function
squash jkl3456 Oops forgot to save
squash mno7890 Actually add multiply
squash pqr1234 Fix formatting
squash stu5678 Add docstrings
```

**EXPLAIN REBASE OPTIONS:**

- `pick` - keep commit as-is
- `squash` - combine with previous commit
- `edit` - pause to modify commit
- `drop` - remove commit entirely

**STEP 4: Edit Commit Message**
**GUIDE PARTICIPANTS:**

```
Add complete calculator module with basic operations

- Implemented add, subtract, multiply functions
- Added comprehensive docstrings
- Cleaned up formatting and style
```

**STEP 5: Verify Clean History**

```bash
git log --oneline
```

**CELEBRATE:** One clean commit instead of seven messy ones!

### 3.3 Reverting Commits (20 min)

**SAY:**

> "Sometimes we need to undo commits safely. Let's learn the difference between revert and reset."

**STEP 1: Switch to Main Branch**

```bash
git checkout main
```

**STEP 2: Create Problematic Commits**

```bash
python scripts/revert_scenarios.py
```

**STEP 3: Show Tests Failing**

```bash
pytest src/test_calculator.py -v
```

**EXPECTED RESULT:** Tests should fail due to bugs introduced

**EXPLAIN THE PROBLEMS:**

- `add()` function has bug (adds 1 extra)
- `divide()` function has no zero-check
- `power()` function multiplies by 2

**STEP 4: Show Commit History**

```bash
git log --oneline -5
```

**STEP 5: Safe Revert (Don't Rewrite History)**

```bash
git revert HEAD~1..HEAD
```

**EXPLAIN WHY REVERT vs RESET:**

- `git revert` creates new commits that undo changes
- `git reset` rewrites history (dangerous if pushed)
- Always use revert for public commits

**STEP 6: Verify Fix**

```bash
pytest src/test_calculator.py -v
```

**CELEBRATE:** Tests pass again!

**STEP 7: Show History**

```bash
git log --oneline -8
```

**POINT OUT:**

- Original bad commits still exist
- New revert commits undo the damage
- History is preserved

### 3.4 Navigation and History (15 min)

**SAY:**

> "Let's explore some powerful commands for navigating Git history."

**DEMO COMMANDS:**

```bash
# Show detailed commit info
git show HEAD~2

# Show what changed in each commit
git log --stat --oneline -5

# Show visual branch history
git log --graph --oneline --all

# Find when a bug was introduced
git log -p src/calculator.py

# Show who changed each line
git blame src/calculator.py

# Find commits that mention specific words
git log --grep="calculator"

# Show commits that changed specific files
git log -- src/calculator.py
```

**INTERACTIVE EXERCISE:**
**SAY:**

> "Everyone try these commands and explore your repository history. Raise your hand if you find something interesting!"

---

## 📋 PHASE 4: Team Workflows & Best Practices (20 min)

### 4.1 Pull Request Workflow (10 min)

**SAY:**

> "Let's discuss how teams collaborate effectively with Git."

**SHOW FILES:**

```bash
code .github/pull_request_template.md
code .github/CODEOWNERS
```

**EXPLAIN PR PROCESS:**

1. Create feature branch
2. Make changes and commit
3. Push branch to GitHub
4. Create pull request
5. Code review process
6. Address feedback
7. Merge after approval

**DEMO GITHUB WORKFLOW:**

- Show creating PR on GitHub
- Show review process
- Show merge options (merge, squash, rebase)

### 4.2 Best Practices Discussion (10 min)

**COVER KEY POINTS:**

**Commit Messages:**

```
feat(calculator): add power function with error handling

fix(data-processor): handle missing CSV columns gracefully

docs(readme): update installation instructions
```

**Branch Naming:**

- `feature/add-user-authentication`
- `bugfix/fix-login-validation`
- `hotfix/security-patch`

**When to Use Each Merge Strategy:**

- **Merge commit:** Feature branches with meaningful history
- **Squash and merge:** Small features, cleanup commits
- **Rebase and merge:** Linear history preference

**Code Review Guidelines:**

- Review for functionality, not style (hooks handle style)
- Check test coverage
- Look for security issues
- Verify documentation updates

---

## 📋 PHASE 5: Q&A and Wrap-up (15 min)

### Advanced Topics Teaser (5 min)

**MENTION BUT DON'T DEMO:**

- Git hooks (server-side)
- Git LFS for large files
- Git submodules
- Advanced rebase strategies
- Cherry-picking commits

### Q&A Session (10 min)

**COMMON QUESTIONS TO EXPECT:**

- "What if I accidentally push to main?"
- "How do I undo a merge?"
- "When should I use rebase vs merge?"
- "How do I handle binary files?"
- "What's the difference between fetch and pull?"

**HAVE ANSWERS READY FOR:**

```bash
# Undo last commit (not pushed)
git reset --soft HEAD~1

# Undo merge
git reset --hard HEAD~1  # OR git revert -m 1 HEAD

# Emergency: force push after rebase (use carefully!)
git push --force-with-lease

# See what changed between commits
git diff HEAD~2..HEAD
```

---

## 🎯 Presenter Tips Throughout Session

### Keep Energy High:

- Celebrate when commands work: "Perfect!"
- Acknowledge when things break: "That's exactly what we wanted to see!"
- Use humor: "Git can be git-ty sometimes, but we'll master it!"

### Handle Questions:

- "Great question! Let me show you..."
- "I'll come back to that after this demo"
- "Anyone else have experience with this?"

### Manage Pace:

- Check frequently: "Everyone with me so far?"
- Wait for stragglers: "I'll give you 30 seconds to catch up"
- Have fast participants help slow ones

### Technical Issues:

- Have backup cloud environments ready
- Screen share with participants who need help
- Use breakout rooms for individual help if needed

### Key Phrases to Use:

- "Let's see what happens when..."
- "This is a common scenario where..."
- "In real projects, you'll encounter..."
- "The key takeaway here is..."

---

## 📱 Emergency Backup Plans

### If Demo Fails:

- Have screenshots ready
- Use pre-recorded GIFs
- Switch to different participant's screen
- Have a second repository ready

### If Participants Can't Follow:

- Pair them up
- Use cloud environments
- Screen share and guide individually
- Have them observe and try later

### If Time Runs Short:

- Skip advanced navigation commands
- Combine revert and rebase demos
- Make Q&A optional
- Send follow-up resources

---

## 📋 Post-Session Follow-up

### Immediately After:

- Share recording (if available)
- Send session materials
- Post in chat: "Great session everyone!"

### Within 24 Hours:

**Send Email:**

```
Subject: Git Advanced Session - Resources & Next Steps

Hi everyone!

Great session today! Here are the resources to continue learning:

📁 Repository: [URL] - Keep practicing with the demo scenarios
📚 Additional Resources: [List helpful links]
🎥 Recording: [Link if available]
📝 Feedback Form: [Survey link]

Next steps:
1. Practice the scenarios we covered
2. Try implementing pre-commit hooks in your projects
3. Use interactive rebase to clean up your commit history

Questions? Reply to this email!

Happy Git-ing!
[Your name]
```

**Remember: The goal is confident, practical Git usage in real projects!** 🚀
