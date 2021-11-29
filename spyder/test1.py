#图形输出 99乘法表
import random

for i in range(9):
    for j in range(i+1):
        print(f"{j+1}x{i+1}={(i+1)*(j+1)}",end=" ")
    print()



print("="*300)



#图形问题 钻石图案
for i in range(3,7):
    print(' '*(6-i),end='')
    print('*'*(2*i+1))#1 3 5 7 9
for i in range(6):
    if i == 5:
        break

    print(' ' * (i+1), end='')
    print('*' * (2 * (5-i)+ 1))


#冒泡排序
def bubbleSort(list):
    length=len(list)
    for i in range(length):
        for j in range(length-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
list=[random.randint(1,100) for i in range(100)]
print(f"before\n{list}")
bubbleSort(list)
print(f"after\n{list}")