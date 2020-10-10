apple=6.5
pear=5.5
bana=7.2
count1=float(input("请输入苹果的重量："))
count2=float(input("请输入梨的重量："))
count3=float(input("请输入香蕉的重量："))
print("名称   数量   价格")
print("苹果   {0}k   {1}".format(count1,apple*count1))
print("梨子   {0}k   {1}".format(count2,pear*count2))
print("香蕉   {0}k   {1}".format(count3,bana*count3))
print("总价   {0}".format(apple*count1+pear*count2+bana*count3))