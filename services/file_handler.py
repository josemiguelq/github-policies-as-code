from os import listdir
from os.path import isfile, join
import json

def read_repos():
    repositories_path = './resources/repositories'
    onlyfiles = [f for f in listdir(repositories_path) if isfile(join(repositories_path, f))]
    repositories = []
    # TODO async
    for file in onlyfiles:
        content = open(join(repositories_path, file))
        repo = file.replace('.json', '')
        settings = json.loads(content.read())
        repositories.append({"name" : repo, "settings": settings})
    return repositories

def read_teams():
    teams_path = './resources/teams'
    onlyfiles = [f for f in listdir(teams_path) if isfile(join(teams_path, f))]
    teams = []
    for file in onlyfiles:
        content = open(join(repositories_path, file))
        repo = file.replace('.json', '')
        settings = json.loads(content.read())
        teams.append({"name" : repo, "settings": settings})
    return repositories
