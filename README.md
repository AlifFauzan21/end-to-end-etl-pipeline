# 🛍️ End-to-End Fashion ETL Pipeline

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/docker-compose-2496ED?logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Dicoding-⭐%205%20Stars%20Advanced-gold" />
  <img src="https://img.shields.io/badge/coverage-82%25-brightgreen" />
</p>

<p align="center">
  A modular, production-ready ETL pipeline built with Python and containerized with Docker.<br/>
  Awarded <strong>5 Stars / Advanced Level</strong> as the Final Project for <em>Belajar Fundamental Pemrosesan Data</em> — Dicoding Indonesia.
</p>

---

## 📌 Overview

Pipeline ini mengotomatiskan proses **Extract → Transform → Load** data produk fashion dari kompetitor, membersihkan data, lalu memuatnya ke berbagai tujuan penyimpanan untuk kebutuhan analitik.

```
Raw Web Data → Scraping → Cleaning & Transform → CSV / PostgreSQL / Google Sheets
```

---

## 🚀 Features

| # | Feature | Detail |
|---|---------|--------|
| 1 | **Extract** | Scraping multi-halaman dengan `Requests` & `BeautifulSoup4`, pagination & error handling |
| 2 | **Transform** | Pembersihan data dengan `Pandas`, konversi mata uang ke IDR, filter data invalid via Regex |
| 3 | **Load** | Output ke CSV, PostgreSQL (via SQLAlchemy), dan Google Sheets API v4 |
| 4 | **Containerized** | Full Docker Compose — auto-spin PostgreSQL + ETL app |
| 5 | **Unit Testing** | `pytest` dengan code coverage **82%** |

---

## 📂 Project Structure

```
end-to-end-etl-pipeline/
├── utils/
│   ├── __init__.py
│   ├── extract.py       # Web scraping logic
│   ├── transform.py     # Data cleaning & transformation
│   └── load.py          # Load to CSV, PostgreSQL, Google Sheets
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── .gitignore
```

---

## 📊 Data Schema

Schema dataset setelah proses transformasi:

| Column | Type | Description |
|--------|------|-------------|
| `Title` | String | Nama produk |
| `Price` | Float | Harga dalam IDR |
| `Rating` | Float | Rating produk |
| `Colors` | Int | Jumlah warna tersedia |
| `Size` | String | Ukuran produk |
| `Gender` | String | Target gender |
| `timestamp` | String | Waktu scraping |

---

## ⚙️ How to Run

### 🐳 Docker (Recommended)

```bash
# 1. Clone repository
git clone https://github.com/AlifFauzan21/end-to-end-etl-pipeline.git
cd end-to-end-etl-pipeline

# 2. Buat file .env
echo "SPREADSHEET_ID=your_google_sheet_id" > .env

# 3. Tambahkan credentials Google Sheets
#    → Letakkan file google-sheets-api.json di root project

# 4. Jalankan pipeline
docker-compose up --build
```

### 💻 Local (Tanpa Docker)

```bash
# 1. Setup virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. Pastikan PostgreSQL berjalan
sudo service postgresql start

# 3. Jalankan pipeline
python main.py
```

---

## 🧪 Unit Testing

```bash
# Jalankan semua test
pytest tests/ -v

# Dengan laporan coverage
pytest --cov=utils tests/
```

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `DB_URL` | PostgreSQL connection string |
| `SPREADSHEET_ID` | Google Sheets document ID |

> Salin `.env.example` → `.env` dan isi nilainya sebelum menjalankan pipeline.

---

## 📈 Output

Pipeline menghasilkan tiga output secara bersamaan:

- 📄 **`products.csv`** — file lokal hasil scraping yang sudah dibersihkan
- 🐘 **PostgreSQL** — tabel `fashion_competitor` siap untuk query analitik
- ☁️ **Google Sheets** — data terupdate otomatis di spreadsheet

---

## 🧠 Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/BeautifulSoup4-43B02A" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Google%20Sheets%20API-34A853?logo=googlesheets&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=white" />
</p>

---

## 👨‍💻 Author

**Alif Fauzan**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alif-fauzan-9a97b0277)

---

> *From raw web data → clean structured dataset → multi-platform storage* 🚀
