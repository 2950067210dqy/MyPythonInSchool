from selenium import webdriver
import requests
from bs4 import BeautifulSoup


def getSoup(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        ,"Referer":"http://search1.jxedu.gov.cn/searchProject/GktjxxbSearch.action"
        ,"Referer Policy":"strict-origin-when-cross-origin"
        ,"Origin":"http://search1.jxedu.gov.cn"
        ,"Upgrade-Insecure-Requests":"1"

    }
    r = requests.get(link)
    # print(r.text)
    # soup = BeautifulSoup(r.text, 'lxml')
    print(r.text)
    return r
def getDriver(link):
    # 不打开浏览器后台运行
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    headers = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
    referer=("http://search1.jxedu.gov.cn/searchProject/GktjxxbSearch.action")
    # chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument(f'user-agent={headers}')
    chrome_options.add_argument(f'--Referer={referer}')
    # chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("window-size=1024,768")
    driver = webdriver.Chrome(r"chromedriver.exe",chrome_options=chrome_options)
    #打开浏览器
    # driver = webdriver.Chrome(r'chromedriver.exe')

    driver.get(link)
    return driver
def CloseDriver(driver):
    driver.quit()
def getDriverSoup(driver):
    b = driver.page_source
    soup = BeautifulSoup(b, 'lxml')
    return soup
# driver = getDriver("http://47.94.164.171")
# # img_list = getDriverSoup(driver).find_all("div",class_="lazy-img cover")
# CloseDriver(driver)
prex="18360123150"

for i in range(1,2):


    with open(f"1836012315070{i}.gif","wb") as f:
        f.write(getSoup(link=f"http://search1.jxedu.gov.cn/searchProject/healthcheck2011/gif/18360123/1836012315070{2}.gif").content)
        f.close()