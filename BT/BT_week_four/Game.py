import random

def get_level():
    while True:
        try:
            level = int(input("Nhập một số nguyên dương là cấp độ, n: "))
            if level > 0:
                return level
            else:
                print("Vui lòng nhập một số nguyên dương.")
        except ValueError:
            print("Vui lòng nhập một số nguyên dương.")

def play_game(level):
    target_number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Nhập dự đoán của bạn: "))

            if guess < target_number:
                print("Too small! Thử lại.")
            elif guess > target_number:
                print("Too large! Thử lại.")
            else:
                print("Just right! ")
                break
        except ValueError:
            print("Vui lòng nhập một số nguyên dương.")

def main():
    level = get_level()
    print(f"Đã chọn cấp độ: {level}")
    play_game(level)

if __name__ == "__main__":
    main()
