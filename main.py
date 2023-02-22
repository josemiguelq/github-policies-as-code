from services.file_handler import *
from services.repository_actions import *
import os

# TODO config file
owner = os.environ['GITHUB_OWNER']
token = os.environ['GITHUB_TOKEN']

repos = read_repos()

for repo in repos:
    print(repo)
    update_repo(token, owner, repo['name'], repo['settings'])
