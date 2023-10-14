def main():
    input_text = input("Input:")
    output_text = shorten(input_text)
    print("Output:", output_text)


def shorten(text):
    # Loại bỏ nguyên âm
    vowels = "aeiouAEIOU"
    text_without_vowels = ''.join([char for char in text if char not in vowels])
    return text_without_vowels


if __name__ == "__main__":
    main()

    
    
#Để kiểm tra các bài kiểm tra của bạn, hãy chạy pytest test_twttr.py. Hãy chắc chắn rằng
#bạn có một bản sao của twttr.py tập tin trong cùng một thư mục. Cố gắng sử dụng các
#phiên bản đúng và không chính xác của twttr.py để xác định mức độ kiểm tra của bạn
#phát hiện ra lỗi:
#• Đảm bảo bạn có phiên bản chính xác của twttr.py. Chạy thử nghiệm của bạn bằng
#cách thực thi pytest test_twttr.py. pytest sẽ cho thấy rằng tất cả các bài kiểm tra
#của bạn đã vượt qua.
#• Sửa đổi phiên bản chính xác twttr.py theo cách có thể tạo ra lỗi. Ví dụ: chương
#trình của bạn có thể nhầm lẫn khi chỉ bỏ sót các nguyên âm viết thường! Chạy thử
#nghiệm của bạn bằng cách thực thi pytest test_twttr.py. pytest sẽ cho thấy rằng ít
#nhất một trong các thử nghiệm của bạn đã thất bại.