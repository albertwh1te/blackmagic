def reverse_vowel(s):
    '''
    >>> reverse_vowel('apple')
    'eppla'
    >>> reverse_vowel('machin')
    'michan'
    '''
    n = list(s)
    first = None
    vowels = ['a','e','i','o','u']
    for d,i in enumerate(n):
        if i in vowels and not first:
            first = i
            first_idx = d
            vowels.remove(i)
        if i in vowels:
            n[d] = first
            n[first_idx] = i
    return "".join(n)
            
        

if __name__ == '__main__':
    s = 'apple'
    print(reverse_vowel(s))
    print(reverse_vowel('machin'))