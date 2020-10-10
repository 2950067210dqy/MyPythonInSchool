#邓亲优 20
word="2020,中国,China,欢迎您!"
e=0
m=0
p=0
c=0
for i in range(0,len(word)):
    if (ord(word[i]) >=97 and ord(word[i]) <=122) or (ord(word[i]) >=65 and ord(word[i]) <=90):
        e+=1
    elif ord(word[i]) >=48 and ord(word[i]) <=57 :
        m+=1
    elif ord(word[i]) >=128:
        c+=1
    elif ( ord(word[i]) >=32 and ord(word[i]) <=47) or ( ord(word[i]) >=58 and ord(word[i]) <=64) or\
        ( ord(word[i]) >=91 and ord(word[i]) <=96) or( ord(word[i]) >=123 and ord(word[i]) <=126):
        p+=1
print(f"这句话共有英文字符{e}个，数字{m}个，标点符号{p}个,汉字{c}个")

