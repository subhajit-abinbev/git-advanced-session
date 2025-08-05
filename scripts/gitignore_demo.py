#!/usr/bin/env python3
"""
Git Ignore Demonstration Script

This script demonstrates how .gitignore works by showing:
1. Files that are tracked by git
2. Files that are ignored by git
3. How to check if a file would be ignored

Usage: python scripts/gitignore_demo.py
"""

import os
import subprocess


def run_git_command(command):
    """Run a git command and return the output."""
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, cwd="."
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"


def main():
    print("=== Git Ignore Demonstration ===\n")

    # Check if we're in a git repository
    if not os.path.exists(".git"):
        print("Error: Not in a git repository!")
        return

    print("1. Current git status:")
    status = run_git_command("git status --porcelain")
    if status:
        print(status)
    else:
        print("Working directory is clean")
    print()

    print("2. Files being ignored by .gitignore:")
    ignored = run_git_command("git status --ignored --porcelain")
    ignored_files = [line[3:] for line in ignored.split("\n") if line.startswith("!!")]
    if ignored_files:
        for file in ignored_files:
            print(f"  - {file}")
    else:
        print("  No ignored files found")
    print()

    print("3. Checking specific files:")
    files_to_check = [".env", ".env.example", "README.md", "nonexistent.log"]

    for file in files_to_check:
        # Check if file exists
        exists = "✓" if os.path.exists(file) else "✗"

        # Check if file would be ignored
        check_ignore = run_git_command(f"git check-ignore {file}")
        ignored = "✓" if check_ignore else "✗"

        print(f"  {file:<20} | Exists: {exists} | Ignored: {ignored}")

    print("\n4. Contents of .gitignore (first 10 lines):")
    try:
        with open(".gitignore", "r") as f:
            lines = f.readlines()[:10]
            for i, line in enumerate(lines, 1):
                print(f"  {i:2}: {line.rstrip()}")
        if len(lines) == 10:
            with open(".gitignore", "r") as f:
                total_lines = sum(1 for _ in f)
            print(f"  ... and {total_lines - 10} more lines")
    except FileNotFoundError:
        print("  .gitignore file not found")

    print("\n=== Demo Complete ===")
    print("\nKey Points:")
    print("- .env files contain sensitive data and should NEVER be committed")
    print("- .env.example shows the structure but can be safely committed")
    print("- .gitignore prevents accidental commits of sensitive files")
    print("- Use 'git check-ignore <file>' to test if a file would be ignored")


if __name__ == "__main__":
    main()
