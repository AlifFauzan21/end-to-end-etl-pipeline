import pandas as pd
from utils.transform import transform_data

def test_transform_data():
    data_mentah = {
        'Title': ['Kemeja Flanel', 'Unknown Product'],
        'Price': ['$20', 'Price Unavailable'],
        'Rating': ['4.5 / 5', 'Invalid Rating'],
        'Colors': ['2 Colors', 'Unknown Colors'],
        'Size': ['Size: L', 'Unknown Size'],
        'Gender': ['Gender: Women', 'Unknown Gender']
    }

    df_raw = pd.DataFrame(data_mentah)

    df_clean = transform_data(df_raw)

    assert len(df_clean) == 1
    assert df_clean.iloc[0]['Price'] == 320000.0
    assert df_clean.iloc[0]['Rating'] == 4.5
    assert df_clean.iloc[0]['Colors'] == 2
    assert df_clean.iloc[0]['Size'] == 'L'
    assert df_clean.iloc[0]['Gender'] == 'Women'
    assert 'timestamp' in df_clean.columns