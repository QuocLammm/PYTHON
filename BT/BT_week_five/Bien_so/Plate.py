def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        
def is_valid(plate):
    if 2 <= len(plate) <= 6:
        if plate[0].isalpha() and plate[1].isalpha():
            if plate[2].isdigit() and plate[2] != '0':
                for i in range(3, len(plate)):
                    if not plate[i].isdigit():
                        return False
                return True
    return False

if __name__ == "__main__":
    main()
