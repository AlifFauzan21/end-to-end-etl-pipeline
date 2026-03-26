import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from utils.extract import extract_data

@patch('utils.extract.requests.get')
def test_extract_data(mock_get):
    # Kita pura-pura (mock) balasan dari website Dicoding
    mock_response = MagicMock()
    mock_response.text = '''
    <div class="product-card">
        <h3>Kaos Keren</h3>
        <span class="price">$10</span>
        <span class="rating">4.8 / 5</span>
        <span class="colors">3 Colors</span>
        <span class="size">Size: M</span>
        <span class="gender">Gender: Men</span>
    </div>
    '''
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    # Jalankan fungsi extract (cukup 1 halaman aja buat ngetes)
    df = extract_data(total_pages=1)

    # Validasi hasilnya
    assert len(df) == 1
    assert df.iloc[0]['Title'] == 'Kaos Keren'
    assert df.iloc[0]['Price'] == '$10'
    assert df.iloc[0]['Rating'] == '4.8 / 5'
    assert df.iloc[0]['Colors'] == '3 Colors'
    assert df.iloc[0]['Size'] == 'Size: M'
    assert df.iloc[0]['Gender'] == 'Gender: Men'