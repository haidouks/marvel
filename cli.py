import hashlib
import requests
import datetime
from pprint import pprint
import logging
#from marvel import Marvel #Did not want to use client :)

logging.basicConfig( #Set logging format & config
    level = logging.INFO, #logging.DEBUG to see debug messages
    format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
    )

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

#Keys received from Marvel
public_key = 'a66345542c86987744a1702aa4fa6c5a'
private_key = 'b7b6e3b60bfa422572ef626753fe2c5cb2de8c6b'

def hash_params():
    """ Marvel API required md5 hash of timestamp + public key + private key """
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{private_key}{public_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()
    return hashed_params

def search_marvel_characters(keyword: str):
    matching_characters = []
    #Set request parameters for marvel characters api
    params = {
        'ts': timestamp, 
        'apikey': public_key, 
        'hash': hash_params(),
        'limit': 50,
        'offset' : 0 #
        }
    do = True 
    while(do):

        logging.debug(msg=f"Checking for offset: {params['offset']}")
        response = requests.get(
            url = 'https://gateway.marvel.com:443/v1/public/characters',
            params=params
        )
        results = response.json()["data"]["results"] #Get results from response
        for character in results:
            logging.debug(msg=f'Checking if {character["name"]} matchs {keyword}')
            if keyword.lower() in character["name"].lower(): # Lower both variable and don't miss matching capital letters
                logging.debug(msg=f"{character}") # Found character name matching with keyword
                matching_characters.append(character)
        params["offset"] = params["offset"] + params["limit"] #increase offset on each iteration
        if params["offset"] > response.json()["data"]["total"]: #Continue while offset is less than total record count 
            do = False
    return matching_characters

if __name__ == "__main__":
    character_name = input("Please enter a keyword: ")
    print(search_marvel_characters(keyword=character_name))
