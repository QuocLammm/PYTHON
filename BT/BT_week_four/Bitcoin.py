import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Raises a HTTPError for bad requests (4xx and 5xx)
        bitcoin_data = response.json()
        return float(bitcoin_data['bpi']['USD']['rate_float'])
    except requests.RequestException as e:
        print(f"Missing command-line argument {str(e)}")
        sys.exit(1)
    except KeyError:
        print("Missing command-line argumentd")
        sys.exit(1)

def main():
    try:
        n = float(input("Nhập số lượng Bitcoin bạn muốn mua: "))
    except ValueError:
        print(" Command-line argument is not a number")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    total_cost = n * bitcoin_price
    print(f"Chi phí hiện tại của {n:.4f} Bitcoin là: ${total_cost:,.4f}")

if __name__ == "__main__":
    main()
