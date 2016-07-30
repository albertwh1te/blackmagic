# coding:utf-8

def test_yield(test_list):
    for x in test_list:
        yield x * x


cc  = test_yield(range(1,10))
for w in cc:
    print w 
