import requests

GITHUB_USERNAME = 'kullanici_adiniz'
GITHUB_TOKEN = 'ghp_xxx...'  # GitHub Personal Access Token https://github.com/settings/tokens
OLD_URL = 'https://eski-webhook.com'
NEW_URL = 'https://yeni-webhook.com'

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_all_repos():
    repos = []
    page = 1
    while True:
        url = f'https://api.github.com/users/{GITHUB_USERNAME}/repos?type=public&per_page=100&page={page}'
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            raise Exception(f"Repo alınamadı: {r.status_code}")
        data = r.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def update_hooks_for_repo(repo_name):
    hooks_url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/hooks'
    r = requests.get(hooks_url, headers=headers)
    hooks = r.json()

    for hook in hooks:
        if hook['config']['url'] == OLD_URL:
            hook_id = hook['id']
            update_url = f'{hooks_url}/{hook_id}'
            data = {
                'config': {
                    'url': NEW_URL,
                    'content_type': hook['config'].get('content_type', 'json'),
                    'secret': hook['config'].get('secret', ''),
                    'insecure_ssl': hook['config'].get('insecure_ssl', '0'),
                }
            }
            print(f"[+] Güncelleniyor: {repo_name} - Hook ID: {hook_id}")
            resp = requests.patch(update_url, headers=headers, json=data)
            if resp.status_code == 200:
                print(f"    ✅ Başarılı")
            else:
                print(f"    ❌ Hata: {resp.status_code} - {resp.text}")

def main():
    repos = get_all_repos()
    print(f"Toplam {len(repos)} repo bulundu.")
    for repo in repos:
        update_hooks_for_repo(repo['name'])

if __name__ == '__main__':
    main()
