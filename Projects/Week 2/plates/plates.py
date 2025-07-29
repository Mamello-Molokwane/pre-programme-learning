def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    count = 0
    punc = [' ', '.', ',', '-']
    if s[:2].isalpha() and 2 <= len(s) <= 6:
        for i in s:
            if i.isdigit():
                count += 1
                if i == '0' and count == 1:
                    count = 0
                    return False
                if s[-2].isalpha():
                    return False
            elif i in punc:
                return False
    else:
         return False
    return True

main()
