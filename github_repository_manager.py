```python
import os
from github import Github

# Shared dependencies
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = "your-repo-name"
MAIN_BRANCH_NAME = "main"
DOCKER_COMPOSE_FILE_NAME = "docker-compose.yml"
CRITICAL_FILES_LIST = ["file1", "file2"]
ESSENTIAL_FILES_LIST = ["file3", "file4"]

# GitHub API initialization
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

def review_branches():
    branches = repo.get_branches()
    for branch in branches:
        print(branch.name)

def ensure_file_consistency():
    branches = repo.get_branches()
    for branch in branches:
        branch_files = get_files(branch)
        if set(branch_files) != set(MAIN_BRANCH_FILES):
            print("Inconsistent files in branch", branch.name)

def get_files(branch):
    contents = repo.get_contents("", ref=branch.name)
    return [content.path for content in contents]

def verify_essential_files():
    main_branch_files = get_files(MAIN_BRANCH_NAME)
    for file in ESSENTIAL_FILES_LIST:
        if file not in main_branch_files:
            print("Essential file", file, "is missing in main branch")

def move_missing_files():
    main_branch_files = get_files(MAIN_BRANCH_NAME)
    for file in ESSENTIAL_FILES_LIST:
        if file not in main_branch_files:
            move_file_to_main(file)

def move_file_to_main(file):
    branches = repo.get_branches()
    for branch in branches:
        branch_files = get_files(branch)
        if file in branch_files:
            file_content = repo.get_contents(file, ref=branch.name)
            repo.create_file(file, "move file to main", file_content.decoded_content)
            print("Moved file", file, "to main branch from", branch.name)
            break

def remove_critical_files():
    branches = repo.get_branches()
    for branch in branches:
        if branch.name != MAIN_BRANCH_NAME:
            branch_files = get_files(branch)
            for file in CRITICAL_FILES_LIST:
                if file in branch_files:
                    repo.delete_file(file, "remove critical file", branch.commit.sha, branch=branch.name)
                    print("Removed critical file", file, "from branch", branch.name)

if __name__ == "__main__":
    review_branches()
    ensure_file_consistency()
    verify_essential_files()
    move_missing_files()
    remove_critical_files()
```