# 🌦 Weather Logger

![Cron Status](https://api.cron-job.org/jobs/6636020/d6e43d168f56a78d/status-7.svg)
![Weather Logger](https://github.com/allnovice/weather-logger/actions/workflows/weather.yml/badge.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/allnovice/weather-logger)
![Repo Size](https://img.shields.io/github/repo-size/allnovice/weather-logger)
![License](https://img.shields.io/github/license/allnovice/weather-logger)
[![Release](https://img.shields.io/github/v/release/allnovice/weather-logger)](https://github.com/allnovice/weather-logger/releases/latest)
[![View Dashboard](https://img.shields.io/badge/Dashboard-Streamlit-blue?logo=streamlit)](https://weather-logger-gahhfpxtukmpjjaha4qr7l.streamlit.app)

---

### 🧠 Overview
Weather Logger automatically collects and visualizes hourly weather data from **OpenWeather API** and stores it in a **Neon PostgreSQL** database. It uses a simple linear model in Streamlit for local predictions and visualization. Automation runs via **GitHub Actions** and **cron-job.org** for continuous data logging.

---

### ⚙️ Features
- 🌦 Automated hourly weather fetch  
- 💾 Data storage in Neon PostgreSQL  
- 📊 Streamlit dashboard with historical graphs  
- 🤖 Auto changelog + semantic release integration  
- 🔮 Simple linear model for basic forecasting  

---

### 🚀 Setup Instructions (Termux / Debian)
**Install and clone**
pkg install proot-distro git python3 -y || sudo apt install git python3-venv -y  
proot-distro install debian && proot-distro login debian  
git clone https://github.com/allnovice/weather-logger.git  
cd weather-logger  
python3 -m venv venv && source venv/bin/activate  
pip install -r requirements.txt  

**Add API keys and database connection**
Create `.streamlit/secrets.toml` or use GitHub Secrets:

OPENWEATHER_API_KEY = "your_api_key"  
NEON_CONN = "your_neon_connection_string"  

---

### 🗄️ Database Schema
CREATE TABLE weather_logs (  
    id SERIAL PRIMARY KEY,  
    timestamp_local TIMESTAMP NOT NULL,  
    temperature_c NUMERIC,  
    humidity_percent NUMERIC,  
    condition TEXT  
);

---

### 🔍 Sample Query
SELECT * FROM weather_logs ORDER BY timestamp_local DESC LIMIT 10;

---

### 🧩 Future Improvements
- Add weather forecast API integration  
- Grafana dashboard support  
- Enhanced ML-based temperature forecasting  

---

### 🧾 Changelog Preview
🪄 *Auto-generated from latest GitHub Releases*

[![Latest Release](https://img.shields.io/github/v/release/allnovice/weather-logger?label=latest)](https://github.com/allnovice/weather-logger/releases/latest)

See the full changelog here: [CHANGELOG.md](CHANGELOG.md)
