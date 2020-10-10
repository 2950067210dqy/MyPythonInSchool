#
# s1=[4,5,6]
# s2=s1
# s1[1]=0
# print(s2)
# #猴子摘桃
# num=1
# for i in range(1,10):
#     num=(num+1)*2
#     print(f"第{10-i}填摘了{num}个桃子")
# print(f"第一天摘了{num}个桃子")
#
# #斐波那契数列
# def getS(n):
#     if n<=1:
#         return 1
#     return getS(n-1)+getS(n-2)
# for i in range(0,20):
#     print(getS(i),end=' ')
# print()
# #200以内的素数
# for i in range(2,201):
#     flag=True
#     for j in range(2,i+1):
#         if i==j:
#             continue
#         if i%j==0:
#             flag=False
#             break
#     if flag:
#         print(i)
# #三个数比大小
# a=int(input("请输入第一个数:"))
# b=int(input("请输入第二个数："))
# c=int(input("请输入第三个数："))
# if a<=b<=c:
#     print(a,b,c)
# elif a<=c<=b:
#     print(a,c,b)
# elif c<=a<=b:
#     print(c,a,b)
# elif c<=b<=a:
#     print(c,b,a)
# elif b<=a<=c:
#     print(b,a,c)
# elif b<=c<=a:
#     print(b,c,a)
# from math import sqrt
# print (sqrt(3)*sqrt(3))
list=['a','b','c','d','e']
print(list[-4:-1:-1])
print(list[:3:2])
# print(list[1:3:0])
print(list['a','d',2])