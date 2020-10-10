import requests
from bs4 import BeautifulSoup
key_dict = {'start': 0, 'filter': ''}
num=0
while(key_dict['start']<=225):
    # link = "https://movie.douban.com/top250"
    headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; win64;en-us; x64) ApplewebKit/537.36\
            (KHTML, like Gecko) Chrom/80.0.3987.149 Safari/537.36',\
         'Host':'movie.douban.com'}
    # r=requests.post(link,data=key_dict,timeout=20)
    r = requests.get("https://movie.douban.com/top250?", params=key_dict,headers=headers)
    # print(link)
    soup = BeautifulSoup(r.text, "lxml")
    # title = soup.find("span", class_="title").text.strip()
    title=""
    # print(title)
    title_list = soup.find_all('span', class_='title')
    for i in range(len(title_list)):
        title = title_list[i].text.strip()
        if(title.count("/",0,len(title))>0):
            continue
        else:
          with open('title.txt', "a+", encoding="utf-8") as f:
                num = num + 1
                f.write(f'TOP {num} 的电影名字是： {title}\n')
                f.close()

    key_dict['start'] += 25

