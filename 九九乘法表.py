#邓亲优20
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,i*j),end=" ")
    for k in range(1,10-i):
        print(end=" ")
    print()