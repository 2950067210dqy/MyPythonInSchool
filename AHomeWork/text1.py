import random
def init_random_list(size=20,min=0,max=100):
    list=[]
    for i in range(int(size)):
        list.append(random.randint(int(min),int(max)))
    return list
newList=init_random_list()
newListF=newList[0:(len(newList)//2)]
newListB=newList[len(newList)//2:len(newList)]
print(f"原列表为：{newList}")
print(f"前10个元素为{newListF}")
print(f"后10个元素为{newListB}")
newListF.sort(reverse=False)
newListB.sort(reverse=True)
print(f"前10个元素升序排列为{newListF}")
print(f"后10个元素降序排列为{newListB}")
newListF.extend(newListB)
newList=newListF
print(f"排序后列表为：{newList}")