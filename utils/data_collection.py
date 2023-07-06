import pandas as pd
import requests

def collect_data(api_key, symbol, start_date, end_date):
    # Add code here to collect data from the stock market API
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key,
        "outputsize": "full",
        "datatype": "csv",
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = pd.read_csv(response.url)
            data['date'] = pd.to_datetime(data['timestamp'])
            data.set_index('date', inplace=True)
            data = data.loc[start_date:end_date]
            return data
        else:
            print(f"Error: Unable to fetch data from the API. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: Unable to fetch data from the API. {e}")
        return None
