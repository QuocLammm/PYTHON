def generate_farewell(names):
    n = len(names)

    if n == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif n == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        farewell = ", ".join(names[:-1])
        farewell += f", and {names[-1]}"
        return f"Adieu, adieu, to {farewell}"

def main():
    names = []
    print("Nhập tên (nhấn Ctrl-Z để kết thúc nhập):")
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass  # Khi người dùng nhấn  Ctrl-Z 
    
    print(generate_farewell(names))

if __name__ == "__main__":
    main()
    
#Cách test:
#- Chạy chương trình của bạn với python adieu.py. Nhập Liesl và nhấn Enter, theo sau là
#control-z. Chương trình của bạn sẽ xuất ra: Adieu, adieu, to Liesl
#- Chạy chương trình của bạn với python adieu.py. Nhập Liesl và nhấn Enter, sau đó
#nhập Friedrich và nhấn Enter, theo sau là control-z. Chương trình của bạn sẽ xuất ra:
#Adieu, adieu, to Liesl and Friedrich
#- Chạy chương trình của bạn với python adieu.py. Nhập Liesl và nhấn Enter, sau đó
#nhập Friedrich và nhấn Enter. Bây giờ gõ Louisa và nhấn Enter, theo sau là control+z. Chương trình của bạn sẽ xuất ra: Adieu, adieu, to Liesl, Friedrich, and Louisa
