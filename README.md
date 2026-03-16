# PyCodeBot 🤖

PyCodeBot is a simple Python-based **code management bot** for GitHub repositories.
It helps automate common development tasks such as reviewing pull requests, enforcing coding standards, and improving repository quality.

---

## Features

* 🔍 Automatically reviews open pull requests
* 💬 Posts helpful comments on pull requests
* 🧹 Encourages consistent code formatting
* ⚠️ Reminds contributors to run lint checks
* 🚀 Easy to extend with more automation features

---

## Requirements

* Python 3.8+
* A GitHub Personal Access Token
* Python libraries:

  * PyGithub

Install dependencies:

```bash
pip install PyGithub
```

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Create a GitHub Token

Go to GitHub:

**Settings → Developer Settings → Personal Access Tokens**

Create a token with permission to access repositories.

---

### 3. Set Environment Variable

Linux / Mac:

```bash
export GITHUB_TOKEN=your_token_here
```

Windows:

```bash
set GITHUB_TOKEN=your_token_here
```

---

### 4. Configure the Bot

Open `codebot.py` and change the repository name:

```python
REPO_NAME = "your-username/your-repository"
```

---

## Running the Bot

Run the bot with:

```bash
python codebot.py
```

The bot will:

1. Connect to your GitHub repository
2. Find open pull requests
3. Leave a review comment automatically

---

## Project Structure

```
pycodebot/
│
├── codebot.py
├── requirements.txt
└── README.md
```

---

## Example Bot Comment

```
🤖 PyCodeBot Review:

- Please ensure code follows formatting guidelines.
- Run lint checks before committing.
- Make sure tests pass.
```

---

## Future Improvements

* Add automatic code formatting
* Integrate lint checking
* Auto-fix style issues
* Run tests on pull requests
* AI-powered code review

---

## License

This project is open source and available under the MIT License.
