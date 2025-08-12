import sys
import requests

def crypto():
    try:
        if len(sys.argv) < 3:
            bitcoin_num = float(sys.argv[1])
            response = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=5015b33d97498558fb156479aa7a5e8287aef26409bd8929f501dd4adfb9a450').json()
            amount = float(response['data']['priceUsd']) * bitcoin_num
            print(f"${amount:,.4f}")
        else:
            sys.exit('Missing command-line argument  ')
    except ValueError:
        sys.exit('Command-line argument is not a number')

crypto()
