from github import Github
import os

# Get GitHub token from environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Repository name (example: username/repo)
REPO_NAME = "your-username/your-repository"

def review_pull_requests():
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)

    pulls = repo.get_pulls(state="open")

    for pr in pulls:
        print(f"Reviewing PR #{pr.number}: {pr.title}")

        pr.create_issue_comment(
            "🤖 PyCodeBot Review:\n"
            "- Please ensure code follows formatting guidelines.\n"
            "- Run lint checks before committing.\n"
            "- Make sure tests pass."
        )

if __name__ == "__main__":
    review_pull_requests()
from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "your-username/your-repository"

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

for pr in repo.get_pulls(state="open"):
    pr.create_issue_comment("🤖 PyCodeBot Review: Please follow coding guidelines.")
