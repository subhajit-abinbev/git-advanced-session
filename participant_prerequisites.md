# Git Advanced Session - Participant Prerequisites & Setup

## 📋 Pre-Session Requirements

Please complete ALL steps below **BEFORE** the session starts. This ensures we can focus on learning Git concepts rather than troubleshooting setup issues.

---

## 🛠️ Software Installation Requirements

### 1. Git (Latest Version)

**Required:** Git 2.30 or later

#### Windows:

- Download from: https://git-scm.com/download/win
- Use Git Bash (included) for commands
- ✅ Verify: `git --version`

#### Mac:

```bash
# Using Homebrew (recommended)
brew install git

# Or download from: https://git-scm.com/download/mac
```

- ✅ Verify: `git --version`

#### Linux:

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install git

# CentOS/RHEL
sudo yum install git
```

- ✅ Verify: `git --version`

### 2. Python 3.8 or Higher

**Required:** Python 3.8+

#### Check Current Version:

```bash
python --version
# OR
python3 --version
```

#### Install if Needed:

- **Windows:** https://python.org/downloads/
- **Mac:** `brew install python3`
- **Linux:** `sudo apt install python3 python3-pip`

### 3. Code Editor

**Recommended:** Visual Studio Code

- Download: https://code.visualstudio.com/
- **Alternative options:** PyCharm, Sublime Text, Vim, etc.

### 4. GitHub Account

- Create free account at: https://github.com
- We'll use this for pull request demonstrations

---

## 🚀 Environment Setup Instructions

### Step 1: Clone the Repository

```bash
# Replace <repository-url> with actual URL provided by instructor
git clone <repository-url>
cd git-advanced-session
```

### Step 2: Automated Setup (Recommended)

```bash
# Make setup script executable
chmod +x scripts/setup_environment.sh

# Run complete setup
./scripts/setup_environment.sh
```

**What this does:**

- ✅ Creates Python virtual environment
- ✅ Installs all dependencies
- ✅ Sets up pre-commit hooks
- ✅ Runs initial tests
- ✅ Creates baseline configurations

### Step 3: Manual Setup (If Automated Fails)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (Git Bash):
source venv/Scripts/activate
# On Mac/Linux:
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

# Initialize secrets baseline
detect-secrets scan --baseline .secrets.baseline

# Verify setup
pytest
pre-commit run --all-files
```

### Step 4: Verify Installation

Run these commands to ensure everything works:

```bash
# Check Python packages
python -c "import pandas, numpy, pytest; print('✅ All packages installed')"

# Check pre-commit
pre-commit --version

# Check tests pass
pytest

# Check Git configuration
git config --list
```

**Expected Output:**

- ✅ All tests should pass
- ✅ Pre-commit hooks should install successfully
- ✅ No import errors for Python packages

---

## ⚙️ Git Configuration Setup

### Essential Git Configuration

```bash
# Set your identity (use your real name and email)
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Enable colored output
git config --global color.ui auto

# Set default editor (optional)
git config --global core.editor "code --wait"  # VS Code
# OR
git config --global core.editor "vim"          # Vim
```

### GitHub Authentication Setup

You'll need this for pull request exercises:

#### Option 1: Personal Access Token (Recommended)

1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token with `repo` permissions
3. Save the token securely
4. Use token as password when prompted

#### Option 2: SSH Keys

```bash
# Generate SSH key
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# Add to GitHub: Settings → SSH and GPG keys
```

---

## 📱 Session Day Setup

### 15 Minutes Before Session Starts:

1. **Update Repository:**

```bash
cd git-advanced-session
git pull origin main
```

2. **Activate Environment:**

```bash
source venv/bin/activate  # Mac/Linux
# OR
source venv/Scripts/activate  # Windows
```

3. **Verify Everything Still Works:**

```bash
pytest
pre-commit run --all-files
```

4. **Open Your Code Editor:**

```bash
code .  # VS Code
# OR open the project folder in your preferred editor
```

---

## 🎯 Demo Scenarios Preparation

**DO NOT RUN THESE YET** - We'll do this together during the session:

These scripts will create demo files during the session:

- `python scripts/demo_scenarios.py` - Basic scenarios
- `python scripts/create_merge_conflicts.py` - Merge conflicts
- `python scripts/create_commit_history.py` - Messy history
- `python scripts/revert_scenarios.py` - Problematic commits

---

## 📚 Pre-Session Reading (Optional)

If you want to prepare, review these concepts:

- Git basics: add, commit, push, pull
- Branching and merging fundamentals
- What are merge conflicts?
- Basic command line usage

**Useful Resources:**

- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Pro Git Book](https://git-scm.com/book) (Chapters 1-3)

---

## ❓ Troubleshooting Common Issues

### Issue: "command not found: git"

**Solution:** Git not installed or not in PATH

- Reinstall Git ensuring "Add to PATH" is selected
- Restart terminal/command prompt

### Issue: "python: command not found"

**Solution:** Try `python3` instead, or Python not in PATH

- On Windows: Use `py` command
- Ensure Python added to PATH during installation

### Issue: Permission denied (Windows)

**Solution:** Run Git Bash as Administrator

- Right-click Git Bash → "Run as Administrator"

### Issue: Pre-commit hooks fail

**Solution:**

```bash
# Clear and reinstall
pre-commit clean
pre-commit install
pre-commit run --all-files
```

### Issue: Import errors

**Solution:** Ensure virtual environment is activated

```bash
# Check which Python you're using
which python
# Should show path to venv/bin/python or venv/Scripts/python
```

---

## ✅ Pre-Session Checklist

Before the session starts, ensure you can check ALL these boxes:

- [ ] Git version 2.30+ installed and working
- [ ] Python 3.8+ installed and working
- [ ] Code editor installed and working
- [ ] GitHub account created
- [ ] Repository cloned successfully
- [ ] Virtual environment created and activated
- [ ] All Python packages installed (`pip list` shows pandas, pytest, etc.)
- [ ] Pre-commit hooks installed (`pre-commit --version` works)
- [ ] Tests pass (`pytest` runs without errors)
- [ ] Git identity configured (`git config --list` shows name/email)
- [ ] Can create and commit files in the repository
- [ ] No firewall/network issues accessing GitHub

---

## 🆘 Need Help?

### During Setup:

- Post questions in the session chat/forum
- Email instructor with setup issues
- Join the pre-session setup call (if available)

### Session Day:

- Raise your hand for immediate help
- Use chat for quick questions
- Don't hesitate to ask - we're here to help!

---

## 📧 Contact Information

**Instructor:** [Your Name]
**Email:** [your.email@example.com]
**Session Chat:** [Link to chat platform]

---

## 🎉 You're Ready!

Once you've completed this setup, you'll be ready to dive deep into advanced Git workflows. We'll cover real-world scenarios that every developer encounters, and you'll have hands-on practice with each concept.

**See you in the session!** 🚀

---

_Last updated: [Current Date]_
_Session duration: 2.5 hours_
_Format: Interactive hands-on workshop_
