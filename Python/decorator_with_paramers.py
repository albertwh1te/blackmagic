# coding:utf-8

def water(func):
    def _wrapper(**kwargs):
        first_name = kwargs.get('first_name', None)
        second_name = kwargs.get('second_name', None)
        print "{first_name} {second_name}'s upper water".format(first_name=first_name,second_name=second_name)
        func(first_name=first_name, second_name=second_name)
        print "{first_name}{second_name}'s bottom water".format(first_name=first_name,second_name=second_name)
    return _wrapper

def shell(func):
    def _wrapper(**kwargs):
        first_name = kwargs.get('first_name', None)
        second_name = kwargs.get('second_name', None)
        print "{first_name} {second_name}'s upper shell".format(first_name=first_name,second_name=second_name)
        func(first_name=first_name, second_name=second_name)
        print "{first_name}{second_name}'s bottom shell".format(first_name=first_name,second_name=second_name)
    return _wrapper

@shell
@water
def origin_one(**kwargs):
    first_name = kwargs.get('first_name', None)
    second_name = kwargs.get('second_name', None)
    print "my name is {first_name} {second_name}".format(first_name=first_name,second_name=second_name)


origin_one(first_name="mark",second_name="wh1te")


    
    

