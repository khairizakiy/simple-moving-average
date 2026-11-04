import numpy as np
import yfinance as yf

yf.set_tz_cache_location("custom/cache/location")

symbols = input('input symbols:')

dat = yf.Ticker(symbols)
history = dat.history(period='50D') # ngambil history di parameter dat

buffer = history['Close'].dropna().tolist() # buffer ngambil history, dropna buang yang kosong, toslist bentuk jadi list biasa

def get_price(data: dict):
    price = data.get('price') # ngambil harga dari yfinance
    if price is not None:
        buffer.append(price) # kalo harga gak kosong bakal nambah
    if len(buffer) > 50:
        buffer.pop(0) #.pop untuk buang 1 data
    if len(buffer) < 50:
        print({price}) # jika kurang dari 20 maka nunggu
        return
    ma_short = np.mean(buffer[-10:]) # hitung rata"
    ma_long = np.mean(buffer[-50:])
    if ma_short > ma_long:
        signal = "BUY"
    else:
        signal = "SELL"
    
    print(f"{price} | MA 10 = {ma_short:<9.2f} | MA 50 = {ma_long:<9.2f} | {signal}")

dat.live(message_handler=get_price)