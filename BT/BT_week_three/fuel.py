def calculate_fuel_percentage(x, y):
    try:
        # Chuyển đổi x và y thành số nguyên
        x = int(x)
        y = int(y)

        # Kiểm tra x và y có đúng là số nguyên dương và y khác 0
        if x <= 0 or y <= 0:
            raise ValueError("X and Y must be positive integers")

        # Kiểm tra x có lớn hơn y
        if x > y:
            raise ValueError("X must be less than or equal to Y")

        # Tính phần trăm nhiên liệu
        percentage = (x / y) * 100

        # Làm tròn phần trăm và chuyển đổi thành số nguyên gần nhất
        rounded_percentage = round(percentage)

        # Xác định trạng thái của bình nhiên liệu
        if rounded_percentage <= 1:
            return 'E'
        elif rounded_percentage >= 99:
            return 'F'
        else:
            return str(rounded_percentage) + '%'

    except ValueError as ve:
        return str(ve)
    except ZeroDivisionError:
        return "Y cannot be zero"


if __name__ == "__main__":
    fraction = input("Nhập (dạng X/Y): ")
    
    x, y = fraction.split('/') # Tách X và Y từ phân số
    result = calculate_fuel_percentage(x, y)
    print(result)
