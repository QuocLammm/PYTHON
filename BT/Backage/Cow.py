import cowsay
import sys
if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
# muốn chạy được chương trình cần vào 
#Window gõ cmd hiện cửa sổ và install gói cowsay vào sau đó chạy đường dẫn file và + 1 chuỗi bất kỳ