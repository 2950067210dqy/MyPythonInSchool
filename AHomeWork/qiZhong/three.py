base1="a"
base2="A"
ruleTable={}
for i in range(26):
    ruleTable[i+1]=(chr(int(ord(base1))+i),chr(int(ord(base2))+i))
def enerypt(text="",num=1):
    secret = ""
    for i in text:
        if i==" ":
            secret+=i
        else:
            for key,values in ruleTable.items():
                for j in range(len(values)):
                    if values[j] == i:
                        newKey = key + num
                        if newKey / 26 > 1:
                            newKey = newKey % 26
                        secret += ruleTable[newKey][j]
    return secret
print("凯撒密码")
secretBefore=input("请输入要进行加密的信息：")
secretNum=int(input("请输入凯撒密码加密的偏移量:"))
print(f"凯撒密码加密前：{secretBefore}")
print(f"凯撒密码(偏移量为{secretNum})加密后：{enerypt(secretBefore,secretNum)}")