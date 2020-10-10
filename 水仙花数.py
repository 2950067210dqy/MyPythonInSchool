#邓亲优20
temp =0
for a in range(10):
    for b in range(10):
        for c in range(10):
             if a**3+b**3+c**3==a*100+b*10+c and 100<=(a*100+b*10+c)<=999 :
                print("水仙花数%d"%(a*100+b*10+c))
                temp+=1
else:
    print(f"共有{temp}个")