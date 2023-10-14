def calculate_fuel_percentage(x, y):
    try:
        x = int(x)
        y = int(y)

        if x <= 0 or y <= 0:
            raise ValueError("X and Y must be positive integers")
        if x > y:
            raise ValueError("X must be less than or equal to Y")
        percentage = (x / y) * 100
        rounded_percentage = round(percentage)

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


def main():
    fraction = input("Nhập (dạng X/Y): ")
    
    x, y = fraction.split('/') # Tách X và Y từ phân số
    result = calculate_fuel_percentage(x, y)
    print(result)


if __name__ == "__main__":
    main()
