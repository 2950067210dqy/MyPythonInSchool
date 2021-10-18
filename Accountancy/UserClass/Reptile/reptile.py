import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from Accountancy.UserClass.POJO.comment import comment
from Accountancy.UserClass.IO.commentIO import commentIO
import re
class reptile():
    searchAdress='https://search.douban.com/movie/subject_search?search_text='
    suf="comments?start="
    page=0
    AllWordsByUrl=[]
    headers = {
        #"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/91.0.4472.101"
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        }
    urlList=[]
    allnums=0
    getnumflag=True
    def __init__(self,urlList=''):
        self.ChangeURL(urlList=urlList)
    def getWebSites(self,videoname):
        newUrlList = []
        for i in videoname:
            atmptAdress=self.searchAdress+i
            newUrlList.append(self.getHTMLWithVideoName(atmptAdress, self.headers)+self.suf)
            pass
        return newUrlList
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
            while self.getHTML(i+str(self.page),self.headers):
                self.getHTML(i+str(self.page),self.headers)
        #    返回解析好了的单词(未过滤)
        return self.AllWordsByUrl

    # 根据影视名获得网址
    def getHTMLWithVideoName(self, link, headers):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("window-size=1024,768")
        #driver = webdriver.Chrome("chromedriver", chrome_options=chrome_options)
        driver = webdriver.Chrome(r'chromedriver.exe')
        driver.get(link)
        soup = BeautifulSoup(driver.page_source, "lxml")
        subsoup=soup.find("div", {"class": {"detail"}})
        subsoup2=subsoup.find("a",{"class":{"title-text"}})
        driver.quit()
        return subsoup2['href']
    # 获取网页内容
    def getHTML(self,link,headers):
        HTML = requests.get(link, headers=headers)
        HTML.encoding="utf8"
        HTML=HTML.text
        soup = BeautifulSoup(HTML, 'lxml')
        # 找到body 把body文档树进行lxml解析
        soup=BeautifulSoup(str(soup.find_all('body')), 'lxml')
        return self.getWords(soup=soup)
    # 解析获取的数据
    def getWords(self,soup):
        if self.getnumflag:
            try:
                self.allnums=int(re.findall(r'\d+',\
                    soup.find("ul", {"class": {"fleft","CommentTabs"}}).find("li", {"class": {"is-active"}}).find('span').text)[0])
                if self.allnums>15000:
                    self.allnums=15000
                self.getnumflag=False
            except:
                print(soup)
                print("出现问题")
                return False
        if self.page<self.allnums:
            commentgroup=soup.find_all("div", {"class": {"comment-item"}})
            videoname=soup.find("div",{"id":{"content"}}).find('h1').text[:len(soup.find("div",{"id":{"content"}}).find('h1').text)-3:1]
            print(videoname)
            print(len(commentgroup))
            for i in commentgroup:
                user_addre=i.find("div", {"class": {"avatar"}}).find("a")['href']
                user_img=i.find("div", {"class": {"avatar"}}).find("a").find('img')['src']
                user_name = i.find("span", {"class": {"comment-info"}}).find("a").text
                coment = i.find("p", {"class": {"comment-content"}}).find('span').text
                if len(i.find("span", {"class": {"comment-info"}}).find_all("span")[1]['class'])==1:
                    star=0
                else:
                    star=int(re.findall(r'\d+',i.find("span", {"class": {"comment-info"}}).find_all("span")[1]['class'][0])[0])
                user_agree=i.find("span", {"class": {"votes","vote-count"}}).text
                time=i.find("span", {"class": {"comment-time"}}).text.strip("\n").strip()
                io = commentIO()
                id=io.getMaxId()
                comments = comment(id,user_addre,user_img,user_name,coment,star,user_agree,time,videoname)
                commentsdict=comments.__dict__
                io.comment=commentsdict
                io.insert()
            self.page+=20
            return True
            pass
        else:
            self.page=0
            self.allnums=0
            self.getnumflag = True
            return False
        # newWordsList=[]
        # for i in htmlStrList:
        #     newWordsList=newWordsList+i.split(" ")
        # self.AllWordsByUrl=self.AllWordsByUrl+newWordsList

