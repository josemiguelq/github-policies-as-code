from services.file_handler import *
from services.repository_actions import *

repos = read_repos()

for repo in repos:
    print(repo)
    update_repo(repo['name'], repo['settings'])
