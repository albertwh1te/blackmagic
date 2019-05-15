def permutation(array: list, start: int, end: int, results: list) -> list:
    if start == end:
        results.append("".join(array))
    else:
        for i in range(start, end + 1):
            array[start], array[i] = array[i], array[start]
            permutation(array, start + 1, end, results)
            # backtrack
            array[start], array[i] = array[i], array[start]
    return results


def middle_permutation(string):
    #your code here
    strings = permutation(list(string), 0, len(string) - 1, [])
    return strings[int(len(strings) / 2)]


import time
start = time.time()
print(middle_permutation("abc"))
print(time.time() - start)
