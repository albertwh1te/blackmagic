# coding:utf-8


def limit_fun_times(func):
    def _wrapper():
        i = 0
        if i < 10:
            func
            print "now render {func_name} {render_time} times".format(
                                                            func_name=func.__name__, 
                                                            render_time=i
            )
            i += 1
    return _wrapper

@limit_fun_times
def test_func():
    print "hi"

test_func()
#  a = map(test_func,[1,2,3])
    
