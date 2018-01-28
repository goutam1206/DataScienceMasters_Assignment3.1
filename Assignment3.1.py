def myreduce(func, lst):
    finalValue = lst[0]
    for val in lst[1:]:
        finalValue = func(finalValue,val)
    return finalValue

def addNums(x,y):
    c = x + y
    return c

redNum = myreduce(addNums,[1,2,3,4])
print (redNum)


def myfilter(func,lst):
    retlst = []
    for val in lst:
        if (func(val)):
            retlst.append(val)
            
    return retlst

def func_filter(num):
    if (num <= 4):
        return True

mylist = myfilter(func_filter,[5,6,3,7,1,2,0,-2])
print (mylist)