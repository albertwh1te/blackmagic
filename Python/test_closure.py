# coding:utf-8


def test_cleasure():
    a = 6
    b = 10
    def _innter():
        c = 5
        return a + b + c
    return _innter

a = test_cleasure()
print a
print a()
