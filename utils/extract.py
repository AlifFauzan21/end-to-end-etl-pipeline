import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def extract_data(base_url="https://fashion-studio.dicoding.dev", total_pages=50):
    print("Memulai proses ekstraksi data...")
    extracted_data = []
    base_url = base_url.rstrip('/')

    for page in range(1, total_pages + 1):
        # Deteksi otomatis format URL Dicoding
        url_1 = f"{base_url}/page{page}/" 
        url_2 = f"{base_url}/page/{page}/"
        url_3 = f"{base_url}/?page={page}"
        
        target_url = base_url if page == 1 else url_1
        
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(target_url, headers=headers, timeout=10)
            
            # Auto-fallback jika format URL pertama 404
            if page > 1 and response.status_code == 404:
                response = requests.get(url_2, headers=headers, timeout=10)
                if response.status_code == 404:
                    response = requests.get(url_3, headers=headers, timeout=10)
            
            if response.status_code == 404:
                print(f"Halaman {page} tidak ditemukan (404). Asumsi halaman habis, lanjut...")
                continue
                
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # STRATEGI BRUTAL: Cari semua judul tanpa peduli nama Class div-nya
            title_tags = soup.find_all(['h3', 'h2', 'h5'])
            
            for tag in title_tags:
                try:
                    title = tag.text.strip()
                    if not title or len(title) < 3: 
                        continue
                    
                    # Naik ke parent element untuk nyari bungkus 1 produk full
                    container = tag.parent
                    found_container = False
                    for _ in range(4): # Naik tangga max 4 level parent
                        if container is None: break
                        text_content = container.get_text(separator=' ').lower()
                        # Ciri-ciri produk: ada harga dan ada info warna/size
                        if ('$' in text_content or 'price' in text_content) and ('color' in text_content or 'size' in text_content):
                            found_container = True
                            break
                        container = container.parent
                        
                    if not found_container or not container:
                        continue
                        
                    # Ekstrak teks secara brutal baris per baris
                    price = "Price Unavailable"
                    rating = "Invalid Rating"
                    colors = "Unknown Colors"
                    size = "Unknown Size"
                    gender = "Unknown Gender"

                    texts = container.get_text(separator='|').split('|')
                    for text in texts:
                        text = text.strip()
                        if not text: continue
                        
                        if '$' in text or 'Price Unavailable' in text:
                            price = text
                        elif '/ 5' in text:
                            rating = text
                        elif 'Color' in text or 'color' in text:
                            colors = text
                        elif 'Size' in text:
                            size = text
                        elif 'Gender' in text:
                            gender = text

                    extracted_data.append({
                        'Title': title,
                        'Price': price,
                        'Rating': rating,
                        'Colors': colors,
                        'Size': size,
                        'Gender': gender
                    })
                except Exception as e:
                    continue
                    
        except requests.exceptions.RequestException as e:
            print(f"Error mengakses halaman {page}: {e}")
            continue
            
        # Jeda dikit biar gak disangka hacker DDOS
        time.sleep(0.5)

    df = pd.DataFrame(extracted_data)
    
    if not df.empty:
        # Hapus duplikat dari hasil ekstraksi brutal
        df = df.drop_duplicates(subset=['Title', 'Price', 'Colors'])
    
    print(f"Ekstraksi selesai. Total data mentah: {len(df)} baris.")
    return df