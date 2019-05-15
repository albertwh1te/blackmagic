print("This is an app calculate the lenght of a word")


def String_Lenght(word):
    if word.isdigit():
        return "Integers can't be counted"
    elif word.replace(".", "", 1).isdigit():
        return "floats can't be counted"
    else:
        return len(word)


word = input("enter the word")
print(String_Lenght(word))
