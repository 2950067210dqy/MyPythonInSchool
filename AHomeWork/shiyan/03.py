# from random import  random
# times=int(input("请输入投飞镖次数:"))
# hits=0
# for i in range(times):
#     x=random()
#     y=random()
#     if x*x+y*y<=1:
#         hits+=1
# print(4.0*hits/times)

# s=input('x,y,z=')
# x,y,z=s.split(',')
# if x>y:
#     x,y=y,x
# if x>z:
#     x,z=z,x
# if y>z:
#     y,z=z,y
# print(x,y,z)

# height,weight=eval(input("身高体重[,]"))
# bmi = (weight)/(pow(height,2))
# print(bmi)
# print("BMI 数值为:{:.2f}".format(bmi))


# sum=0
# for i in range(1,100,2):
#     sum+=i


n = int(input())
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()