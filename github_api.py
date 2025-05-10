import requests
from utils.config import GITHUB_TOKEN

HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def fetch_contributors(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()

def fetch_commits(owner: str, repo: str, per_page: int = 100):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {"per_page": per_page}
    resp = requests.get(url, headers=HEADERS, params=params)
    resp.raise_for_status()
    return resp.json()

# Puedes añadir fetch_issues, fetch_prs, etc.
