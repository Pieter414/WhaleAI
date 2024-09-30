import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data import Data

class Visual(Data):
    def __init__(self, link) -> None:
        super().__init__(link)

    def time_series(self, mv=20, date_range="all"):
        stock_data = self.df.copy()
        stock_data[f'{mv}-day SMA'] = stock_data['Previous'].rolling(window=mv).mean()

        # Filter data berdasarkan range waktunya
        today = pd.Timestamp.now()

        if date_range == 'year':
            start_date = today - pd.DateOffset(years=1)
        elif date_range == 'week':
            start_date = today - pd.DateOffset(weeks=1)
        elif date_range == 'all':
            start_date = stock_data['Last Trading Date'].min()  # Use the earliest date if no range specified

        stock_data = stock_data[stock_data['Last Trading Date'] >= start_date]

        # Plot garis data yang difilter dengan moving average
        plt.figure(figsize=(10, 6))
        plt.plot(stock_data['Last Trading Date'], stock_data['Previous'], label='Closing Price')
        plt.plot(stock_data['Last Trading Date'], stock_data[f'{mv}-day SMA'], label=f'{mv}-day SMA', linestyle='--')

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

    def monthly_average(self):
        stock_data = self.df.copy()
        monthly_price_change = stock_data.groupby(['Year', 'Month'])['Previous'].mean().pct_change() * 100

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

        