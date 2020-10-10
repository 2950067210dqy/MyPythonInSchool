#邓亲优 20
list=[1,1]
for i in range(0,18):
    sum=list[i]+list[i+1]
    list.append(sum)
print(list)


def getList(n):
    if(n<=1):
        return 1;
    return getList(n-1)+getList(n-2)
for i in range(0,23):
    print(getList(i))