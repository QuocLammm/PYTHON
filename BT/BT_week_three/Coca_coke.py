def main():
    # Giá của chai Coca-Cola trong xu
    coke_price = 50
    # Mệnh giá của đồng xu được chấp nhận
    coin = [25, 10, 5]
    # Số tiền còn nợ ban đầu
    t_no = coke_price

    # Nhắc người dùng chèn từng đồng xu
    while t_no > 0:
        user= input("Insert Coin: ")
        # Xử lý lựa chọn đồng xu
        if user:
            coin_s = int(user)
            if coin_s in coin:
                t_no -= coin_s

        # Hiển thị số tiền còn nợ
        print("Amount Due:", max(0, t_no))
    # Xuất số xu mà người dùng đã chèn
    print("Change Owed: ", coke_price - t_no)

main()