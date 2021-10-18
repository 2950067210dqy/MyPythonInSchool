# coding:utf-8
import re
x = input("请输入点的x的坐标")
while not re.match(r'^[0-9./-]*$',x):
    x = input(f"{x}值非法，请重新输入x坐标")
y = input("请输入点的y的坐标 ")
while not re.match(r'^[0-9./-]*$',y):
    x = input(f"{y}值非法，请重新输入y坐标")
x=float(x)
y=float(y)
if x>0 and y>0:
    print(f"（{x},{y}）在第一象限")
if x>0 and y<0:
    print(f"（{x},{y}）在第四象限")
if x<0 and y>0:
    print(f"（{x},{y}）在第二象限")
if x<0 and y<0:
    print(f"（{x},{y}）在第三象限")
if x==0 and y==0:
    print(f"（{x},{y}）在原点(0,0)")
if x==0 and y>0:
    print(f"（{x},{y}）在y轴的正半轴上")
if x==0 and y<0:
    print(f"（{x},{y}）在y轴的负半轴上")
if y==0 and x>0:
    print(f"（{x},{y}）在x轴的正半轴上")
if y==0 and x<0:
    print(f"（{x},{y}）在x轴的负半轴上")