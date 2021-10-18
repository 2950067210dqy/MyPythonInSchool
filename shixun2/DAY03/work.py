nums=input("请输入一个数")
newNums=""
i=len(nums)-1
while i>=0:
    newNums = newNums + nums[i]
    i=i-1
# for i in range(len(nums)-1,-1,-1):
#     newNums=newNums+nums[i]
print(newNums)