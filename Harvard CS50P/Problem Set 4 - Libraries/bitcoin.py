# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import sys
import json
import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    units = float(sys.argv[1]) # check that command-line argument exists and is a number
    try:
        data = requests.get(url).json() # check that url is valid
        price = float(data['bpi']['USD']['rate'].replace(',','') )
        total = units*price
        print(f"${total:,.4f}")
    except requests.RequestException as e:
        print(e)
    except Exception as e:
        print(e)
except IndexError: # missing argument - sys.argv[1] does not exist
    sys.exit("Missing command-line argument")
except ValueError: # non-numerical argument - sys.argv[1] cannot be converted to a float
    sys.exit("Command-line argument is not a number")
