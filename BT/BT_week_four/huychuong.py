import re

# Danh sách ánh xạ mã (hoặc bí danh) thành biểu tượng cảm xúc
emoji_map = {
    "thumbs_up": "👍",
    "thumbsdown": "👎",
    "1st_place_medal:": "🥇",
    "2nd_place_medal" : "🥈",
    "3rd_place_medal" : "🥉",
    "ATM_sign" : "🏧",
    "Aquarius" : "♒",
    "Aries" : "♈",
    "BACK_arrow" : "🔙",
    "Christmas_tree" : "🎄",
    "ambulance" : "🚑",
    "anchor" : "⚓",
    "abacus": "🧮",
    # Thêm các ánh xạ khác tại đây
}

def emojize_str(input_str):
    # Sử dụng regular expression để tìm mã (hoặc bí danh) và thay thế thành biểu tượng cảm xúc
    for code, emoji in emoji_map.items():
        input_str = re.sub(re.escape(code), emoji, input_str)

    return input_str

def main():
    user_input = input("Nhập một chuỗi: ")
    emojized_str = emojize_str(user_input)
    print("Biểu tượng cảm xúc của chuỗi là:", emojized_str)

if __name__ == "__main__":
    main()

#Cách test:
#- Chạy chương trình của bạn với python emojize.py. Nhập :1st_place_medal: và nhấn Enter. Chương trình của bạn sẽ xuất ra: Output: icon huy chương vàng
#- Chạy chương trình của bạn với python emojize.py. Nhập :money_bag: và nhấn Enter. Chương trình của bạn sẽ xuất ra: Output: icon túi tiền
#- Chạy chương trình của bạn với python emojize.py. Nhập :smile_cat: và nhấn Enter. Chương trình của bạn sẽ xuất ra: Output: icon mèo cười