def test(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
def fact(m,n):
    s=1
    for i in range(1,n+1):
        s=s*m
    return m,n,s
def calculateNum(num):
    result=0
    i=1
    while i<=num:
        result=result+i
        i+=1
    return  result
def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=" ")
        a,b=b,a+b
    print()
def main():
    numbers=[865,1169,1208,1243,329]
    numbers.sort(key=sumofOddDigits,reverse=True)
    print('sorted by sum of odd digits:')
    print(numbers)
def sumofOddDigits(num):
    listNums=list(str(num))
    total=0
    for i in range(len(listNums)):
        if int(listNums[i])%2==1:
            total+=int(listNums[i])
    return total
def demo(*para):
    avg=sum(para)/len(para)
    g=[i for i in para if i>avg]
    return (avg,)+tuple(g)
print(demo(1,2,3,4))