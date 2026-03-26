from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import load_to_csv, load_to_postgres, load_to_gsheets

def main():
    print("=== Memulai ETL Pipeline ===")
    
    # 1. Extract
    raw_data = extract_data(total_pages=50)
    
    if raw_data.empty:
        print("Gagal mengekstrak data. Pipeline dihentikan.")
        return
        
    # 2. Transform
    clean_data = transform_data(raw_data)
    
    if clean_data.empty:
        print("Gagal membersihkan data. Pipeline dihentikan.")
        return
        
    # 3. Load
    # Ganti SPREADSHEET_ID dengan ID asli dari link G-Sheets lu
    SPREADSHEET_ID = '1Bmo9MfeYrNPLwuj_SRcC4DTxJBThptaT4LBBr7psfSQ' 
    
    load_to_csv(clean_data)
    load_to_postgres(clean_data) # Pastikan Postgres lu jalan dan kredensialnya benar
    load_to_gsheets(clean_data, SPREADSHEET_ID)
    
    print("=== ETL Pipeline Selesai ===")

if __name__ == "__main__":
    main()