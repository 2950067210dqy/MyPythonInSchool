
from time import sleep
from selenium import webdriver
import pymysql
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains


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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup
def getDriver(link):
    #不打开浏览器后台运行
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("window-size=1024,768")
    #driver = webdriver.Chrome("chromedriver",chrome_options=chrome_options)
    #打开浏览器
    driver = webdriver.Chrome(r'chromedriver.exe')

    driver.get(link)
    # driver.find_element_by_id('fm-login-id').send_keys('15970674596')
    # driver.find_element_by_id('fm-login-password').send_keys('2591215997dqy')
    # driver.find_element_by_tag_name('button').click()
    # target_ele=driver.find_element_by_class_name('nc-lang-cnt')
    # # 创建一个拖动对象
    # action = ActionChains(driver)
    # # 点击拖动对象并长按保持
    # action.click_and_hold(target_ele)
    # for i in range(5):
    #     # 执行拖动动作
    #     action.move_by_offset(150, 0).perform()
    # # 释放拖动对象句柄
    # action.release()
    # driver.find_element_by_tag_name('button').click()

    k = 1
    for i in range(110):
        driver.execute_script(f'window.scrollTo({k}, {k + 100})')  # 竖直滑动，scrollHeight一屏高度
        k = k + 100
        sleep(0.4)
    return driver

def CloseDriver(driver):
    driver.quit()
    pass
def getDriverSoup(driver):
    b = driver.page_source
    soup = BeautifulSoup(b, 'lxml')
    return soup


def allorderby(link,table,dbs,type):
    db=getDB("localhost",3306,"root","",f'{dbs}','utf8')
    cursor=getCursor(db)
    driver = getDriver(link)
    soup=getDriverSoup(driver)
    CloseDriver(driver)
    # print(soup)


    place=['上海嘉定','上海静安','江西南昌','江西上饶','浙江义乌','河南郑州','河南南阳','福建福州','福建泉州','福建厦门','北京通州','湖南长沙','江西赣州',\
           '青海西宁','新疆乌鲁木齐','黑龙江哈尔滨','内蒙古齐齐哈尔','广东广州','广东东莞','广东深圳','广东惠州'\
           ]
    page=soup.find_all("li",{"class":{"gl-item"}})
    for i in range(0,56):
        title=page[i].find("div",{"class":{"p-name p-name-type-2"}}).find('em').text.strip()
        price=page[i].find("div",{"class":{"p-price"}}).find('strong').text.strip()
        product_addre=page[i].find("div",{"class":{"p-name p-name-type-2"}}).find("a")['href']
        merchant=page[i].find("div",{"class":{"p-shop"}}).find("a").text.strip()
        merchant_addre=page[i].find("div",{"class":{"p-shop"}}).find("a")['href']
        merchant_place=place[random.randint(0,len(place)-1)]
        img_addre=page[i].find("div",{"class":{"p-img"}}).find("img")['src']
        sql=f'insert into {table} values (null,%s,%s,%s,%s,%s,%s,%s,null,%s)'
        try:
             print(cursor.execute(sql, (title,price,merchant,merchant_place,merchant_addre,img_addre,product_addre,type)))
             time3 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
             print(time3)
             print(f"{dbs}的{table}信息抓取完毕！{i} " + sql)
        except:
            # 发生错误时回滚
            db.rollback()
            time3 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            print(time3)
            print(f"{dbs}的{table}信息抓取出错！{i} " + sql)
    db.commit()
    db.close()


time1=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(time1)
productsBoy={'yurongfu':'羽绒服','jiake':'夹克','xifu':'西服套装','txue':'T恤','xiuxianku':"休闲裤"}
productsGirl={'lianyiqun':'连衣裙','banshenqun':'半身裙','duanwaitao':'短外套','xiaoxizhuang':'小西装','yangrongshan':'羊绒衫','hunsha':'婚纱'}
for key,value in productsBoy.items():
    for z in range(1,25):
        print(f'正在抓取{value}男第{z}页')
        allorderby(link = f"https://search.jd.com/Search?keyword={value}男&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={value}&page={z}&s=408&click=0",table="boy_clothes_product",dbs="shopping",type=key)
print("男生服装抓取完毕")
for key,value in productsGirl.items():
    for z in range(1,25):
        print(f'正在抓取{value}男第{z}页')
        allorderby(link = f"https://search.jd.com/Search?keyword={value}男&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={value}&page={z}&s=408&click=0",table="boy_clothes_product",dbs="shopping",type=key)


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


