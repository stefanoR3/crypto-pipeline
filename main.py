import requests

def get_crypto_price(coin):
    #API -> 'f' for variables introduction
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

    #get request to server
    response = requests.get(url)

    #state code 200 = connection successful
    if response.status_code==200:
        print("Connection successful! The api is responding")
        data = response.json()
        return data[coin]['usd']
    else:
        return None
    
#function test:

price = get_crypto_price('bitcoin')
if price:
    print(f"current Bitcoin price: ${price}")
else:
    print("Eroare la preluarea datelor.")