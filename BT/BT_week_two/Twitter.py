#hãy triển khai một chương 
#trình nhắc người dùng nhập một str văn bản và sau đó xuất ra cùng một văn bản 
#nhưng bỏ qua tất cả các nguyên âm (A, E, I, O và U), cho dù được nhập bằng chữ
#hoa hay chữ thường

def remove(text):
    text = text.lower() #Không phân biệt chữ hoa và chữ thường
    #Xóa nguyên âm 
    vote = "aeiou"
    text_vote = ''.join([char for char in text if char not in vote])
    return text_vote

def main():
    a = input("Input:")
    b = remove(a)
    print("Output:", b)
    
main()
    