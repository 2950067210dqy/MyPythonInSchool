for i in range(2,201):
    flag = True
    for j in range(2,i+1):
        if j==i:
            continue
        if i%j==0:
            flag=False
            break
    if flag:
        print(i)
