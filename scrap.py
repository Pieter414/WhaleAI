import yfinance as yf
import pandas as pd
import json

# Fungsi untuk mengambil data saham dengan periode "max"
def fetch_stock_data(stock_symbol):
    try:
        hist = yf.Ticker(stock_symbol)
        df = hist.history(period="max", auto_adjust=True)
        
        if not df.empty:
            # Menampilkan 2 baris terakhir untuk contoh (bisa dihapus jika tidak diperlukan)
            print(df.tail(2))
            
            # Mengonversi indeks Timestamp menjadi string untuk JSON
            df.index = df.index.strftime('%Y-%m-%d')
            
            # Mengonversi seluruh DataFrame menjadi dictionary
            stock_data = df.reset_index().to_dict(orient='records')
            
            # Menyimpan data ke file JSON
            json_filename = f'{stock_symbol}_history.json'
            with open(json_filename, 'w') as json_file:
                json.dump(stock_data, json_file, indent=4)
            
            print(f"Data telah disimpan ke {json_filename}")
        else:
            print(f"Tidak ada data untuk saham {stock_symbol}")
    except Exception as e:
        print(f"Error fetching data for {stock_symbol}: {e}")

# Input simbol saham dari pengguna
if __name__ == "__main__":
    stock_symbol = input("Masukkan simbol saham yang ingin dicari (contoh: tlkm.jk): ")
    fetch_stock_data(stock_symbol)
