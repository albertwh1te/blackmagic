def searchlist(x,alist):
        end=int(len(alist)-1)
        mid=int(len(alist)/2)

        while len(alist)>2:
                if  x==alist[mid] or x==alist[0] or x==alist[end] :
                        return("true")
                        break
                elif x>alist[mid]:
                        alist=alist[mid:]
                        mid=int(len(alist)/2)
                        end=int(len(alist)-1)


                elif x<alist[mid]:
                        alist=alist[:mid]
                        mid=int(len(alist)/2)
                        end=int(len(alist)-1)

                else:
                        return("false")

aList=[2,3,5,7,9,12,14,23,34,45,67,89,101]

xnum=int(input("enter a number:"))
searchlist(xnum,aList)
print(searchlist(xnum,aList))
