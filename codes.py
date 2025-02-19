#To get updated bank codes in case they're changed

import requests
URL = "https://api.paystack.co/bank"
response = requests.get(URL)
banks = response.json()

if banks.get("status"):
    for bank in banks["data"]:
        print(f"{bank['name']} - {bank['code']}")
else:
    print("Failed")
