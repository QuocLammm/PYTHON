import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def validate_date(date_str):
    # Kiểm tra định dạng ngày: tháng-ngày-năm hoặc tên tháng ngày, năm
    pattern1 = re.compile(r"\d+/\d+/\d+")
    pattern2 = re.compile(r"(\w+) (\d+), (\d+)")
    
    if pattern1.match(date_str):
        return True
    elif pattern2.match(date_str):
        return True
    else:
        return False

def convert_to_yyyy_mm_dd(date_str):
    # Tách thông tin ngày, tháng, năm từ chuỗi đầu vào
    if '/' in date_str:
        month, day, year = map(int, date_str.split('/'))
    else:
        match = re.match(r"(\w+) (\d+), (\d+)", date_str)
        month = months.index(match.group(1)) + 1
        day = int(match.group(2))
        year = int(match.group(3))
    
    return f"{year:04d}-{month:02d}-{day:02d}"

if __name__ == "__main__":
    while True:
        date_str = input("Nhập ngày (hoặc ấn Enter để kết thúc): ")

        if not date_str:
            break

        if validate_date(date_str):
            formatted_date = convert_to_yyyy_mm_dd(date_str)
            print(formatted_date)
        else:
            print("Ngày không hợp lệ. Vui lòng nhập lại.")
