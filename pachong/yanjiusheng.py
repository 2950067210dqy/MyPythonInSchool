
import random
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import aiohttp
import asyncio
import time
from time import sleep
import requests
import hashlib
import opener as opener
import requests
from bs4 import BeautifulSoup
import re
import xlrd
import xlwt
import math
import lxml
class DataPojo():
    def __init__(self,name,place,isyanjiushengyuan,iszizhuhuaxian,isboshidian,kaoshifangshi,yuanxi,zhuanye,xuexifangshi,yanjiufangxiang,
                 zhidaolaoshi,nizhaorenshu,beizhu,ke1,ke2,ke3,ke4):
        self.name=name
        self.place=place
        self.isyanjiushengyuan=isyanjiushengyuan
        self.iszizhuhuaxian=iszizhuhuaxian
        self.isboshidian=isboshidian
        self.zhuanye=zhuanye
        self.yuanxi=yuanxi
        self.kaoshifangshi=kaoshifangshi
        self.yanjiufangxiang=yanjiufangxiang
        self.nizhaorenshu=nizhaorenshu
        self.xuexifangshi=xuexifangshi
        self.zhidaolaoshi=zhidaolaoshi
        self.beizhu=beizhu
        self.ke1=ke1
        self.ke2=ke2
        self.ke3=ke3
        self.ke4=ke4

        pass
def urlGetInit(url,data):
    url+='?'
    for key, value in data.items():
        url+=(str(key)+"="+str(value)+"&")
    return url

datas=[]

