import random
name=["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj","kk","ll"]
first=[]
third=[]
second=[]
fouth=[]
for i in range(0,len(name)):
    temp = random.choice(name)
    if(i>=0 and i<=2):
        first.append(temp)
    elif(i>=3 and i<=5):
        second.append(temp)
    elif(i>=6 and i<=8):
        third.append(temp)
    elif(i>=9 and i<=11):
        fouth.append(temp)
    name.remove(temp)
print(first)
print(second)
print(third)
print(fouth)