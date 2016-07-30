# def solution():
#     pos = neg = zero = 0
#     for i in arr:
#         if i > 0:
#             pos += 1
#         elif i == 0:
#             zero += 1
#         else:
#             neg += 1
#     print("%6.6f" % (float(pos)/float(n)))
#     print("%6.6f" % (float(zero)/float(n)))
#     print("%6.6f" % (float(neg)/float(n)))
# n = 4    
# def solution():
#     for i in xrange(n):
#         print ' ' * (n-1) + '#' * i 
#     return True
# 
# solution()
time = "12:05:45AM"
def solution():
    true_time  = time[:-2]
    [hh, mm, ss] = true_time.split(':')
    if "PM" in time:
        if int(hh) == 12:
            hh = "00"
        else:
            hh = str(int(hh) + 12)
    print ":".join([hh, mm, ss])
    return True
solution()

