import sys
from pyfiglet import Figlet

def print_random_font(text):
    # Lấy một phông chữ ngẫu nhiên từ danh sách            
    figlet = Figlet()
    print(f"Văn bản được xuất bằng phông chữ ngẫu nhiên:")
    print(figlet.renderText(text))

def print_in_font(text, font):
    # Xuất văn bản theo phông chữ
    figlet = Figlet(font=font)
    print(f"Văn bản được xuất bằng phông chữ '{font}':")
    print(figlet.renderText(text))

if __name__ == "__main__":
    num_args = len(sys.argv) - 1  # Số lượng đối số dòng lệnh

    # Xử lý trường hợp không hoặc hai đối số dòng lệnh
    if num_args == 0:
        user_text = input("Nhập văn bản: ")
        print_random_font(user_text)
    elif num_args == 2 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        user_font = sys.argv[2]
        user_text = input("Nhập văn bản: ")
        print_in_font(user_text, user_font)
    else:
        print("Invalid usage")
        sys.exit(1)

#cách text:
#Chạy chương trình của bạn với python figlet.py test. Chương trình của bạn sẽ thoát qua sys.exit và in thông báo lỗi: Invalid usage
#Chạy chương trình của bạn với python figlet.py -f invalid_font. Chương trình của bạn sẽ thoát qua sys.exit và in thông báo lỗi: Invalid usage
# -f rectangles, -f slant,-f alphabet, --font
