# -*- coding: utf-8 -*-
import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)
        return result

    return timed

@timeit
def test(n):
    time.sleep(n)
    print("i have sleep {} seconds".format(n))
    return n



if __name__ == '__main__':
    test(3)
