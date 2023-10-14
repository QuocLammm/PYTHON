def main():
    greeting = input("Nhập lời chào của bạn: ")
    money = value(greeting)
    print(money)


def value(greeting):
    greeting = greeting.lower().strip()

    if greeting == "hello":
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
