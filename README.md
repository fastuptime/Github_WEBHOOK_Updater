# 🔁 GitHub Webhook Updater

A simple Python script to **bulk update webhook URLs** across all your **public GitHub repositories**.  
Useful when you're migrating services or endpoints and want to avoid manual updates.

---

## ✨ Features

- 🔍 Scans all your **public repositories**
- 🔗 Detects existing **webhooks with a specific URL**
- ♻️ Automatically **updates webhook URL** with a new one
- 🧾 Clean and informative logging for each update

---

## 📦 Requirements

- Python 3.6+
- `requests` library  
  Install via pip:
  ```bash pip install requests```

* A **GitHub Personal Access Token (PAT)** with at least:

  * `repo` scope (for public repos)
  * `admin:repo_hook` (for managing webhooks)

---

## ⚙️ Configuration

Open the `start.py` file and edit the following variables:

```python
GITHUB_USERNAME = 'your_github_username'
GITHUB_TOKEN = 'ghp_your_personal_access_token'

OLD_URL = 'https://old-webhook.com'
NEW_URL = 'https://new-webhook.com'
```

---

## 🚀 Usage

Simply run the script with Python:

```bash python start.py```

Sample output:

```
Toplam 5 repo bulundu.
[+] Güncelleniyor: example-repo - Hook ID: 123456
    ✅ Başarılı
```

---

## 📌 How It Works

1. Fetches all public repositories of the specified GitHub user.
2. For each repository:

   * Retrieves all configured webhooks.
   * Identifies webhooks where `config.url == OLD_URL`.
   * Updates the webhook's config with `NEW_URL` and retains other fields like `content_type`, `secret`, etc.

---

## ⚠️ Notes

* If the `secret` or `content_type` is missing in the existing webhook, GitHub API may return an error during update.
  You might need to manually inspect such webhooks.
* This script **only works on public repositories**. To support private repos, update the API URL to `?type=all` and ensure your token has full `repo` access.
* Hitting GitHub's [rate limits](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting) may cause failures if you have too many repositories.

---

## 🧩 TODO

* [ ] Add CLI arguments for easier automation
* [ ] Support webhook creation if none exists
* [ ] Allow updating webhooks across organizations

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo and submit improvements.

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Example Use Case

> You're moving your webhook handler from Heroku to Vercel, and need to update
> `https://old-heroku-webhook.com` ➜ `https://new-vercel-endpoint.com` across 50+ public repos?
> Run this script and you're done in seconds. 💥
