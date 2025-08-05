# Git Ignore Demonstration

This demonstration shows how `.gitignore` prevents sensitive files from being accidentally committed to version control.

## Files Created for This Demo

1. **`.env`** - Contains fake environment variables and API keys (NEVER commit this!)
2. **`.env.example`** - Template showing the structure without sensitive values (safe to commit)
3. **`.gitignore`** - Comprehensive ignore rules to prevent sensitive files from being tracked
4. **`scripts/gitignore_demo.py`** - Demonstration script showing how gitignore works

## Running the Demo

```bash
# Run the demonstration script
python scripts/gitignore_demo.py

# Check what files git sees
git status

# Check what files are being ignored
git status --ignored

# Test if a specific file would be ignored
git check-ignore .env
```

## Key Learning Points

### ✅ Best Practices
- Always add `.env` files to `.gitignore` BEFORE creating them
- Use `.env.example` to document required environment variables
- Review `.gitignore` patterns regularly
- Use `git check-ignore <file>` to test ignore rules

### ❌ What NOT to Do
- Never commit files containing real API keys, passwords, or secrets
- Don't ignore `.env.example` files (these should be committed)
- Avoid overly broad ignore patterns that might hide important files

### 🛡️ Security Benefits
- Prevents accidental exposure of sensitive data
- Protects API keys and database credentials
- Maintains clean repository history
- Reduces security vulnerabilities

## Demonstration Flow

1. **Show the .env file** - Contains fake but realistic sensitive data
2. **Run git status** - Notice .env doesn't appear (it's ignored!)
3. **Check ignored files** - Use `git status --ignored` to see what's being ignored
4. **Test ignore rules** - Use `git check-ignore` to test specific files
5. **Show .env.example** - Safe template that can be committed

## Common Scenarios to Demo

### Scenario 1: Accidental Commit Prevention
```bash
# Try to add .env (will be ignored)
git add .env
# Nothing happens - git ignores it!

# But .env.example can be added
git add .env.example
```

### Scenario 2: Testing Ignore Rules
```bash
# Test if files would be ignored
git check-ignore .env          # Returns: .env (ignored)
git check-ignore .env.example  # Returns nothing (not ignored)
git check-ignore secrets.yaml  # Returns: secrets.yaml (ignored)
```

### Scenario 3: Viewing All Ignored Files
```bash
# See all files being ignored
git status --ignored --porcelain | grep "^!!"
```

This demonstration effectively shows why `.gitignore` is crucial for maintaining security and keeping repositories clean!
