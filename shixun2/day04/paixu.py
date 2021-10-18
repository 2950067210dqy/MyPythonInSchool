

def maopao(numlist=[]):
    for i in range(len(numlist)-1):
        for j in range(len(numlist)-i-1):
            if numlist[j]>numlist[j+1]:
                t=numlist[j]
                numlist[j]=numlist[j+1]
                numlist[j+1]=t

num=[3,2,6,1,3,8,0,23]
maopao(num)
print(num)