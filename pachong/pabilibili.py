import threading
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
def allorderby(link,table,counter,db):
    print(21)
    db = pymysql.connect(host="47.94.164.171", port=3306, user="root", password="2591215997as", database=f'{db}', charset='utf8')
    cursor = db.cursor()  # 数据游标
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    r = requests.get(link, headers=headers)
    # print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
    num_list = soup.find_all("div", class_="num")
    name_list = soup.find_all("div", class_="info")
    else_num_list = soup.find_all("span", class_="data-box")
    addre_list = soup.find_all("div", class_="img")
    up_addre_list=soup.find_all("div",class_="detail")
    score_list = soup.find_all("div",class_="pts")
    flag = 0
    id = 1501
    for i in range(0, len(num_list)):
        num = num_list[i].text.strip()
        name = name_list[i].a.text.strip()
        addre = addre_list[i].find('a')
        addr = addre['href']
        # s = requests.get(addr, headers=headers)
        # soup = BeautifulSoup(s.text, 'lxml')
        # fance_num= soup.find_all("div",class_="default-btn follow-btn b-gz not-follow")
        # if(len(fance_num)==0):
        #     fance="暂无数据(团队创作)"
        # else:
        #     fance_num=fance_num[0].find('span')
        #     fance_num=fance_num.find('span')
        #     fance=fance_num.text
        vidieo_num = else_num_list[flag].text.strip()
        flag += 1
        # string = string + "第" + num + "名:视频名称为：" + name + ";播放量为:" + vidieo_num + ";弹幕量为:"
        bullet_num = else_num_list[flag].text.strip()
        flag += 1
        # string = string + bullet_num + ";up主为："
        up = else_num_list[flag].text.strip()
        flag += 1
        # string = string + up + ";\n"
        up_addre=up_addre_list[i].find('a')
        upaddr=up_addre['href']
        upaddr="https:"+upaddr
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(upaddr)
        b = driver.page_source
        # print(b)
        soup = BeautifulSoup(b, 'lxml')
        # a = soup.find_all("div", class_="n-statistics")
        a = soup.find_all("a", class_="n-data n-fs")
        if(len(a)==0):
            fance="暂未获取到数据"
        else:
            fance= a[0]['title']
        print(fance)
        driver.quit()
        score=score_list[i].div.text.strip()
        try:
            # table=MySQLdb.escape_string(table)
            # num = MySQLdb.escape_string(num)
            # name= MySQLdb.escape_string(name)
            # vidieo_num=MySQLdb.escape_string(vidieo_num)
            # bullet_num=MySQLdb.escape_string(bullet_num)
            # up=MySQLdb.escape_string(up)
            # im=MySQLdb.escape_string(im)
            # 执行sql语句
            # sql = f'insert into {table} values ({id},%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            sql = f'update {table} set num=%s,title=%s,play_num=%s,bul_num=%s,author=%s,video_addre=%s,score=%s,up_addre=%s,fance=%s where id = {id}'
            print(cursor.execute(sql,(num,name, vidieo_num, bullet_num, up, addr,score,upaddr,fance)))
            print(f"视频抓取成功")
            id += 1
            # 提交到数据库执行
        except:
             # 发生错误时回滚
            db.rollback()
            print(f"视频出错！  "+sql)

    db.commit()
    db.close()
    # print(string)

def allfanju(link,table,counter,db):
    db = pymysql.connect(host="47.94.164.171", port=3306, user="root", password="2591215997as", database=f'{db}', charset='utf8')
    cursor = db.cursor()  # 数据游标


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    r = requests.get(link, headers=headers)
    # print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
    num_list = soup.find_all("div", class_="num")
    name_list = soup.find_all("div", class_="info")
    allnum_list=soup.find_all("div",class_="pgc-info")
    else_num_list = soup.find_all("span", class_="data-box")
    addre_list = soup.find_all("div", class_="img")
    score_list = soup.find_all("div", class_="pts")
    flag = 0
    id = 1501
    for i in range(0, len(num_list)):
        num = num_list[i].text.strip()
        name = name_list[i].a.text.strip()
        allnum=allnum_list[i].text.strip()
        addre = addre_list[i].find('a')
        addr = addre['href']
        vidieo_num = else_num_list[flag].text.strip()
        flag += 1
        # string = string + "第" + num + "名:视频名称为：" + name + ";播放量为:" + vidieo_num + ";弹幕量为:"
        bullet_num = else_num_list[flag].text.strip()
        flag += 1
        # string = string + bullet_num + ";up主为："
        shoucang = else_num_list[flag].text.strip()
        flag += 1
        # string = string + up + ";\n"
        score = score_list[i].div.text.strip()
        try:
            # table=MySQLdb.escape_string(table)
            # num = MySQLdb.escape_string(num)
            # name= MySQLdb.escape_string(name)
            # vidieo_num=MySQLdb.escape_string(vidieo_num)
            # bullet_num=MySQLdb.escape_string(bullet_num)
            # up=MySQLdb.escape_string(up)
            # im=MySQLdb.escape_string(im)
            # 执行sql语句
            # sql = f'insert into {table} values ({id},%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            # print(sql)
            sql = f'update {table} set num=%s,title=%s,all_num=%s,play_num=%s,bul_num=%s,shoucang_num=%s,video_addre=%s,score=%s where id = {id}'
            print(cursor.execute(sql, (num, name,allnum, vidieo_num, bullet_num, shoucang, addr, score)))
            print(f"番剧电影抓取成功")
            id += 1
            # 提交到数据库执行
        except:
             #发生错误时回滚
             db.rollback()
             print(f"番剧电影出错！  " + sql)

    db.commit()
    db.close()
    # print(string)

