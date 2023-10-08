phone_book = {}  # Danh bạ điện thoại


def add_contact():
    global phone_book
    name = input("Nhập tên: ")
    phone = input("Nhập số điện thoại: ")
    phone_book[name] = phone
    print("Đã thêm mục mới vào danh bạ.")


def search_contact():
    global phone_book
    name = input("Nhập tên cần tìm: ")
    if name in phone_book:
        print(f"Số điện thoại của {name}: {phone_book[name]}")
    else:
        print("Không tìm thấy thông tin cho", name)


def delete_contact():
    global phone_book
    name = input("Nhập tên cần xóa: ")
    if name in phone_book:
        del phone_book[name]
        print(f"Đã xóa {name} khỏi danh bạ.")
    else:
        print("Không tìm thấy thông tin cho", name)


def edit_contact():
    global phone_book
    name = input("Nhập tên cần chỉnh sửa: ")
    if name in phone_book:
        new_phone = input("Nhập số điện thoại mới: ")
        phone_book[name] = new_phone
        print(f"Đã cập nhật số điện thoại cho {name}.")
    else:
        print("Không tìm thấy thông tin cho", name)


def print_menu():
    print("\nDanh bạ điện thoại - Menu:")
    print("1. Thêm mục")
    print("2. Tìm kiếm")
    print("3. Xóa mục")
    print("4. Chỉnh sửa")
    print("5. Thoát")


def main():
    while True:
        print_menu()
        choice = input("Chọn một chức năng (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            print("Kết thúc chương trình.")
            break
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()
