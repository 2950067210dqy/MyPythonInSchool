#邓亲优20
fish = 1
while True:
    total, enough = fish, True
    for i in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print('总共有%d条鱼'%fish)
        break
    fish += 1
