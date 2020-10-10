#邓亲优20
money=4000
time=int(input("请输入您要买的飞机票的时间为几月（用1-12表示）"))
sort=int(input("您是否购买头等舱（购买输入1，经济舱输入0）"))
if 5<=time<=10:
    if sort==1:
        print(f"您购买的为头等舱，您的飞机票价格为：{money*0.9}元")
    else:
        print(f"您购买的为经济舱，您的飞机票价格为：{money * 0.75}元")
else:
    if sort == 1:
        print(f"您购买的为头等舱，您的飞机票价格为：{money * 0.6}元")
    else:
        print(f"您购买的为经济舱，您的飞机票价格为：{money * 0.3}元")
