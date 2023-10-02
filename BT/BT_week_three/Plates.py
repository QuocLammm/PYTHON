def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        
def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            if s[2].isdigit() and s[2] != '0':
                for i in range(3, len(s)):
                    if not s[i].isdigit():
                        return False
                return True
    return False

main()
