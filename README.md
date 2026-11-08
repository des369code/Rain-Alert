# ☔ Automated Daily Rain Alert

An automated Python notification pipeline that queries the OpenWeather 5-Day / 3-Hour Forecast API and dispatches email notifications via SMTP whenever rain is forecasted within an upcoming window. Automated to run daily using GitHub Actions.

---

## 📌 Architecture Overview

1. **Weather Forecast API**: Sends coordinated requests (`lat`, `lon`, `cnt`) to the OpenWeatherMap 5-day/3-hour forecast API endpoint.
2. **Condition Parsing**: Iterates through forecast snapshots and monitors OpenWeather condition IDs below `700` (which indicate thunderstorm, drizzle, rain, or snow conditions).
3. **Email Dispatch**: Connects via TLS to Google's SMTP relay (`smtp.gmail.com:587`) and sends an automated notification if precipitation is detected.
4. **CI/CD Automation**: Scheduled using GitHub Actions via UTC cron scheduling (`0 3 * * *` for 11:00 AM MYT) and manual workflow dispatch triggers.
5. **Secret Security**: API credentials and application app passwords are kept out of source code and injected as process environment variables.

---

## 🛠️ Tech Stack & Requirements

* **Python 3.12+**
* **Dependencies**:
  * `requests` (API querying)
  * Standard library: `os`, `smtplib`, `email`

---

## ⚙️ Environment Variables

The application expects the following secrets provided as environment variables:

| Variable | Description |
| :--- | :--- |
| `api_key` | OpenWeatherMap API key |
| `MY_PASSWORD` | 16-character Google Account App Password |

---

## 🚀 Local Setup

### 1. Clone the repository
```bash
git clone [https://github.com/des369code/Rain-Alert.git](https://github.com/des369code/Rain-Alert.git)
cd Rain-Alert

2. Create and activate a virtual environment

python3 -m venv .venv
source .venv/bin/activate


3. Install dependencies

pip install -r requirements.txt


4. Run with environment variables

export api_key="your_openweathermap_api_key"
export MY_PASSWORD="your_google_app_password"
python3 main.py


🤖 GitHub Actions Workflow

The project includes automated workflows under .github/workflows/:

scheduled.yml: Runs automatically every morning at 11:00 AM MYT (03:00 UTC) via GitHub Actions schedule cron, or manually via workflow_dispatch.

test.yml: A dry-run workflow for validating syntax, repository structure, and secret configuration.

Configuring Secrets in GitHub

To allow GitHub Actions to inject variables:

Navigate to Settings → Secrets and variables → Actions.

Add the following repository secrets:

API_KEY: Your OpenWeather API key.

MY_EMAIL_PASSWORD: Your 16-character Google App Password.

📄 License

MIT
