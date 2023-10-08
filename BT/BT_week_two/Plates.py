# hãy triển khai một chương trình nhắc người dùng nhập vào một 
#biển số rồi xuất ra Valid nếu đáp ứng tất cả các yêu cầu hoặc Invalid nếu 
#không. Giả sử rằng mọi chữ cái trong dữ liệu nhập của người dùng sẽ là chữ
#hoa. Cấu trúc chương trình của bạn theo bên dưới, trong đó is_valid trả về True
#nếu s đáp ứng tất cả các yêu cầu và False nếu không. Giả sử đó s sẽ là 
#một str. Bạn có thể triển khai các chức năng bổ sung để hàm is_valid gọi (ví dụ: 
#một chức năng cho mỗi yêu cầu).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        
def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            if s[2].isdigit() and s[2] != '0':
                for i in range(3, len(s)):
                    if not s[i].isdigit():
                        return False
                return True
    return False

main()
