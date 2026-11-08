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
