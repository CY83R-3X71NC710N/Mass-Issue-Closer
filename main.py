from github import Github
import sys
import os
import platform
import subprocess

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

# check the OS platform
os_name = platform.system()

# clear command history based on the OS
if os_name == "Windows":
    subprocess.run(["doskey", "/reinstall", "/listsize=0"], shell=True)
elif os_name == "Linux" or os_name == "Darwin":
    subprocess.run(["history", "-c"], shell=True)
else:
    print("Unsupported operating system.")
    exit()

# clear the screen
subprocess.run("cls" if os_name == "Windows" else "clear", shell=True)
    
print("Command-line history and screen cleared.")
