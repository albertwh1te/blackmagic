#!/usr/bin/python3
# coding:utf-8


class test_del():
    def __init__(self, name):
        self.name = name
        print("my name is %s" % self.name)

    def __del__(self):
        print("%s has been deleted" % self.name)


if __name__ == '__main__':
    dd = test_del("bobo")
    del dd
