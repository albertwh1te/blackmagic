def isPP(n):
    """
    m**k = n
    """
    #your code here
    ori = n
    m = 2
    while m <= pow(ori, 0.5):
        n = ori
        k = 0
        while n % m == 0:
            k = k + 1
            n /= m
            if n == 1:
                return [m, k]
        m += 1
    return None
