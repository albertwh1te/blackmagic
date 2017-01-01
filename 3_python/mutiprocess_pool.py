from multiprocessing import Pool

def  f(x):
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=10)              # start 4 worker processes
    # result = pool.apply_async(f, [x for x in range(10)])    # evaluate "f(10)" asynchronously
    # print(result.get(timeout=1))           # prints "100" unless your computer is *very* slow
    result = pool.map_async(f, range(10))
    print(result.get(timeout=1))           # prints "100" unless your computer is *very* slow
