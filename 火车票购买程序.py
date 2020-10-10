price=int(input("请输入单张火车票的全价（1-1000）："))
peopleType=input("是否为学生（Y/N）:")
month=int(input("请输入当前的月份（1-12）:"))
peopleNum=int(input("请输入需要订票的人数："))
if peopleType == "y" or peopleType == "Y":
    if peopleNum >= 10:
        if 1 <= month <= 3 or 7 <= month <= 9:
            print("您应付的金额是：%.1f"%(price * 0.5 * 0.9 * peopleNum))
        else:
            print("您应付的金额是：%.1f" % (price  * 0.9 * peopleNum))
    else:
        if 1 <= month <= 3 or 7 <= month <= 9:
            print("您应付的金额是：%.1f" % (price * 0.5 * peopleNum ))
        else:
            print("您应付的金额是：%.1f" % (price * peopleNum))
elif peopleType == "n" or peopleType == "N":
    if peopleNum >= 10:
        print("您应付的金额是：%.1f" % (price * 0.9* peopleNum))
    else:
        print("您应付的金额是：%.1f" % (price* peopleNum))