burl='https://yz.chsi.com.cn/zsml/queryAction.do'
# config=["专业学位","(0454)应用心理","应用心理","全日制","0454"]
# config=["专业学位","(0854)电子信息","计算机技术","全日制","0854"]
# config=["专业学位","(0257)审计","审计","全日制","0257"]
config=["专业学位","(1253)会计","会计","全日制","1253"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1024,768")
driver = webdriver.Chrome("chromedriver", chrome_options=chrome_options)
driver = webdriver.Chrome(r'chromedriver.exe')
driver.get(burl)

select_mldm = driver.find_element_by_name("mldm")
all_options_mldm = select_mldm.find_elements_by_tag_name("option")
for option in all_options_mldm:
    # print u"选项显示的文本：", option.text
    # print u"选项值为：", option.get_attribute("value")
    if option.text==config[0]:
        option.click()
        break

select_yjxkdm = driver.find_element_by_name("yjxkdm")
all_options_yjxkdm = select_yjxkdm.find_elements_by_tag_name("option")
for option in all_options_yjxkdm:
    if option.text==config[1]:
        option.click()
        break

select_zymc = driver.find_element_by_name("zymc")
all_options_zymc = select_zymc.find_elements_by_tag_name("option")
for option in all_options_zymc:
    if option.text==config[2]:
        option.click()
        break

select_xxfs = driver.find_element_by_name("xxfs")
all_options_xxfs = select_xxfs.find_elements_by_tag_name("option")
for option in all_options_xxfs:
    if option.text==config[3]:
        option.click()
        break

button = driver.find_element_by_name("button")
button.click()
schools=[]
flag=True
while flag:
# while BeautifulSoup(driver.page_source,"html.parser").find("div",{"class":{"zsml-page-box"}}).find("ul",{"class":{"ch-page"}}).find("li",{"class":{"lip-last","unable","lip"}}):
    soup = BeautifulSoup(driver.page_source,"html.parser")
    table=soup.find("table",{"class":{"ch-table"}})
    tr=table.find_all("tr")
    tr=tr[1:len(tr)]
    for i in tr:
        tds=i.find_all("td")
        schoolStr=tds[0].text.strip()
        schoolN=schoolStr[1:schoolStr.find(")")]
        school=schoolStr[schoolStr.find(")")+1:len(schoolStr)]
        placeStr=tds[1].text.strip()
        placeN = placeStr[1:placeStr.find(")") ]
        place = placeStr[placeStr.find(")") + 1:len(placeStr)]
        isyanjiushengyuan="是"
        iszizhuhuaxian="是"
        isboshidian="是"
        if tds[2].find("i")==None:
            isyanjiushengyuan = "否"
        if tds[3].find("i")==None:
            iszizhuhuaxian = "否"
        if tds[4].find("i")==None:
            isboshidian = "否"
        elment={"schoolN":schoolN,
                "school":school,
                "placeN":placeN,
                "place":place,
                "isyanjiushengyuan":isyanjiushengyuan,
                "iszizhuhuaxian": iszizhuhuaxian,
                "isboshidian":isboshidian}
        schools.append(elment)
    if BeautifulSoup(driver.page_source, "html.parser").select_one('li.dot.lip')==None:
        if BeautifulSoup(driver.page_source, "html.parser").select_one('li.lip-last.unable.lip')==None:
            driver.find_element_by_class_name("lip-last").click()
        else:
            flag=False
    else:
        if BeautifulSoup(driver.page_source, "html.parser").select_one('ul.ch-page').find_all("li")[len(BeautifulSoup(driver.page_source, "html.parser").select_one('ul.ch-page').find_all("li"))-2:len(BeautifulSoup(driver.page_source, "html.parser").select_one('ul.ch-page').find_all("li"))-1][0]['class'][1] != "unable":
            driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[4]/ul/li[9]").click()
        else:
            flag = False


USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
baseurl='https://yz.chsi.com.cn/zsml/querySchAction.do'
newSchools=[]
for school in schools:
    headers = {
        'User-Agent': USER_AGENTS[random.randint(0, len(USER_AGENTS) - 1)],
    }
    postdata = {
    'ssdm': '',
    'dwmc':'',
        'ssdm':school['placeN'],
        'dwmc':school['school'],
        'mldm':'zyxw',
        'mlmc':"",
        "yjxkdm":config[4],
        'xxfs':'1',
        'zymc':config[2]
    }

    url=urlGetInit(baseurl,postdata)
    HTML = requests.get(url,  headers=headers)
    HTML.encoding = "utf8"
    soup = BeautifulSoup(HTML.text, "html.parser")
    table=soup.select_one("table.ch-table.more-content")
    trs=soup.find_all("tr")
    trs=trs[1:len(trs)]
    for tr in trs:
        td=tr.find_all("td")
        detailUrl="https://yz.chsi.com.cn"+str(td[7].find("a")['href'])
        newelement={
            "detailUrl":detailUrl,
            "place":str(school['placeN'])+str(school['place']),
                "isyanjiushengyuan":school['isyanjiushengyuan'],
                "iszizhuhuaxian":school['iszizhuhuaxian'],
                "isboshidian":school['isboshidian']
        }
        newSchools.append(newelement)


#生成一个excel文件
writebook = xlwt.Workbook()  # 打开一个excel
sheet = writebook.add_sheet('data')  # 在打开的excel中添加一个sheet
#初始化excel字段名
sheet.write(0, 0, "序号")  # 写入excel，i行j列
sheet.write(0, 1, "招生院校")  # 写入excel，i行j列
sheet.write(0, 2, "招生地点")  # 写入excel，i行j列
sheet.write(0, 3, "研究生院")  # 写入excel，i行j列
sheet.write(0, 4, "自划线院校")  # 写入excel，i行j列
sheet.write(0, 5, "博士点")  # 写入excel，i行j列
sheet.write(0, 6, "考试方式")  # 写入excel，i行j列
sheet.write(0, 7, "院系所")  # 写入excel，i行j列
sheet.write(0, 8, "专业")  # 写入excel，i行j列
sheet.write(0, 9, "学习方式")  # 写入excel，i行j列
sheet.write(0, 10, "研究方向")  # 写入excel，i行j列
sheet.write(0, 11, "指导老师")  # 写入excel，i行j列
sheet.write(0, 12, "拟招人数")  # 写入excel，i行j列
sheet.write(0, 13, "备注")  # 写入excel，i行j列
sheet.write(0, 14, "考试科目1")  # 写入excel，i行j列
sheet.write(0, 15, "考试科目2")  # 写入excel，i行j列
sheet.write(0, 16, "考试科目3")  # 写入excel，i行j列
sheet.write(0, 17, "考试科目4")  # 写入excel，i行j列

number=1
for newSchool in newSchools:
    name = None
    place = None
    isyanjiushengyuan = None
    iszizhuhuaxian = None
    isboshidian = None
    kaoshifangshi = None
    yuanxi = None
    zhuanye = None
    xuexifangshi = None
    yanjiufangxiang = None
    zhidaolaoshi = None
    nizhaorenshu = None
    beizhu = None
    ke1 = None
    ke2 = None
    ke3 = None
    ke4 = None
    headers = {
        'User-Agent': USER_AGENTS[random.randint(0, len(USER_AGENTS) - 1)],
    }
    HTML = requests.get(newSchool['detailUrl'], headers=headers)
    HTML.encoding = "utf8"
    soup = BeautifulSoup(HTML.text, "html.parser")
    table=soup.select_one("table.zsml-condition")
    trs=table.find_all("tr")
    name=trs[0].find_all("td")[1].text
    place=newSchool['place']
    isyanjiushengyuan=newSchool['isyanjiushengyuan']
    iszizhuhuaxian=newSchool['iszizhuhuaxian']
    isboshidian=newSchool['isboshidian']
    kaoshifangshi=trs[0].find_all("td")[3].text
    yuanxi=trs[1].find_all("td")[1].text
    zhuanye=trs[1].find_all("td")[3].text
    xuexifangshi=trs[2].find_all("td")[1].text
    yanjiufangxiang=trs[2].find_all("td")[3].text
    zhidaolaoshi=trs[3].find_all("td")[1].text
    nizhaorenshu=trs[3].find_all("td")[3].text
    beizhu=trs[4].find_all("td")[1].text

    kaoshiDiv=soup.select_one("div.zsml-result")
    kaoshiTable=kaoshiDiv.select_one("table")
    kaoshitrs=kaoshiTable.find_all("tr")
    kaoshitds=kaoshitrs[1].find_all("td")
    ke1=kaoshitds[0].text[0:len(kaoshitds[0].text)-len("参考考试大纲")]
    ke2=kaoshitds[1].text[0:len(kaoshitds[1].text)-len("参考考试大纲")]
    ke3=kaoshitds[2].text[0:len(kaoshitds[2].text)-len("参考考试大纲")]
    ke4=kaoshitds[3].text[0:len(kaoshitds[3].text)-len("参考考试大纲")]
    # data=DataPojo( name, place, isyanjiushengyuan, iszizhuhuaxian, isboshidian, kaoshifangshi, yuanxi, zhuanye,
    #              xuexifangshi, yanjiufangxiang,
    #              zhidaolaoshi, nizhaorenshu, beizhu, ke1, ke2, ke3, ke4)

    sheet.write(number, 0, number)  # 写入excel，i行j列
    sheet.write(number, 1, name)  # 写入excel，i行j列
    sheet.write(number, 2, place)  # 写入excel，i行j列
    sheet.write(number, 3, isyanjiushengyuan)  # 写入excel，i行j列
    sheet.write(number, 4, iszizhuhuaxian)  # 写入excel，i行j列
    sheet.write(number, 5, isboshidian)  # 写入excel，i行j列
    sheet.write(number, 6, kaoshifangshi)  # 写入excel，i行j列
    sheet.write(number, 7,  yuanxi)  # 写入excel，i行j列
    sheet.write(number, 8, zhuanye)  # 写入excel，i行j列
    sheet.write(number, 9, xuexifangshi)  # 写入excel，i行j列
    sheet.write(number, 10, yanjiufangxiang)  # 写入excel，i行j列
    sheet.write(number, 11, zhidaolaoshi)  # 写入excel，i行j列
    sheet.write(number, 12, nizhaorenshu)  # 写入excel，i行j列
    sheet.write(number, 13, beizhu)  # 写入excel，i行j列
    sheet.write(number, 14,  ke1)  # 写入excel，i行j列
    sheet.write(number, 15,  ke2)  # 写入excel，i行j列
    sheet.write(number, 16,  ke3)  # 写入excel，i行j列
    sheet.write(number, 17,  ke4)  # 写入excel，i行j列
    number+=1
writebook.save(f'考研{config[0]}{config[1]}{config[2]}{config[3]}数据.xls')  # 一定要记得保存
driver.quit()




