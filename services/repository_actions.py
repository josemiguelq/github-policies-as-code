import requests
import os
import json

owner = os.environ['GITHUB_OWNER']
url = f'https://api.github.com/repos/{owner}/'

def update_repo(repo, settings):
    headers = {'Authorization': 'Bearer ' + os.environ['GITHUB_TOKEN'], 'Accept': 'application/vnd.github+json'}
    x = requests.patch(url+repo, headers=headers, data=json.dumps(settings))
    print(x.text)
