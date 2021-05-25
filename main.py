from binance.client import Client
import json
import os
#python-binance
apikey='DPnNZxc3BWwpyR9Crteh2lAvdNCWuwgvrJNH0GlqGl81f8n2r9TyUyuSPvkLo08e'
secretkey='r6oaxvU3bY7hFc3Z9s2i4P5ng7xVN5RRoK2fVNPNqsBNAE7dMHs0jhcSdtW22ju5'

client = Client(apikey, secretkey)

#avg_price = client.get_avg_price(symbol='BNBBTC')   

#info = client.get_account()
klinesA = client.get_historical_klines("BTCUSDT","2h", "1 day ago UTC")

coinPriceFile = 'docs/result.json'

if os.path.exists(coinPriceFile):
    os.remove(coinPriceFile)

with open(coinPriceFile, 'a') as acutalPriceFile:
    json.dump(klinesA, acutalPriceFile)
