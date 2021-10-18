# num=input('请输入一个自然数：')
# print(sum(map(int,num)))

# setA = eval(input('请输入一个集合：'))
# setB = eval(input('请输入一个集合：'))
# print('交集：',setA & setB)
# print('并集：',setA | setB)
# print('差集：',setA - setB)

# num = int(input('请输入一个自然数：'))
# print('二进制：',bin(num))
# print('八进制：',oct(num))
# print('十六进制：',hex(num))


#
# bill=float(input('Enter amount of bill:'))
# tip=bill*0.15
# if tip <2:
#     tip=2
# print('Tip is ${0:,.2f}'.format(tip))

# li = ["www","old","boy","edu"]
# li.append("com")
# print(li)

# li = ["www","old","boy"]
# li.extend(["edu","com"])
# print(li)

# li = ["www","old","boy","edu","com"]
# obj =li.pop()
# print(obj)

# li = ["www","old","boy","edu","com"]
# obj =li.remove("old")
# print(li)

# li = ["www","old","boy","edu","com"]
# del li
# print(li)

# li = ["www","old","boy","edu","com"]
# li.clear()
# print(li)

# li = ["old","boy","edu","com"]
# li.insert(0,'www')
# print(li)

# a_turple=(1,2,3,4,5)
# for num in a_turple:
#     print(num,end="  ")

li = ["www","old","boy","edu","com"]
print(li.index("edu"))