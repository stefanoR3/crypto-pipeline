# for http requests ( server -> client). installed in venv
import requests
from api_utils import APImanager

#for time stamp
from datetime import datetime 

#create object (Instance)
manager = APImanager(currency = 'usd')

#strip = trim in java (to delate spaces)
coin_name = input("Wich cryptocurrency do you want to ceck: ").lower().strip()
    
#function test:

price = manager.get_crypto_price(coin_name)

if price:
    #capture current time
    #strftime = string format time (to edit)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] {coin_name.capitalize()}: ${price:,}")
else:
    print("error retrieving data!")