import requests
import json
from time import sleep
import sys
try:
    while True:
        sleep(2)

        response = requests.get("https://api.binance.us/api/v3/ticker/price?symbol=SHIBUSDT")
        output = response.json()
        data = json.dumps(output['price'])
        punctuation = '''"'''
        remove_punct = ""
        for character in data:
            if character not in punctuation:
                remove_punct = remove_punct + character
        
        shib_ammout = float(14610505.01186419)
        price = remove_punct
        price_as_float = float(price)
        net_profit = str(price_as_float * shib_ammout)


        print("current price of doge: " + net_profit, flush=True)
except KeyboardInterrupt:
    exit('\n')

    
