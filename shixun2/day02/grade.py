grades = {"VLs": 97}
print("=" * 40)
print("欢迎来到成绩管理系统")
print("1.查询成绩")
print("2.增加成绩")
print("3.修改成绩")
print("4.删除成绩")
print("=" * 40)
s = input("选择你要操作的序号，y键退出")
while s != 'y':
    if s == '1':
        print("...正在查询成绩，请稍后....")
        for key, value in grades.items():
            print(f"查询到的成绩为：{key}:{value},")
        pass
    elif s == '2':
        print("...正在打开增加成绩功能，请稍后...")
        name = input("请输入要添加成绩的学生名字：")
        grade = input(f"请输入（{name}）的成绩")
        isInsert = input(f"您确定要添加（{name}）的成绩吗？Y/N")
        if isInsert == 'Y' or isInsert == 'y':
            grades[name] = grade
            print("插入成功！")
        else:
            print("添加操作取消成功！")
        pass
    elif s == '3':
        print("...正在打开修改成绩功能，请稍后....")
        name = input("请输入要修改的学生名:")
        if name in grades.keys():
            grade = input(f"请输入（{name}）修改之后的成绩")
            isEdit = input(f"您确定要修改（{name}）的成绩吗？Y/N")
            if isEdit == 'Y' or isInsert == 'y':
                grades[name] = grade
                print("修改成功！")
            else:
                print("修改操作取消成功！")
            pass
        else:
            print(f"您要修改的用户({name})不存在！")
    elif s == '4':
        print("...正在打开删除成绩功能，请稍后....")
        name = input("请输入要删除的学生名:")
        isDelete = input(f"您确定要修改（{name}）的成绩吗？Y/N")
        if isDelete == 'Y' or isInsert == 'y':
            grades.pop(name, "您要删除的学生不存在！")
            print("删除成功！")
        else:
            print("删除操作取消成功！")
        pass
        pass
    j = input("是否需要继续操作:y/n")
    if j == 'y' or j == 'Y':
        print("=" * 40)
        print("1.查询成绩")
        print("2.增加成绩")
        print("3.修改成绩")
        print("4.删除成绩")
        print("=" * 40)
        s = input("选择你要操作的序号，y键退出")
        pass
    else:
        s = 'y'
        pass
