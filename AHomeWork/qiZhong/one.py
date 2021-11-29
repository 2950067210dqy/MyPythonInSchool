

def deleteFtoSentence(sentence):
    newWords=""
    for i in sentence:
        if i!="r" and i!="R":
            newWords=newWords+i
    return newWords
Words=input("请输入一句话（英文）：")
print(f"用户输入的句子为：{Words}")
print(f"处理过后的句子为：{deleteFtoSentence(Words)}")