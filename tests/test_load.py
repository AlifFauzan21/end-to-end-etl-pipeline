from unittest.mock import patch, MagicMock
import pandas as pd
from utils.load import load_to_csv, load_to_postgres, load_to_gsheets

@patch('pandas.DataFrame.to_csv')
def test_load_to_csv(mock_to_csv):
    df = pd.DataFrame({
        'Title': ['Baju'],
        'Price': ['$10']
    })

    load_to_csv(df, 'test_products.csv')
    mock_to_csv.assert_called_once_with('test_products.csv', index=False)


@patch('pandas.DataFrame.to_sql')
@patch('utils.load.create_engine')
def test_load_to_postgres(mock_create_engine, mock_to_sql):
    df = pd.DataFrame({
        'Title': ['Baju'],
        'Price': ['$10']
    })

    load_to_postgres(df, 'sqlite:///:memory:')
    mock_to_sql.assert_called_once()


@patch('utils.load.build')
@patch('utils.load.Credentials.from_service_account_file')
def test_load_to_gsheets(mock_creds, mock_build):
    df = pd.DataFrame({
        'Title': ['Baju'],
        'timestamp': ['2026-10-10']
    })
    
    mock_service = MagicMock()
    mock_build.return_value = mock_service

    # 🔥 penting biar chain call aman
    mock_service.spreadsheets.return_value.values.return_value.update.return_value.execute.return_value = {}

    load_to_gsheets(df, 'fake_spreadsheet_id')

    mock_service.spreadsheets.return_value.values.return_value.update.assert_called_once()