import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data import Data

class Visual(Data):
    def __init__(self, link) -> None:
        super().__init__(link)


    # Export time-series data based on time and moving average 
    def time_series(self, mv=20, date_range="all"):
        stock_data = self.df.copy()

        # Compute the moving average
        stock_data[f'{mv}-day SMA'] = stock_data['Close'].rolling(window=mv).mean()

        # Filter based on range

        today = pd.Timestamp.now()

        if date_range == '5 year':
            start_date = today - pd.DateOffset(years=5)
        elif date_range == 'year':
            start_date = today - pd.DateOffset(years=1)
        elif date_range == 'month':
            start_date = today - pd.DateOffset(months=1)
        elif date_range == 'week':
            start_date = today - pd.DateOffset(weeks=1)
        elif date_range == 'all':
            start_date = stock_data['Date'].min()

        # Filter the stock data by the date range
        stock_data = stock_data[stock_data['Date'] >= start_date]

        stock_data['Date'] = stock_data['Date'].dt.strftime('%Y-%m-%d')
        
        # Convert to JSON (array of objects with 'Date', 'Close', and 'SMA')
        json_data = stock_data[['Date', 'Close', f'{mv}-day SMA']].to_json(orient='records', date_format='iso')
        
        return json_data

    # Historic monthly price change over the years
    def monthly_average(self):
        stock_data = self.df.copy()
        monthly_price_change = stock_data.groupby(['Year', 'Month'])['Close'].mean().pct_change() * 100

        # Pivot data jadi tabel tahun dan bulan dan melihat pct_change()
        price_change_pivot = monthly_price_change.unstack()

        # Buat heatmap hasil pivot
        plt.figure(figsize=(12, 8))
        sns.heatmap(price_change_pivot, annot=True, fmt=".2f", cmap="RdYlGn", linewidths=0.5)
        plt.title('Monthly Price Change for Stock (in %)')
        plt.xlabel('Month')
        plt.ylabel('Year')
        plt.tight_layout()

        # Export image
        link_path = f'./assets/table_change.png'
        plt.savefig(link_path)
        print(f"Plot saved to '{link_path}'")


    def volume_analysis(self, date_range='all'):
        stock_data = self.df.copy()
        daily_volume = stock_data.groupby('Date')['Volume'].mean().reset_index()

        today = pd.Timestamp.now()

        if date_range == '5 year':
            start_date = today - pd.DateOffset(years=5)
        elif date_range == 'year':
            start_date = today - pd.DateOffset(years=1)
        elif date_range == 'month':
            start_date = today - pd.DateOffset(months=1)
        elif date_range == 'week':
            start_date = today - pd.DateOffset(weeks=1)
        elif date_range == 'all':
            start_date = stock_data['Date'].min() 

        daily_volume = daily_volume[daily_volume['Date'] >= start_date]
        daily_volume['Date'] = daily_volume['Date'].dt.strftime('%Y-%m-%d')
        
        # Convert to JSON using the json module
        json_data = daily_volume[['Date', 'Volume']].to_json(orient='records')
        return json_data

    def price_and_percent(self, date_range='all'):
        stock_data = self.df.copy()
        stock_data['Close_Pct_Change'] = stock_data['Close'].pct_change()

        # Set up precision for better spread
        stock_data['Close_Pct_Change'] = stock_data['Close_Pct_Change'].round(6)

        today = pd.Timestamp.now()
        if date_range == '5 year':
            start_date = today - pd.DateOffset(years=5)
        elif date_range == 'year':
            start_date = today - pd.DateOffset(years=1)
        elif date_range == 'month':
            start_date = today - pd.DateOffset(months=1)
        elif date_range == 'week':
            start_date = today - pd.DateOffset(weeks=1)
        elif date_range == 'all':
            start_date = stock_data['Date'].min() 

        stock_data = stock_data[stock_data['Date'] >= start_date]
        stock_data['Date'] = stock_data['Date'].dt.strftime('%Y-%m-%d')
        
        # Create an array of JSON objects with 'Date' and 'Close_Pct_Change'
        json_array = stock_data[['Date', 'Close_Pct_Change']].to_json(orient='records')
        return json_array




        