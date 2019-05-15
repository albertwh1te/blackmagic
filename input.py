def isnumber(s):
    if s.isdigit() and len(s) <= 9:
        return True
    else:
        print('you should input number and length less than 9')
        return False


def main():
    s = ""
    while not isnumber(s):
        s = input('What is your number')
    print("your number is", s)


if __name__ == "__main__":
    main()