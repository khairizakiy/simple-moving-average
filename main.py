"""### Pilihan 2: "Detektor Sinyal Trading: Moving Average Crossover" (Tingkat: Menengah - Favorit Trader)                                              
                                                                                                                                                       
  • Tujuannya:                                                                                                                                         
  Membuat sistem yang bisa mendeteksi kapan waktu yang tepat untuk "Beli" dan "Jual" menggunakan strategi paling klasik di Wall Street (Golden Cross). 
  • Alur Logika yang Harus Anda Bangun:                                                                                                                
      # 1. Ambil data harga penutupan satu saham selama minimal 100 hari perdagangan.                                                                    
      # 2. Hitung garis rata-rata jangka pendek (misal: rata-rata bergerak 5 hari terakhir).                                                             
      # 3. Hitung garis rata-rata jangka panjang (misal: rata-rata bergerak 20 hari terakhir).                                                           
      4. Cari kondisi persilangan (crossover):                                                                                                         
          • Hari di mana garis 5-hari memotong ke atas garis 20-hari → Tandai sebagai Sinyal BELI.                                                     
          • Hari di mana garis 5-hari memotong ke bawah garis 20-hari → Tandai sebagai Sinyal JUAL.                                                    
      5. Kumpulkan data hari apa saja sinyal-sinyal tersebut terjadi.                                                                                  
  • Output yang Diharapkan di Terminal:                                                                                                                
  Daftar tanggal atau hari ke berapa saja sistem Anda menyuruh Anda "Beli" dan hari ke berapa menyuruh Anda "Jual".  """

import numpy as np
import yfinance as yf
import os
import pandas as pd

yf.set_tz_cache_location("custom/cache/location")
os.makedirs('cache', exist_ok=True)
pd.set_option('display.max_rows', None)

symbols = input("input a symbol (ex. ES=F, AAPL, ...):")

dat = yf.Tickers(symbols).history(period="100d") # no 1

close = dat.get(['Close']).values # no 1

def moving_average(): # no 2-4
    arr = np.array(close)
    short = arr[-5:]
    long = arr[-20:]
    rata_short = np.mean(short)
    rata_long = np.mean(long)
    if rata_short > rata_long:
        print('buy')
    else:
        print('sell')

moving_average() # no 5