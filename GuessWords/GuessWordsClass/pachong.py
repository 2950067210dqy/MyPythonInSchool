import requests
from bs4 import BeautifulSoup
import re
class pachong:
    AllWordsByUrl=[]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    urlList=[]
    def __init__(self,urlList):
        self.ChangeURL(urlList=urlList)
    # 网址自动添加https://或http://
    def ChangeURL(self,urlList):
        newUrlList=[]
        for i in urlList:
            if i[:8]!="https://" and i[:7]!="http://":
                newUrlList.append("https://"+i)
            else:
                newUrlList.append(i)
        self.urlList = newUrlList
    #  开始爬网页
    def start(self):
        for i in self.urlList:
            self.getHTML(i,self.headers)
        #    返回解析好了的单词(未过滤)
        return self.AllWordsByUrl
    # 获取网页内容
    def getHTML(self,link,headers):
        HTML = requests.get(link, headers=headers)
        HTML.encoding="utf8"
        HTML=HTML.text
        soup = BeautifulSoup(HTML, 'lxml')
        # 找到body 把body文档树进行lxml解析
        soup=BeautifulSoup(str(soup.find_all('body')), 'lxml')
        # 找到文档中的字符串内容
        htmlStrList=soup.find_all(text=re.compile("[a-zA-Z]"))
        self.getWords(htmlStrList=htmlStrList)
    # 解析获取的数据
    def getWords(self,htmlStrList):
        newWordsList=[]
        for i in htmlStrList:
            newWordsList=newWordsList+i.split(" ")
        self.AllWordsByUrl=self.AllWordsByUrl+newWordsList

