

#邓亲优20
# a=int(input("请输入第一个整数："))
# b=int(input("请输入第二个整数："))
# c=int(input("请输入第三个整数："))
# if a>b:
#     if a>c:
#         if b>c:
#             print(a,b,c)
#         else:
#             print(a,c,b)
#     else:
#         print(c,a,b)
# else:
#     if a>c:
#         print(b,a,c)
#     else:
#         if b>c:
#             print(b,c,a)
#         else:
#             print(c,b,a)


#邓亲优20
# flag = 1
# for i in range(2, 201):
#     for j in range(2, 201):
#         if i == j:
#             continue
#         if i % j == 0:
#             flag = 0
#             break
#     if flag == 1:
#         print(i,end=",")
#     flag = 1
# 求素数
flag=1
for i in range(100, 1000):
    for j in range(2, 1000):
        if(i==j):
            continue
        if i%j==0:
            flag=0
            break
    if flag==1:
        print(i,end=",")
    flag=1
























