import requests

class APImanager:

    #constructor
    #self for variable name manager 
    def __init__ (self,currency = 'usd'):
        #API -> 'f' for variables introduction (placeholder)
        self.base_url = "https://api.coingecko.com/api/v3/simple/price"
        self.currency = currency


    def get_crypto_price(self, coin):

        #get request to server parameters -> for request function
        #params automatically handles spaces
        params = {
            'ids': coin,
            'vs_currencies': self.currency
        }
        
        try:
            #send request
            response = requests.get(self.base_url,params=params)

            #auto catch code errors
            response.raise_for_status()

            #state code 200 = connection successful
            #state code 404 = not found
            #state cade 500 = server error

            data = response.json()

            #json -> from raw text to dictionary
            #data is a dictionary of dictionary/s
            #{bitcoin: {usd: {xxx}}} -> bitcoin is n element of a dictionary itself

            return data[coin][self.currency]
        
        except KeyError:
            #error name spelled wrong coin or currency
            print(f"Key error: The coin '{coin}' was not found")
            return None
        except requests.exceptions.RequestException as e:
            #network errors -> no internet/server down
            print(f"Exception: {e}")
        except Exception as e:
            #general error
            print(f"Unexpected error occured")
            return None
