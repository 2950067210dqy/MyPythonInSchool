import random
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import aiohttp
import asyncio
import time
from time import sleep
import pymysql
# 开始时间
t1 = time.time()
print('#' * 50)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
# url = "http://www.wikidata.org/w/index.php?title=Special:WhatLinksHere/Q5&limit=500&from=0"
# # 请求头部
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
# # 发送HTTP请求
# req = requests.get(url, headers=headers)
# # 解析网页
# soup = BeautifulSoup(req.text, "lxml")
# # 找到name和Description所在的记录
# human_list = soup.find(id='mw-whatlinkshere-list')('li')
productsBoy={'boy_yurongfu':'羽绒服','boy_jiake':'夹克','boy_xifu':'西服套装','boy_txue':'T恤','boy_xiuxianku':"休闲裤"}
productsGirl={'girl_lianyiqun':'连衣裙','girl_banshenqun':'半身裙','girl_duanwaitao':'短外套','girl_xiaoxizhuang':'小西装','girl_yangrongshan':'羊绒衫','girl_hunsha':'婚纱'}
urls = {}
# 获取网址
for key,value in productsBoy.items():
    for z in range(1,37):
        dict2={f"https://search.jd.com/Search?keyword={value}男&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={value}&page={z}&s=408&click=0":key}
        urls.update(dict2)
for key,value in productsGirl.items():
    for z in range(1,37):
        dict2 = {f"https://search.jd.com/Search?keyword={value}女&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={value}&page={z}&s=408&click=0": key}
        urls.update(dict2)


# 异步HTTP请求
async def fetch(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("window-size=1024,768")
    driver = webdriver.Chrome("chromedriver", chrome_options=chrome_options)
    # driver = webdriver.Chrome(r'chromedriver.exe')
    driver.get(url)
    k = 1
    for i in range(45):
        driver.execute_script(f'window.scrollTo({k}, {k + 250})')  # 竖直滑动，scrollHeight一屏高度
        k = k + 250
        sleep(0.1)
    soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()
    print('我正在打开浏览器')
    return soup

# 解析网页
async def parser(soup,type):
    # 利用BeautifulSoup将获取到的文本解析成HTML
    db = await CreateDB()
    cursor=await CreateCursor(db)
    place = ['上海嘉定', '上海静安', '江西南昌', '江西上饶', '浙江义乌', '河南郑州', '河南南阳', '福建福州', '福建泉州', '福建厦门', '北京通州', '湖南长沙', '江西赣州', \
             '青海西宁', '新疆乌鲁木齐', '黑龙江哈尔滨', '内蒙古齐齐哈尔', '广东广州', '广东东莞', '广东深圳', '广东惠州' \
             ]
    page = soup.find_all("li", {"class": {"gl-item"}})
    for i in range(0, 56):
        title = page[i].find("div", {"class": {"p-name p-name-type-2"}}).find('em').text.strip()
        price = page[i].find("div", {"class": {"p-price"}}).find('strong').text.strip()
        product_addre = page[i].find("div", {"class": {"p-name p-name-type-2"}}).find("a")['href']
        merchant = page[i].find("div", {"class": {"p-shop"}}).find("a").text.strip()
        merchant_addre = page[i].find("div", {"class": {"p-shop"}}).find("a")['href']
        merchant_place = place[random.randint(0, len(place) - 1)]
        img_addre = page[i].find("div", {"class": {"p-img"}}).find("img")['src']
        # if title is not None and price is not None and product_addre is not None and merchant is not None and merchant_addre is not None and merchant_place is not None and img_addre is not None:
        #     print(f'{title}\n{price}\n{product_addre}\n{merchant}\n{merchant_addre}\n{merchant_place}\n{img_addre}')
        await ToDB(title=title,price=price,product_addre=product_addre,merchant=merchant,merchant_addre=merchant_addre,merchant_place=merchant_place,img_addre\
                   =img_addre,type=type,i=i,cursor=cursor,db=db)
async def CreateDB():
    db = pymysql.connect(host="localhost", port=3306, user="root", password="", database="shopping",
                         charset='utf8')
    return db
async def CreateCursor(db):
    cursor = db.cursor()
    return cursor
# 将数据放入数据库
async def ToDB(title,price,product_addre,merchant,merchant_addre,merchant_place,img_addre,type,i,cursor,db):
    sql = f'insert into boy_clothes_product values (null,%s,%s,%s,%s,%s,%s,%s,null,%s)'
    try:
        print(cursor.execute(sql,\
                             (title, price, merchant, merchant_place, merchant_addre, img_addre, product_addre, type)))
        time3 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(time3)
        print(f"{type}信息抓取完毕！{i} " )
    except:
        # 发生错误时回滚
        db.rollback()
        time3 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(time3)
        print(f"{type}信息抓取出错！{i} " )
    if i==55:
        db.commit()
        db.close()
# 处理网页，获取name和description
async def download(url,type):
    html = await fetch(url)
    await parser(html,type)
    # async with aiohttp.ClientSession(headers=headers) as session:
    #     try:
    #
    #         print(4)
    #
    #     except Exception as err:
    #         print(3)
    #         print(err)


# 利用asyncio模块进行异步IO处理
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(download(url,type)) for url,type in urls.items()]
tasks = asyncio.gather(*tasks)
loop.run_until_complete(tasks)

t2 = time.time()  # 结束时间
print('使用异步，总共耗时：%s' % (t2 - t1))
print('#' * 50)