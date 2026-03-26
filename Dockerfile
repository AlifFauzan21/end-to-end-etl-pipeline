# Pake Python versi ringan
FROM python:3.10-slim

# Bikin folder kerja di dalam Docker
WORKDIR /app

# Copy file requirements dulu biar di-install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-dotenv

# Copy seluruh file proyek lu ke dalam Docker
COPY . .

# Perintah yang dijalanin pas container nyala
CMD ["python", "main.py"]
