def remove(text):
    text = text.lower() #Không phân biệt chữ hoa và chữ thường
    #Xóa nguyên âm 
    vote = "aeiou"
    text_vote = ''.join([char for char in text if char not in vote])
    return text_vote

def main():
    a = input("Nhập chuỗi:")
    b = remove(a)
    print("Chuỗi sau khi đã xóa nguyên âm:", b)
    
main()
    