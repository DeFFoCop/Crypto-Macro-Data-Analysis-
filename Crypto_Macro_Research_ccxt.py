import ccxt
#set the exchange we will be extracting from
bitmex   = ccxt.bitmex()

# Set the timeframe for the data (e.g., '1d' for daily, '1h' for hourly)
timeframe = '1d'
# Get the OHLCV (Open-High-Low-Close-Volume) data for the BTC/USDT trading pair
symbol = 'BTC/USDT'
limit = 1000  # Number of data points to retrieve

# Fetch the historical data from the exchange
data =  bitmex.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

# Print the retrieved data
for candle in data:
    print(candle)