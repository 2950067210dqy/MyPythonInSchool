# def make_story():
#     f=open('story.txt','w')
#     f.write('Marry had a little lamb,\n')
#     f.write('and then she had some more.\n')
#     f.close()
# # make_story()
# f=open('story.txt','a')
# f.write('i am songyan')
# f.close()

# fo=open("output.txt","w+")
# ls=["China","France","America"]
# fo.writelines(ls)
# fo.seek(0)
# for line in fo:
#     print(line)
# fo.close()
# fo=open("output.txt","r")
# for line in fo:
#     print(line)
# fo.close()
#
#
# def main():
#     phone={'a':"alpha","b":"bravo","c":"charlie"}
#     while True:
#         try:
#             letter=input("Enter a,b, or c:")
#             print(phone[letter])
#             break
#         except KeyError:
#             print("ssssssss")
# import turtle
# t=turtle.Pen()
# t.reset()
# for x in range(1,38):
#     t.forward(100)
#     t.left(175)
f=open('output.txt','r')
content=f.readline()
print(f"1.{content}")
content=f.readline()
print(f"2.{content}")
content=f.readline()
print(f"3.{content}")
f.close()