import requests
from bs4 import BeautifulSoup
import re
import xlrd
import xlwt
import math

class dataPojo():
    def __init__(self,detail,title,name,place,room,size,direct,style,stairstyle,stairs,frontstyle,totalprice,singalprice):
        self.detail=detail#房源详细信息网址
        self.title=title#房源介绍
        self.name=name#房源名称
        self.place=place#房源位置
        self.room=room#房源几房几厅
        self.size=size#房源大小
        self.direct=direct#房源朝向
        self.style=style#房源风格
        self.stairstyle=stairstyle#房源楼层类型
        self.stairs=stairs#房源总楼层
        self.frontstyle=frontstyle#房源类型
        self.totalprice=totalprice#房源总价
        self.singalprice=singalprice#房源每平米单价
        pass
#生成一个excel文件
writebook = xlwt.Workbook()  # 打开一个excel
sheet = writebook.add_sheet('data')  # 在打开的excel中添加一个sheet
#初始化excel字段名
sheet.write(0, 0, "序号")  # 写入excel，i行j列
sheet.write(0, 1, "详细信息网址")  # 写入excel，i行j列
sheet.write(0, 2, "房源介绍")  # 写入excel，i行j列
sheet.write(0, 3, "房源名称")  # 写入excel，i行j列
sheet.write(0, 4, "房源位置")  # 写入excel，i行j列
sheet.write(0, 5, "房源几房几厅")  # 写入excel，i行j列
sheet.write(0, 6, "房源大小(平米)")  # 写入excel，i行j列
sheet.write(0, 7, "房源朝向")  # 写入excel，i行j列
sheet.write(0, 8, "房源风格")  # 写入excel，i行j列
sheet.write(0, 9, "房源楼层类型")  # 写入excel，i行j列
sheet.write(0, 10, "房源总楼层（层）")  # 写入excel，i行j列
sheet.write(0, 11, "房源类型")  # 写入excel，i行j列
sheet.write(0, 12, "房源总价（万元）")  # 写入excel，i行j列
sheet.write(0, 13, "房源单价（元/每平米）")  # 写入excel，i行j列
#爬虫配置初始化
headers = {
    # "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/91.0.4472.101"
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
cityname=None
city="nc"
city=input("请输入您要爬取哪个城市的二手房信息(例如：南昌输入nc，上海输入sh)：")
while not re.match(r'^[A-Za-z]+$', city) or len(city) == 0 :
    city = input(f"{city}值非法，请输入您要爬取哪个城市的二手房信息(例如：南昌输入nc，上海输入sh)：")
baseURL=f"https://{city}.lianjia.com/ershoufang/pg"
pageCurrent=1
limit=30
try:
    HTML = requests.get(baseURL+str(pageCurrent)+"/", headers=headers)
    HTML.encoding = "utf8"
    HTML = HTML.text
    soup = BeautifulSoup(HTML, 'lxml')
    # 找到body 把body文档树进行lxml解析
    soup = BeautifulSoup(str(soup.find_all('body')), 'lxml')
    totoalnums = int(soup.find("h2", {"class": {"total", "fl"}}).find("span").text)
    cityname=soup.find("h2", {"class": {"total", "fl"}}).text
    cityname=cityname[cityname.index("套")+1:cityname.index("二")]
    page = math.floor(totoalnums / 30)
    for e in range(1, page):
        HTML = requests.get(baseURL + str(e) + "/", headers=headers)
        HTML.encoding = "utf8"
        HTML = HTML.text
        soup = BeautifulSoup(HTML, 'lxml')
        # 找到body 把body文档树进行lxml解析
        soup = BeautifulSoup(str(soup.find_all('body')), 'lxml')
        # 解析数据
        try:
            soup = soup.find("ul", {"class": {"sellListContent"}}).find_all("li", {"class": {"clear", "LOGCLICKDATA"}})
            for i in range(len(soup)):
                print(f"正在爬取第" + str((e - 1) * 30 + i + 1) + f"/{totoalnums}条{cityname}城市的二手房数据，请不要关闭程序，否则数据将丢失！")
                detail = soup[i].find("div", {"class": {"title"}}).find("a")['href']  # 房源详细信息网址
                title = soup[i].find("div", {"class": {"title"}}).find("a").text  # 房源介绍
                name = soup[i].find("div", {"class": {"positionInfo"}}).find("a").text  # 房源名称
                place = soup[i].find("a", {"class": {"noresultRecommend", "img", "LOGCLICKDATA"}}).find("img", {
                    "class": {"lj-lazy"}})['alt']  # 房源位置
                allRoomInfo = str(soup[i].find("div", {"class": {"houseInfo"}}).text)
                allRoomInfoList = allRoomInfo.split("|")
                room = allRoomInfoList[0]  # 房源几房几厅
                size = int(re.findall(r'\d+', allRoomInfoList[1].strip())[0])  # 房源大小
                direct = allRoomInfoList[2].strip()  # 房源朝向
                style = allRoomInfoList[3].strip()  # 房源风格
                stairstyle = allRoomInfoList[4].strip()[:3:1]  # 房源楼层类型
                stairs = int(re.findall(r'\d+', allRoomInfoList[4])[0])  # 房源总楼层
                frontstyle = allRoomInfoList[5].strip()  # 房源类型
                totalprice = float(soup[i].find("div", {"class": {"totalPrice"}}).find("span").text)  # 房源总价
                singalprice = int(
                    re.findall(r'\d+', soup[i].find("div", {"class": {"unitPrice"}}).find("span").text)[0])  # 房源每平米单价
                sheet.write((e - 1) * 30 + i + 1, 0, (e - 1) * 30 + i + 1)  # 写入excel，i行j列
                sheet.write((e - 1) * 30 + i + 1, 1, detail)  # 写入excel，i行j列
                sheet.write((e - 1) * 30 + i + 1, 2, title)  # 写入excel，i行j列
                sheet.write((e - 1) * 30 + i + 1, 3, name)  # 写入excel，i行j列
                sheet.write((e - 1) * 30 + i + 1, 4, place)  # 写入excel，i行j列
                sheet.write((e - 1) * 30 + i + 1, 5, room)  # 写入excel，i行j列
                sheet.write((e - 1) * 30 + i + 1, 6, size)  # 写入excel，i行j列
                sheet.write((e - 1) * 30 + i + 1, 7, direct)  # 写入excel，i行j列
                sheet.write((e - 1) * 30 + i + 1, 8, style)  # 写入excel，i行j列
                sheet.write((e - 1) * 30 + i + 1, 9, stairstyle)  # 写入excel，i行j列
                sheet.write((e - 1) * 30 + i + 1, 10, stairs)  # 写入excel，i行j列
                sheet.write((e - 1) * 30 + i + 1, 11, frontstyle)  # 写入excel，i行j列
                sheet.write((e - 1) * 30 + i + 1, 12, totalprice)  # 写入excel，i行j列
                sheet.write((e - 1) * 30 + i + 1, 13, singalprice)  # 写入excel，i行j列
        except:
            print("网站错误，跳过！")
except:
    print("城市输入错误，请重新运行程序！")
writebook.save(f'{cityname}二手房数据.xls')  # 一定要记得保存
