#使用递归来判断一个单词是否是回文单词
def demo(word):
    if word=='':
        print("是回文单词")
        return
    word=word.lower()
    if word[0]==word[len(word)-1:len(word)]:
        demo(word[1:len(word)-1])
    else:
        print("不是回文单词")

demo("lssmdfsl")