import sys
import requests #Dùng thư viện request để truy xuất trang thông tin

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
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
        n = float(input("Nhập số lượng Bitcoin:"))
        bitcoin_price = get_bitcoin_price()
        amount = n * bitcoin_price
        print(f"${amount:,.4f}")
    except ValueError:
        print(" Command-line argument is not a number")
        sys.exit(1)

    


if __name__ == "__main__":
    main()
    
#Chạy chương trình của bạn với python bitcoin.py. Chương trình của bạn nên sử
#dụng sys.exit để thoát với thông báo lỗi: Missing command-line argument
#• Chạy chương trình của bạn với python bitcoin.py cat. Chương trình của bạn nên sử
#dụng sys.exit để thoát với thông báo lỗi: Command-line argument is not a number
#• Chạy chương trình của bạn với python bitcoin.py 1. Chương trình của bạn phải xuất giá
#của một Bitcoin đến bốn chữ số thập phân, sử dụng ‘,’ làm dấu phân cách hàng nghìn .
