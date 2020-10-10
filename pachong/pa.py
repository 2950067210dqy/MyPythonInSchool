import threading
from asyncio import sleep

from selenium import webdriver
import pymysql
import requests
import _thread
import time
from bs4 import BeautifulSoup


# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print("开始线程：" + self.name)
#         print_time(self.counter, 100000)
#         print("退出线程：" + self.name)
def getDB(host,port,user,password,database,charset):
    db = pymysql.connect(host=host, port=port, user=user, password=password, database=database,
                         charset=charset)
    return db
def getCursor(db):
    cursor = db.cursor()  # 数据游标
    return cursor
def executeSQL(cursor,sql,num,name,video_num, bullet_num, up, addr, score, upaddr, fance,im):
    print(cursor.execute(sql, (num, name,video_num, bullet_num, up, addr, score, upaddr, fance,im)))
def getSoup(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "Content-Type" : "text/plain;charset=UTF-8",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection" : "keep-alive"

    }
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup
def getDriver(link):
    #不打开浏览器后台运行
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(chrome_options=option)
    #打开浏览器
    # driver = webdriver.Chrome(r'chromedriver.exe')

    driver.get(link)
    k=1
    for i in range(1150):
        driver.execute_script(f'window.scrollTo({k}, {k+10})')  # 竖直滑动，scrollHeight一屏高度
        k=k+10
    return driver
def getDefaultDriver(link):
    # 不打开浏览器后台运行
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)
    # 打开浏览器
    # driver = webdriver.Chrome(r'chromedriver.exe')
    driver.get(link)
    return driver
def CloseDriver(driver):
    driver.quit()
def getDriverSoup(driver):
    b = driver.page_source
    soup = BeautifulSoup(b, 'lxml')
    return soup
# def getLenNumList(soup):
#     num_list = soup.find_all("div", class_="num")
#     return len(num_list)
# def getNumList(soup):
#     num_list = soup.find_all("div", class_="num")
#     return num_list
# def getNameList(soup):
#     name_list = soup.find_all("div", class_="info")
#     return name_list
# def getElseNumList(soup):
#     else_num_list = soup.find_all("span", class_="data-box")
#     return else_num_list
# def getAddreList(soup):
#     addre_list = soup.find_all("div", class_="img")
#     return addre_list
# def getUpAddreList(soup):
#     up_addre_list = soup.find_all("div", class_="detail")
#     return up_addre_list
# def getScoreList(soup):
#     score_list = soup.find_all("div", class_="pts")
#     return score_list
def getNum(numlist,i):
    num = numlist[i].text.strip()
    return num
def getName(namelist,i):
    name = namelist[i].a.text.strip()
    return name
def getAddr(addrelist,i):
    addre = addrelist[i].find('a')
    addr = addre['href']
    return addr
def getElseNum(elsenumlist,i):
    else_num = elsenumlist[i].text.strip()
    return else_num
def getUpAddre(up_addre_list,i):
    up_addre = up_addre_list[i].find('a')
    upaddr = up_addre['href']
    upaddr = "https:" + upaddr
    return upaddr
def getScore(score_list,i):
    score = score_list[i].div.text.strip()
    return score

