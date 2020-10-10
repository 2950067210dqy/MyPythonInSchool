#邓亲优20
for i in range(1,21):
    for j in range(1,34):
        xiaoji =100-i-j
        if xiaoji%3==0 and (5*i+3*j+xiaoji/3) ==100:
            print("公鸡有%d只，母鸡有%d只，小鸡有%d只"%(i,j,xiaoji))
