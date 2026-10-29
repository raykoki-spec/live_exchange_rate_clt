import requests

URL = "https://open.er-api.com/v6/latest/USD"

def main():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        kes_rate = data["rates"]["KES"]
        print(f"Exchange rate from USD to KES: {kes_rate}")

        for amount in [10000, 50000, 100000]:
            usd_amount = amount / kes_rate
            print(f"{amount:,} KES = {usd_amount:.2f} USD")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")

    except KeyError:
        print("Error: KES rate not found in the response.")

if __name__ == "__main__":
    main()
    