# def print_time(delay, counter):
#     while counter:
        #爬取一天的
time1=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(time1)
allorderby(link = "https://www.bilibili.com/ranking/all/0/0/1",table="bili",counter=100000,db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/1/0/1", table="cu_bili", counter=100000,db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/168/0/1", table="guochuang_bili", counter=100000,db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/3/0/1", table="music_bili", counter=100000,db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/129/0/1", table="dance_bili", counter=100000,db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/4/0/1", table="game_bili", counter=100000,db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/36/0/1", table="tec_bili", counter=100000,db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/188/0/1", table="shuma_bili", counter=100000,db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/160/0/1", table="life_bili", counter=100000,db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/119/0/1", table="guicu_bili", counter=100000,db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/155/0/1", table="fashion_bili", counter=100000,db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/5/0/1", table="yule_bili", counter=100000,db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/181/0/1", table="video_bili", counter=100000,db="bilibili")

allfanju(link="https://www.bilibili.com/ranking/bangumi/13/0/1", table="fanjuvideo_bili", counter=100000,db="bilibili")
allfanju(link="https://www.bilibili.com/ranking/bangumi/167/0/1", table="guo_fanjuvideo_bili", counter=100000,db="bilibili")

allfanju(link="https://www.bilibili.com/ranking/cinema/177/0/1", table="jilupian_bili", counter=100000,db="bilibili")
allfanju(link="https://www.bilibili.com/ranking/cinema/23/0/1", table="movie_bili", counter=100000,db="bilibili")
allfanju(link="https://www.bilibili.com/ranking/cinema/11/0/1", table="dianshiju_bili", counter=100000,db="bilibili")
print("-"*20+"爬取1天的完成"+"-"*20)

        #爬取7天的
allorderby(link="https://www.bilibili.com/ranking/all/0/0/7", table="bili", counter=100000, db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/1/0/7", table="cu_bili", counter=100000, db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/168/0/7", table="guochuang_bili", counter=100000,
                   db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/3/0/7", table="music_bili", counter=100000, db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/129/0/7", table="dance_bili", counter=100000,
                   db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/4/0/7", table="game_bili", counter=100000, db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/36/0/7", table="tec_bili", counter=100000, db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/188/0/7", table="shuma_bili", counter=100000,
                   db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/160/0/7", table="life_bili", counter=100000,
                   db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/119/0/7", table="guicu_bili", counter=100000,
                   db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/155/0/7", table="fashion_bili", counter=100000,
                   db="7bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/5/0/7", table="yule_bili", counter=100000, db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/181/0/7", table="video_bili", counter=100000,
                   db="7bilibili")

allfanju(link="https://www.bilibili.com/ranking/bangumi/13/0/7", table="fanjuvideo_bili", counter=100000,
                 db="7bilibili")
allfanju(link="https://www.bilibili.com/ranking/bangumi/167/0/7", table="guo_fanjuvideo_bili", counter=100000,
                 db="7bilibili")

allfanju(link="https://www.bilibili.com/ranking/cinema/177/0/7", table="jilupian_bili", counter=100000,
                 db="7bilibili")
allfanju(link="https://www.bilibili.com/ranking/cinema/23/0/7", table="movie_bili", counter=100000,
                 db="7bilibili")
allfanju(link="https://www.bilibili.com/ranking/cinema/11/0/7", table="dianshiju_bili", counter=100000,
                 db="7bilibili")
print("-" * 20 + "爬取3天的完成" + "-" * 20)
        #爬3天的
allorderby(link="https://www.bilibili.com/ranking/all/0/0/3", table="bili", counter=100000, db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/1/0/3", table="cu_bili", counter=100000, db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/168/0/3", table="guochuang_bili", counter=100000,
                   db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/3/0/3", table="music_bili", counter=100000, db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/129/0/3", table="dance_bili", counter=100000,
                   db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/4/0/3", table="game_bili", counter=100000, db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/36/0/3", table="tec_bili", counter=100000, db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/188/0/3", table="shuma_bili", counter=100000,
                   db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/160/0/3", table="life_bili", counter=100000,
                   db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/119/0/3", table="guicu_bili", counter=100000,
                   db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/155/0/3", table="fashion_bili", counter=100000,
                   db="3bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/5/0/3", table="yule_bili", counter=100000, db="bilibili")
allorderby(link="https://www.bilibili.com/ranking/all/181/0/3", table="video_bili", counter=100000,
                   db="3bilibili")

allfanju(link="https://www.bilibili.com/ranking/bangumi/13/0/3", table="fanjuvideo_bili", counter=100000,
                 db="3bilibili")
allfanju(link="https://www.bilibili.com/ranking/bangumi/167/0/3", table="guo_fanjuvideo_bili", counter=100000,
                 db="3bilibili")

allfanju(link="https://www.bilibili.com/ranking/cinema/177/0/3", table="jilupian_bili", counter=100000,
                 db="3bilibili")
allfanju(link="https://www.bilibili.com/ranking/cinema/23/0/3", table="movie_bili", counter=100000,
                 db="3bilibili")
allfanju(link="https://www.bilibili.com/ranking/cinema/11/0/3", table="dianshiju_bili", counter=100000,
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


