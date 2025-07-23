"""
/*
 * © 2022-2026 Ashraf Morningstar
 * GitHub: https://github.com/AshrafMorningstar
 *
 * This project is a personal recreation of existing projects, developed by Ashraf Morningstar 
 * for learning and skill development. Original project concepts remains the intellectual 
 * property of their respective creators.
 */
"""

import subprocess
import time
import os

def run_command(args):
    print(f"Running: {' '.join(args)}")
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        return False, result.stderr.strip()
    print(result.stdout.strip())
    return True, result.stdout.strip()

def main():
    print("--- Auto-Publishing to GitHub ---")
    
    # 1. Check Auth Status
    print("Checking GitHub auth status...")
    success, output = run_command(["gh", "auth", "status"])
    if "You are not logged into any GitHub hosts" in output or not success:
        print("❌ You are NOT logged into GitHub CLI.")
        print("Please run 'gh auth login' in your terminal and try again.")
        return

    # 2. Create Repository
    repo_name = "OmniCoder"
    print(f"Creating public repository '{repo_name}'...")
    
    # Try creating. If it fails because it exists, we catch it.
    # --source=. : Create from current directory
    # --remote=origin : Add remote named origin
    # --push : Push proper commits
    # --public : Make it public
    
    success, output = run_command(["gh", "repo", "create", repo_name, "--public", "--source=.", "--remote=origin", "--push"])
    
    if success:
        print(f"✅ Successfully created and pushed to https://github.com/{output.strip()}")
    else:
        if "already exists" in output:
            print("⚠️ Repository already exists. Attempting to push updates...")
            # If repo exists but we haven't set remote yet?
            run_command(["gh", "repo", "view", repo_name, "--web"]) 
            # Force push just in case
            run_command(["git", "push", "-u", "origin", "main", "--force"])
        else:
            print("❌ Failed to create repository.")

if __name__ == "__main__":
    main()
