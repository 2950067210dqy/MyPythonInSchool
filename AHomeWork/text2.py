list=eval(input(f"请输入一个列表,格式为[data1,data2,data3.....] :"))
index1=int(input(f"请输入第一个整数:"))
index2=int(input(f"请输入第二个整数:"))
print(f"原列表为{list}")
print(f"子列表为{list[index1:index2]}")