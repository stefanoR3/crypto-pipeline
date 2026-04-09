import requests
import os
import json

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
            #{bitcoin: {usd: {xxx}, eur:{xxx}, ...}} -> 
            #we could have used .text

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
        
    def saveToJson(data,fileName = "crypto_history.json"):
        #file verification
        if os.path.exist(fileName):
            with open(fileName,"r") as file:
                #old data load ; r = read
                try:
                    db = json.load(file)
                except json.JSONDecodeError:
                    db = [] 
        else: 
            db=[]

        #add new line to file
        db.append(data)

        #save all back 
        with open (fileName, "w") as file:
            #w = write (deletes all previous data!)
            json.dump(db, file, indent = 4)
        

        
            
