def get_fruit_calories(fruit):
    # Tạo một từ điển liên kết trái cây với lượng calo
    fruit_calories = {
        'apples':130,
        'avocados':50,
        'bananas':105,
        'cantaloupes':50,
        'grapefruits':60,
        'honeydew Melons':50,
        'kiwifriuts':90,
        'lemons':15,
        'limes':20,
        'nectarines':60,
        'oranges':80,
        'peachs':60,
        'pears':100,
        'pineapples':50,
        'plums':70,
        'strawberries':50,
        'sweet Cherries':100,
        'tangerines':50,
        'watermelons':80,
    }

    # Chuyển đổi loại trái cây thành chữ thường để phù hợp với từ điển
    fruit = fruit.lower()

    # Kiểm tra xem loại trái cây có trong từ điển không
    if fruit in fruit_calories:
        return fruit_calories[fruit]
    else:
        return None

def main():
    fruit = input("Nhập loại trái cây: ")
    calories = get_fruit_calories(fruit)
    
    # Xuất kết quả
    if calories is not None:
        print(f"Số lượng calo trong một phần {fruit} là: {calories} calo.")
    else:
        print("Không tìm thấy thông tin calo cho loại trái cây này.")
main()
