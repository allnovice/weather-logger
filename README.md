![Cron Status](https://api.cron-job.org/jobs/6636020/d6e43d168f56a78d/status-7.svg)
![Weather Logger](https://github.com/allnovice/weather-logger/actions/workflows/weather.yml/badge.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/allnovice/weather-logger)
![Repo Size](https://img.shields.io/github/repo-size/allnovice/weather-logger)
![License](https://img.shields.io/github/license/allnovice/weather-logger)

[![View Dashboard](https://img.shields.io/badge/Dashboard-Streamlit-blue?logo=streamlit)](https://weather-logger-gahhfpxtukmpjjaha4qr7l.streamlit.app)

1. Project Overview
A short description of what your logger does (e.g., “Fetches Manila weather data every hour and stores it into a Neon DB.”).


2. Features

Automated weather fetch (via GitHub Actions or cron-job.org)

Stores temperature, humidity, condition

PostgreSQL backend (Neon DB)



3. Setup Instructions
Show how someone could fork your repo and set up their own:

Add OPENWEATHER_API_KEY secret

Add NEON_CONN secret

Enable workflow



4. Database Schema
Example table:

CREATE TABLE weather_logs (
    id SERIAL PRIMARY KEY,
    timestamp_local TIMESTAMP NOT NULL,
    temperature_c NUMERIC,
    humidity_percent NUMERIC,
    condition TEXT
);


5. Sample Query

SELECT * FROM weather_logs ORDER BY timestamp_local DESC LIMIT 10;


6. Future Improvements / TODOs

Add weather forecast

Grafana dashboard

Export to CSV
- Test auto release
- Test auto release
