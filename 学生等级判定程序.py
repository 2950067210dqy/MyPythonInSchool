#邓亲优20
grade = int(input("请输入您的成绩:"))
while grade<0 or grade>100:
    grade = int(input("对不起您输入的数字不符合要求，请输入您的成绩:"))
if 0<=grade<=59:
    print("您的成绩为：不及格！")
elif 60<=grade<=69:
    print("您的成绩为：及格！")
elif 70<=grade<=79:
    print("您的成绩为：中等！")
elif 80<=grade<=89:
    print("您的成绩为：良好！")
elif 90<=grade<=100:
    print("您的成绩为：优秀！")