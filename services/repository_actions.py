import requests
import json

url = 'https://api.github.com/repos'

def update_repo(token, owner, repo, settings):
    headers = {'Authorization': 'Bearer ' + token, 'Accept': 'application/vnd.github+json'}
    x = requests.patch(f'{url}/{owner}/{repo}', headers=headers, data=json.dumps(settings))
    print(x.text)
