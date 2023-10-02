def camel_to_snake(s):
    s_case = ''
    for c in s:
        if c.isupper():
            s_case += '_' + c.lower()
        else:
            s_case += c
    return s_case.lstrip('_')  # Loại bỏ dấu '_' ở đầu kết quả (nếu có)

def main():
    a = input("Nhập chuỗi")
    print(camel_to_snake(a))
    
main()