def my_string(my_list, sep=', '):
    return sep.join(my_list)

my_list = ["item1", "item2", "item3", "item4"]
list_string = my_string(my_list, sep=', ')
print (list_string)
