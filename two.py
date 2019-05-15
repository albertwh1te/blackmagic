def checkReverseEqual(s1, s2):
    return s2 in s1 + s1


print(checkReverseEqual("abb", "bab"))
print(checkReverseEqual("abbcc", "ccabb"))
print(checkReverseEqual("abbdcc", "ccadbb"))
