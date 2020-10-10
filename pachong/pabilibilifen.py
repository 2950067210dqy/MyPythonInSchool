from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)
# driver = webdriver.Chrome(r'chromedriver.exe')
driver.get("https://space.bilibili.com/546195")
b=driver.page_source
soup = BeautifulSoup(b, 'lxml')
a= soup.find_all("div", class_="n-statistics")
a= soup.find_all("a", class_="n-data n-fs")
a=a[0]['title']
print(a)
driver.quit()