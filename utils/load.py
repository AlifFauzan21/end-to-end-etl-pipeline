import os
import pandas as pd
from sqlalchemy import create_engine
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


def load_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"Data berhasil disimpan ke {filename}")
    except Exception as e:
        print(f"Error menyimpan ke CSV: {e}")


def load_to_postgres(df):
    # Ambil dari environment variable (Docker friendly)
    db_url = os.getenv(
        "DB_URL",
        "postgresql://developer:password@localhost:5432/booksdb"
    )

    try:
        engine = create_engine(db_url)

        df.to_sql(
            "fashion_competitor",
            engine,
            if_exists='replace',
            index=False
        )

        print("Data berhasil disimpan ke PostgreSQL")

    except Exception as e:
        print(f"Error menyimpan ke PostgreSQL: {e}")


def load_to_gsheets(df, spreadsheet_id=None, range_name="Sheet1!A1"):
    try:
        # Ambil spreadsheet ID dari env kalau tidak dikasih
        if spreadsheet_id is None:
            spreadsheet_id = os.getenv("SPREADSHEET_ID")

        if not spreadsheet_id:
            raise ValueError("SPREADSHEET_ID tidak ditemukan!")

        # Setup credentials
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_file(
            'google-sheets-api.json',
            scopes=SCOPES
        )

        service = build('sheets', 'v4', credentials=creds)

        # Copy dataframe biar aman
        df_copy = df.copy()

        # Convert timestamp ke string (biar GSheets gak error)
        if 'timestamp' in df_copy.columns:
            df_copy['timestamp'] = df_copy['timestamp'].astype(str)

        # Format data (header + rows)
        values = [df_copy.columns.tolist()] + df_copy.values.tolist()
        body = {'values': values}

        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="RAW",
            body=body
        ).execute()

        print(
            f"Data berhasil disimpan ke Google Sheets. "
            f"{result.get('updatedCells')} cells updated."
        )

    except Exception as e:
        print(f"Error menyimpan ke Google Sheets: {e}")