# -*- coding: utf-8 -*-

def total(money,changes,index):
    # print money,index

    # bad input or just money become negative which means no solution
    if money < 0:
        return 0

    # change made
    if money == 0:
        return 1
    # not enough changes
    if index == len(changes) and money > 0:
        return 0

    return total(money-changes[index],changes,index) + total(money,changes,index+1)


print total(4,[1,2],0)
