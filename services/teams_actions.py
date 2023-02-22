import requests
import os
import json

url = 'https://api.github.com/orgs'

def get_teams(token, owner):
    headers = {'Authorization': 'Bearer ' + os.environ['GITHUB_TOKEN'], 'Accept': 'application/vnd.github+json'}
    x = requests.get(f'{url}/{owner}/teams', headers=headers)
    print(x.text)

def get_team(token, owner, slug):
    headers = {'Authorization': 'Bearer ' + os.environ['GITHUB_TOKEN'], 'Accept': 'application/vnd.github+json'}
    x = requests.get(f'{url}/{owner}/{slug}', headers=headers)
    print(x.text)
