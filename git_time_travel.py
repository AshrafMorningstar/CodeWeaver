
import os
import subprocess
import datetime
import random
import shutil

# Config
REPO_DIR = os.getcwd() # Assumes running from inside the bot folder
START_DATE = datetime.date(2024, 1, 1)
END_DATE = datetime.date.today()
FILES_DIR = "generated_code_files"

def run_git(args, env=None):
    subprocess.run(["git"] + args, cwd=REPO_DIR, env=env, check=False) # check=False to avoid crashing on init errors

def init_repo():
    if not os.path.exists(os.path.join(REPO_DIR, ".git")):
        print("Initializing Git Repository...")
        run_git(["init"])
        run_git(["branch", "-M", "main"])
    else:
        print("Git repository already exists.")

def get_all_files():
    file_list = []
    for root, dirs, files in os.walk(os.path.join(REPO_DIR, FILES_DIR)):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def commit_file(filepath, date_obj):
    # Rel path for git add
    rel_path = os.path.relpath(filepath, REPO_DIR)
    
    # Git add
    run_git(["add", rel_path])
    
    # Environment for backdating
    env = os.environ.copy()
    
    # Morning or Afternoon random time
    hour = random.randint(9, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    
    dt_str = f"{date_obj.isoformat()} {hour}:{minute}:{second}"
    
    env["GIT_AUTHOR_DATE"] = dt_str
    env["GIT_COMMITTER_DATE"] = dt_str
    
    commit_msg = f"Add {os.path.basename(filepath)} implementation ({date_obj.year})"
    
    # Git commit
    # We use -m to pass message
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=REPO_DIR, env=env, check=False)
    print(f"Committed {rel_path} on {dt_str}")

def main():
    init_repo()
    
    # Add base files first on Day 1
    run_git(["add", "README.md", "LICENSE", "CONTRIBUTING.md", "omnicoder.py", "bot_config.py", "validator.py", "requirements.txt"])
    
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = "2024-01-01 12:00:00"
    env["GIT_COMMITTER_DATE"] = "2024-01-01 12:00:00"
    subprocess.run(["git", "commit", "-m", "Initial commit: Core bot architecture"], cwd=REPO_DIR, env=env)
    
    # Now spread the 300 files over the duration
    all_files = get_all_files()
    total_files = len(all_files)
    
    if total_files == 0:
        print("No files found in generated_code_files to backdate!")
        return

    days_diff = (END_DATE - START_DATE).days
    if days_diff <= 0:
        days_diff = 1
        
    print(f"Spreading {total_files} commits over {days_diff} days...")
    
    # Shuffle files to make it look organic
    random.shuffle(all_files)
    
    current_file_idx = 0
    current_date = START_DATE
    
    while current_file_idx < total_files:
        # Pacing: How many files today? Random between 0 and 3
        # Ensure we don't run out of time or files improperly, but for 300 files over 365 days, avg is < 1 per day.
        # So we might skip some days.
        
        if current_date > END_DATE:
            current_date = END_DATE # Dump remaining on last day or stop
        
        # Chance to skip a day (weekend realism etc)
        if random.random() > 0.7:
            current_date += datetime.timedelta(days=1)
            continue
            
        files_today = random.randint(1, 3)
        
        for _ in range(files_today):
            if current_file_idx >= total_files:
                break
            
            commit_file(all_files[current_file_idx], current_date)
            current_file_idx += 1
            
        current_date += datetime.timedelta(days=1)

    print("Backdating Complete!")
    print("Run 'git log' to see the timeline.")
    print("Now create a repo on GitHub, add remote, and push: 'git push -u origin main --force'")

if __name__ == "__main__":
    main()
