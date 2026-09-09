# Verify Nigerian Account Numbers

A Python utility to verify and resolve Nigerian bank account numbers in bulk using the [Paystack](https://paystack.com/) Account Resolution API.

## Features

- **Batch Verification**: Resolves account holder names across hundreds of accounts automatically from a CSV file.
- **Export Verified Data**: Writes results and validated account names directly to `verified_accounts.csv`.
- **Bank Directory Included**: Bundles official CBN bank codes for all Nigerian commercial banks and fintechs in `bank codes.txt`.

---

## Prerequisites

- Python 3.7+
- A [Paystack](https://paystack.com/) account with an active Secret Key (`sk_live_...` or `sk_test_...`)
- `requests` package:
  ```bash
  pip install requests
  ```

---

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AntiVlad/Verify-nigerian-account-numbers.git
   cd Verify-nigerian-account-numbers
   ```

2. **Configure Paystack Secret Key**:
   Open `verify.py` and set your Paystack Secret Key:
   ```python
   SECRET_KEY = "sk_test_your_secret_key_here"
   ```

3. **Format Input Data**:
   Populate `accounts.csv` with account numbers and corresponding bank codes:
   ```csv
   account_number,bank_code
   0123456789,058
   9876543210,033
   ```
   *(Refer to `bank codes.txt` for the 3-digit bank codes)*.

4. **Execute Verification**:
   ```bash
   python verify.py
   ```

The script will process each account and generate `verified_accounts.csv` containing the validated account names.

---

## License

This project is licensed under the MIT License.