def allorderby(link,table,db):
    db=getDB("47.94.164.171",3306,"root","2591215997as",f'{db}','utf8')
    cursor=getCursor(db)
    soup=getSoup(link)
    num_list = soup.find_all("div", class_="num")
    name_list = soup.find_all("div", class_="info")
    else_num_list = soup.find_all("span", class_="data-box")
    addre_list = soup.find_all("div", class_="img")
    up_addre_list=soup.find_all("div",class_="detail")
    score_list = soup.find_all("div",class_="pts")

    driver = getDriver(link)
    img_list = getDriverSoup(driver).find_all("div",class_="lazy-img cover")
    CloseDriver(driver)

    id=1501
    flag=0
    for i in range(0,len(num_list)):
        vidieo_num = getElseNum(else_num_list,flag)
        flag += 1
        bullet_num = getElseNum(else_num_list,flag)
        flag += 1
        up = getElseNum(else_num_list,flag)
        flag += 1

        img=img_list[i].find('img')
        im=img['src']

        addr=getAddr(addre_list,i)
        soup = getSoup(addr)
        fance_num= soup.find_all("div",class_="default-btn follow-btn b-gz not-follow")
        if(len(fance_num)==0):
            fance="暂无数据(团队创作)"
        else:
            fance_num=fance_num[0].find('span')
            fance_num=fance_num.find('span')
            fance=fance_num.text





        sql = f'update {table} set num=%s,title=%s,play_num=%s,bul_num=%s,author=%s,video_addre=%s,score=%s,up_addre=%s,fance=%s,img_addre=%s where id = {id}'
        try:
            executeSQL(cursor,sql,getNum(num_list,i),getName(name_list,i),vidieo_num,bullet_num,up,addr,getScore(score_list,i), \
                       getUpAddre(up_addre_list, i),fance,im)
            time2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            print(time2)
            print(f"视频抓取成功{id-1500}")
            id += 1
            # 提交到数据库执行
        except:
            # 发生错误时回滚
            db.rollback()
            time2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            print(time2)
            print(f"视频出错！{id-1500}  " + sql)
    db.commit()
    db.close()

def allfanju(link,table,db):
    db = getDB("47.94.164.171", 3306, "root", "2591215997as", f'{db}', 'utf8')
    cursor = getCursor(db)
    soup = getSoup(link)
    num_list = soup.find_all("div", class_="num")
    name_list = soup.find_all("div", class_="info")
    allnum_list=soup.find_all("div",class_="pgc-info")
    else_num_list = soup.find_all("span", class_="data-box")
    addre_list = soup.find_all("div", class_="img")
    score_list = soup.find_all("div", class_="pts")
    driver = getDriver(link)
    img_list = getDriverSoup(driver).find_all("div", class_="lazy-img cover")
    CloseDriver(driver)
    flag = 0
    id = 1501
    print(soup)
    print(len(num_list))
    for i in range(0, len(num_list)):
        num = num_list[i].text.strip()
        name = name_list[i].a.text.strip()
        allnum=allnum_list[i].text.strip()
        addre = addre_list[i].find('a')
        addr = addre['href']
        vidieo_num = else_num_list[flag].text.strip()
        flag += 1
        bullet_num = else_num_list[flag].text.strip()
        flag += 1
        shoucang = else_num_list[flag].text.strip()
        flag += 1
        score = score_list[i].div.text.strip()

        img = img_list[i].find('img')
        im = img['src']

        try:
            sql = f'update {table} set num=%s,title=%s,all_num=%s,play_num=%s,bul_num=%s,shoucang_num=%s,video_addre=%s,score=%s,img_addre=%s where id = {id}'
            print(cursor.execute(sql, (num, name,allnum, vidieo_num, bullet_num, shoucang, addr, score,im)))
            time2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            print(time2)
            print(f"番剧电影抓取成功!{id}")
            id += 1
            # 提交到数据库执行
        except:
             #发生错误时回滚
             db.rollback()
             time2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
             print(time2)
             print(f"番剧电影出错！{id}  " + sql)
    db.commit()
    db.close()
    # print(string)

# def print_time(delay, counter):
#     while counter:
        #爬取一天的
time1=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(time1)
allorderby(link = "https://www.bilibili.com/ranking/all/0/0/1",table="bili",db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/1/0/1", table="cu_bili", db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/168/0/1", table="guochuang_bili",db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/3/0/1", table="music_bili", db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/129/0/1", table="dance_bili", db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/4/0/1", table="game_bili", db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/36/0/1", table="tec_bili",db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/188/0/1", table="shuma_bili",db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/160/0/1", table="life_bili", db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/119/0/1", table="guicu_bili",db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/155/0/1", table="fashion_bili",db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/5/0/1", table="yule_bili", db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/181/0/1", table="video_bili",db="bilibili")

