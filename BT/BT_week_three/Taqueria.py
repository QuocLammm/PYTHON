menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def tt_mon_an(order_items):
    total_cost = 0
    for item in order_items:
        if item in menu:
            total_cost += menu[item]
    return total_cost

if __name__ == "__main__":
    order_items = []
    while True:
        try:
            item = input("Nhập mặt hàng (hoặc ấn Control-z để kết thúc): ")
            if not item:
                break

            # Xử lý trường hợp không phân biệt chữ hoa chữ thường
            item = item.lower().capitalize()

            # Thêm mặt hàng vào đơn hàng nếu nó có trong menu
            if item in menu:
                order_items.append(item)
            else:
                print(f"'{item}' không phải là một mặt hàng hợp lệ.")

            # Tính tổng chi phí và hiển thị
            total_cost = tt_mon_an(order_items)
            print(f"${total_cost:.2f}")
        except EOFError:
            break
        
    print("Cảm ơn bạn đã đặt hàng tại Taqueria!")
