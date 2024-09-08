```python
import os
from github import Github

# Shared dependencies
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = "your-repo-name"
MAIN_BRANCH_NAME = "main"
CRITICAL_FILES_LIST = ["file1", "file2"]

# Initialize GitHub API
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

def push_changes():
    try:
        repo.git.push()
        print(push_success)
    except Exception as e:
        print(push_error, str(e))

def merge_branches():
    try:
        repo.git.merge(MAIN_BRANCH_NAME)
        print(merge_success)
    except Exception as e:
        print(merge_error, str(e))

def remove_critical_files():
    for file in CRITICAL_FILES_LIST:
        try:
            repo.git.rm(file)
        except Exception as e:
            print(file_not_found_error, str(e))

def mark_main_branch():
    try:
        repo.create_git_ref(ref=f"refs/heads/{MAIN_BRANCH_NAME}", sha="new-commit-sha")
        print(branch_review_success)
    except Exception as e:
        print(branch_not_found_error, str(e))

if __name__ == "__main__":
    remove_critical_files()
    push_changes()
    merge_branches()
    mark_main_branch()
```