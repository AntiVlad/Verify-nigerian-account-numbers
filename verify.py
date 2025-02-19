import csv
import requests

# Replace with your Paystack secret key
SECRET_KEY = "your_paystacks_secret_key"
URL = "https://api.paystack.co/bank/resolve"

# Input and Output CSV files
INPUT_CSV = "accounts.csv"
OUTPUT_CSV = "verified_accounts.csv"

def verify_account(account_number, bank_code):
    headers = {
        "Authorization": f"Bearer {SECRET_KEY}"
    }
    params = {
        "account_number": account_number.strip(),
        "bank_code": bank_code.strip()
    }

    response = requests.get(URL, headers=headers, params=params)
    data = response.json()

    if data.get("status"):
        return data["data"]["account_name"]
    else:
        return "Verification Failed"

def process_csv(input_file, output_file):
    with open(input_file, "r", newline="", encoding="utf-8") as infile, \
         open(output_file, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        writer.writerow(["Account Number", "Bank Code", "Account Name"])

        for row in reader:
            if len(row) < 2:
                continue
            account_number, bank_code = row
            account_name = verify_account(account_number, bank_code)
            writer.writerow([account_number, bank_code, account_name])
            print(f"Verified: {account_number} - {account_name}")

process_csv(INPUT_CSV, OUTPUT_CSV)
print(f"Verification completed! Results saved in {OUTPUT_CSV}")
