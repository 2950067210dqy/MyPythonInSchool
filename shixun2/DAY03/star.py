j=int(input("请输入您要打印的行数"))
for i in range(7,0,-1):
    if 7-i==j:
        break
    print("@"*(7-i),end="")
    print("*"*(i-(7-i)))