allfanju(link="https://www.bilibili.com/ranking/bangumi/13/0/1", table="fanjuvideo_bili",db="bilibili")
allfanju(link="https://www.bilibili.com/ranking/bangumi/167/0/1", table="guo_fanjuvideo_bili",db="bilibili")

allfanju(link="https://www.bilibili.com/ranking/cinema/177/0/1", table="jilupian_bili",db="bilibili")
allfanju(link="https://www.bilibili.com/ranking/cinema/23/0/1", table="movie_bili", db="bilibili")
allfanju(link="https://www.bilibili.com/ranking/cinema/11/0/1", table="dianshiju_bili",db="bilibili")
print("-"*20+"爬取1天的完成"+"-"*20)

        #爬取7天的
allorderby(link="https://www.bilibili.com/ranking/all/0/0/7", table="bili", db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/1/0/7", table="cu_bili",db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/168/0/7", table="guochuang_bili",
                   db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/3/0/7", table="music_bili", db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/129/0/7", table="dance_bili",
                   db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/4/0/7", table="game_bili",  db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/36/0/7", table="tec_bili",  db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/188/0/7", table="shuma_bili",
                   db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/160/0/7", table="life_bili",
                   db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/119/0/7", table="guicu_bili",
                   db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/155/0/7", table="fashion_bili",
                   db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/5/0/7", table="yule_bili", db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/181/0/7", table="video_bili",
                   db="7bilibili")

allfanju(link="https://www.bilibili.com/ranking/bangumi/13/0/7", table="fanjuvideo_bili",
                 db="7bilibili")
allfanju(link="https://www.bilibili.com/ranking/bangumi/167/0/7", table="guo_fanjuvideo_bili",
                 db="7bilibili")

allfanju(link="https://www.bilibili.com/ranking/cinema/177/0/7", table="jilupian_bili",
                 db="7bilibili")
allfanju(link="https://www.bilibili.com/ranking/cinema/23/0/7", table="movie_bili",
                 db="7bilibili")
allfanju(link="https://www.bilibili.com/ranking/cinema/11/0/7", table="dianshiju_bili",
                 db="7bilibili")
print("-" * 20 + "爬取3天的完成" + "-" * 20)
        #爬3天的
allorderby(link="https://www.bilibili.com/ranking/all/0/0/3", table="bili",db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/1/0/3", table="cu_bili", db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/168/0/3", table="guochuang_bili",
                   db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/3/0/3", table="music_bili",db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/129/0/3", table="dance_bili",
                   db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/4/0/3", table="game_bili",  db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/36/0/3", table="tec_bili",  db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/188/0/3", table="shuma_bili",
                   db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/160/0/3", table="life_bili",
                   db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/119/0/3", table="guicu_bili",
                   db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/155/0/3", table="fashion_bili",
                   db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/5/0/3", table="yule_bili",  db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/181/0/3", table="video_bili",
                   db="3bilibili")

allfanju(link="https://www.bilibili.com/ranking/bangumi/13/0/3", table="fanjuvideo_bili",
                 db="3bilibili")
allfanju(link="https://www.bilibili.com/ranking/bangumi/167/0/3", table="guo_fanjuvideo_bili",
                 db="3bilibili")

allfanju(link="https://www.bilibili.com/ranking/cinema/177/0/3", table="jilupian_bili",
                 db="3bilibili")
allfanju(link="https://www.bilibili.com/ranking/cinema/23/0/3", table="movie_bili",
                 db="3bilibili")
allfanju(link="https://www.bilibili.com/ranking/cinema/11/0/3", table="dianshiju_bili",
                 db="3bilibili")
print("-" * 20 + "爬取7天的完成，新一轮爬取将在120秒后进行！！" + "-" * 20)

print(time1)
time2=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(time2)


# time.sleep(delay)
# # 创建新线程
#
# thread1 = myThread(1, "Thread-1", 120)
#
# # 开启新线程
# thread1.start()


