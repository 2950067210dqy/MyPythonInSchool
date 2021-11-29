# inputstr=input()
# inputstr=inputstr.lower()
# lst=(inputstr).split(' ')
# dit={}
# max=0
# maxkey=""
# for item in lst:
#     if dit.get(item,0):
#         dit[item]=dit[item]+1
#     else:
#         dit[item]=1
#     if dit[item]>max:
#         max=dit[item]
#         maxkey=item
# print(max)
# print(maxkey)
# print(dit)
#
# dict1={'bod':1234,'mike':5678,'john':91011}
# ls=[]
# for i in dict1.items():
#     ls.append(i)
# ls.sort(key=lambda  x:x[1],reverse=True)
# print(ls)

# import string
# import random
# x=string.ascii_letters+string.digits+string.punctuation
# y=[random.choice(x) for i in range(1000)]
# z="".join(y)
# d=dict()
# for ch in z:
#     d[ch]=d.get(ch,0)+1
# print(d)

word=input('Enter a word:')
firstletter=''
secondletter=''
flag=True
for i in range(0,len(word)-1):
    firstletter=word[i]
    secondletter=word[i+1]
    if firstletter>secondletter:
        flag=False
        break
if flag:
    print(1)
else:
    print(2)


# def main():
#     print("Enter the person age group ",end=" ")
#     ageGroup=input('(child,minor,adult,or senior):')
#     print("The admission fee is ",determineAdmissionFee(ageGroup),'dollars.')
# def determineAdmissionFee(ageGroup):
#     dict={'child':0,'minor':5,'adult':10,"senior":8}
#     return dict[ageGroup]
# main()