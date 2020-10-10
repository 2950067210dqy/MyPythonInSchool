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
urls = {"http://47.94.164.171/phpproject2/HTML/message.php?id=1#textarea":1}

# 异步HTTP请求
async def fetch(url):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument("window-size=1024,768")
    # driver = webdriver.Chrome("chromedriver", chrome_options=chrome_options)
    driver = webdriver.Chrome(r'chromedriver.exe')
    driver.get(url)
    inputid = driver.find_element_by_id('id')
    inputpass = driver.find_element_by_id('password')
    inputid.send_keys('root')
    inputpass.send_keys('root')
    button = driver.find_element_by_id('logoin')
    button.click()
    k = 1
    for i in range(45):
        driver.execute_script(f'window.scrollTo({k}, {k + 250})')  # 竖直滑动，scrollHeight一屏高度
        k = k + 250
        sleep(0.1)
    driver.quit()
    print('我正在打开浏览器')
# 处理网页，获取name和description
async def download(url,type):
    html = await fetch(url)
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