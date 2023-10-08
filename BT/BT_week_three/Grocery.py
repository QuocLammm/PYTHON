from collections import Counter

def print_grocery_list(grocery_items):
    # Chuyển danh sách thành chữ hoa và sắp xếp theo thứ tự bảng chữ cái
    sorted_grocery_items = sorted(grocery_items, key=lambda x: x.upper())

    # Đếm số lần xuất hiện của mỗi mặt hàng
    item_counts = Counter(sorted_grocery_items)

    # In danh sách tạp hóa
    for item in sorted(set(sorted_grocery_items)):
        print(f"{item_counts[item]:2d} {item.upper()}")

if __name__ == "__main__":
    print("Nhập danh sách các mặt hàng cần mua tại cửa hàng tạp hóa.")
    
    grocery_items = []
    while True:
        try:
            item = input("Nhập mặt hàng (hoặc ấn control-z để kết thúc): ")
            if not item:
                break

            # Chuyển mặt hàng thành chữ hoa và thêm vào danh sách
            item = item.upper()
            grocery_items.append(item)
        except EOFError:
            break

    print("Danh sách tạp hóa:")
    print_grocery_list(grocery_items)
