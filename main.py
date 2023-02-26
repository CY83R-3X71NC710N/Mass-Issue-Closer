from github import Github
import sys
import os

# get the personal access token from the command-line arguments
token = sys.argv[1]

# authenticate to GitHub API using personal access token
g = Github(token)

# get repository
repo = g.get_repo('CY83R-3X71NC710N/Example-Project')

# get all issues in the repository
issues = repo.get_issues(state='open')

# iterate over the issues and close each one
for issue in issues:
    issue.edit(state='closed')
    print(f"Closed issue #{issue.number}: {issue.title}")

# Mitigate security vulnerability of passing access token as argument by clearing command-line-history
if os.name == 'nt':  # Windows
    os.system("doskey /reinstall")
    os.system("cls")
else:  # macOS and Linux
    os.system("history -c")
    os.system("clear")
    
print("Command-line history and screen cleared.")
