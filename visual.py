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
        stock_data[f'{mv}-day SMA'] = stock_data['Close'].rolling(window=mv).mean()

        # Filter data berdasarkan range waktunya
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


        # Plot garis data yang difilter dengan moving average
        plt.figure(figsize=(10, 6))
        plt.plot(stock_data['Date'], stock_data['Close'], label='Closing Price')
        plt.plot(stock_data['Date'], stock_data[f'{mv}-day SMA'], label=f'{mv}-day SMA', linestyle='--')

        plt.title(f'Stock Closing Price and {mv}-day SMA - Last {date_range.capitalize()}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Export image
        link_path = f'./assets/time_series_{date_range}.png'
        plt.savefig(link_path)
        print(f"Plot saved to '{link_path}'")


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

        # Filter data berdasarkan range waktunya
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
        
        plt.figure(figsize=(12, 6))
        plt.plot(daily_volume['Date'], daily_volume['Volume'], marker='o', color='blue')
        
        plt.title('Daily Volume Trend for BBCA')
        plt.xlabel('Date')
        plt.ylabel('Average Daily Volume')
        plt.grid(True)
        plt.tight_layout()
        
        # Export image
        link_path = f'./assets/volume_analysis_{date_range}.png'
        plt.savefig(link_path)
        print(f"Plot saved to '{link_path}'")


    def price_and_percent(self):
        stock_data = self.df.copy()
        stock_data['Percent Change'] = stock_data['Close'].pct_change() * 100
        
        plt.figure(figsize=(12, 6))
        plt.hist(stock_data['Percent Change'].dropna(), bins=30, color='orange', alpha=0.7)
        plt.title('Percent Change Distribution for BBCA')
        plt.xlabel('Percent Change (%)')
        plt.ylabel('Frequency')

        # Display the plot
        plt.tight_layout()
        
        # Export image
        link_path = f'./assets/price_percent_change.png'
        plt.savefig(link_path)
        print(f"Plot saved to '{link_path}'")



        