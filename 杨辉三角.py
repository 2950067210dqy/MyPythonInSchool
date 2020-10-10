#邓亲优 20
list1 = [1]
list2 = []
n = 0
while n < 11:
    list2.append(list1)
    list1 = [sum(t) for t in zip([0] + list1, list1 + [0])]
    n += 1
   # [0,1] [1,0]
   # zip函数将上面组成元组
   # （0，1）（1,0）
   #  在运用sum函数
   #  1,1
   #  这就是第二行
   #  [0,1,1][1,1,0]
   #  zip函数将上面组成元组
   #  (0,1)(1,1)(1,0)
   #  在运用sum函数
   #  1,2,1
   #  这就是第三行
   #  [0,1,2,1][1,2,1,0]
   #  zip函数将上面组成元组
   #  (0,1)(1,2)(2,1)(1,0)
   #  在运用sum函数
   #  1,3,3,1
   #  这就是第四行
for i in range(0,len(list2)):
    for j in range(0,len(list2[i])):
        print(list2[i][j],end=" ")
    print()