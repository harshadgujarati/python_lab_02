li = [24,35,9,56,12]
def myFun(li):
    si=len(li)

    tmp = li[0]
    li[0] = li[si-1]
    li[si-1] = tmp

    return li
print(myFun(li))