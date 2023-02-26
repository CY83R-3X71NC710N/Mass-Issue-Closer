from github import Github
import os

# authenticate to GitHub API using personal access token
g = Github(os.getenv('GITHUB_TOKEN'))

# get repository
repo = g.get_repo('owner/repo')

# get all issues in the repository
issues = repo.get_issues(state='open')

# iterate over the issues and close each one
for issue in issues:
    issue.edit(state='closed')
