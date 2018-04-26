
from selenium import webdriver
from scrapy import Selector
from urllib import parse
from scrapy.http import Request
#模拟鼠标ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import time

#加载浏览器程序firefox
driver =webdriver.Firefox(executable_path="D:/PycharmProjects/geckodriver.exe")
#get  url
driver.get("https://tieba.baidu.com/f?ie=utf-8&kw=%E7%82%89%E7%9F%B3%E4%BC%A0%E8%AF%B4&fr=search")
#延迟时间
time.sleep(5)
#定位登录元素
login_a=driver.find_element_by_css_selector(".u_login > div:nth-child(1) > a:nth-child(1)")
#点击元素
ActionChains(driver).click(login_a).perform()
#这里要延迟不然script加载慢
time.sleep(5)

#找出登录页面下div p 下ID 是否是用户名登录
select_txt=Selector(text=driver.page_source)
#--本来想判断先出来的是啥，感觉没法判断
# text_id=select_txt.css(".tang-pass-footerBar p::attr(data-type)").extract()[0]
# print(text_id)
# if text_id("normal"):
user_login = driver.find_element_by_css_selector("#TANGRAM__PSP_11__footerULoginBtn")
ActionChains(driver).click(user_login).perform()
time.sleep(5)

#登录用户这里登录   也可以一开始就登录然后查询贴吧

driver.find_element_by_css_selector("#TANGRAM__PSP_11__userName").send_keys("")
driver.find_element_by_css_selector("#TANGRAM__PSP_11__password").send_keys("")
driver.find_element_by_css_selector("#TANGRAM__PSP_11__submit").click()

driver.quit()








