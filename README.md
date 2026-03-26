# 🛍️ End-to-End Fashion ETL Pipeline

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-compose-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Dicoding](https://img.shields.io/badge/Dicoding-5%20Stars%20(Advanced)-gold)](https://www.dicoding.com/)

A modular, production-ready Extract, Transform, Load (ETL) pipeline built with Python and containerized with Docker. This project received the highest rating (**5 Stars / Advanced Level**) as the Final Project for the "Belajar Fundamental Pemrosesan Data" course by Dicoding Indonesia.

## 🚀 Features & Architecture

- **Robust Extract:** Scrapes raw product data (Title, Price, Rating, Colors, Sizes) from a simulated fashion retailer using `BeautifulSoup4` and `Requests`.
- **Clean Transform:** Performs rigorous data cleansing, Regex manipulation, and currency conversion using `Pandas`.
- **Multi-Destination Load:** Simultaneously loads the cleaned data into three distinct repositories:
  - 📄 Local Flat File (`.csv`)
  - 🐘 Relational Database (`PostgreSQL` via SQLAlchemy)
  - ☁️ Cloud Spreadsheet (`Google Sheets API v4`)
- **Containerization:** Fully orchestrated using `Docker Compose`, spinning up both the ETL application and a dedicated PostgreSQL database container seamlessly.
- **Unit Testing:** Validated with an automated test suite using `Pytest` (Test Coverage >80%).
- **Security:** Strict secrets management using `python-dotenv` to protect API credentials.

## 🛠️ Tech Stack

- **Language:** Python 3.10
- **Libraries:** Pandas, BeautifulSoup4, Requests, SQLAlchemy, Google API Client, Pytest
- **Infrastructure:** Docker, Docker Compose, PostgreSQL
- **Version Control:** Git & GitHub

## ⚙️ How to Run Locally (with Docker)

The easiest way to run this pipeline is using Docker. You don't need to install Python or PostgreSQL on your host machine.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AlifFauzan21/end-to-end-etl-pipeline.git](https://github.com/AlifFauzan21/end-to-end-etl-pipeline.git)
   cd end-to-end-etl-pipeline
