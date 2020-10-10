#邓亲优 20
list1=["学号","姓名","性别","年龄","英语成绩","思政成绩","Python成绩"]
list2=["201865110210","李天","男",18,90,66,85]
list3=["201865110202","赵琴","女",29,85,87]
list4=["201865110203","王一凡","男","女",20,84,79]
list2[0]="201865110201"
list3[3]=19
list3.append(88)
list4.remove("女")
list4.insert(4,68)
print("-"*30,end=" 完善后的成绩如下 ")
print("-"*30)
alllist=[list1,list2,list3,list4]
for i in range(0,len(alllist)):
   print(alllist[i])
english=[list2[4],list3[4],list4[4]]
think=[list2[5],list3[5],list4[5]]
python=[list2[6],list3[6],list4[6]]
print("英语的平均分为：%.1f"%(sum(english)/len(english)))
print("思政的平均分为：%.1f"%(sum(think)/len(think)))
print("python的平均分为：%.1f"%(sum(python)/len(python)))


