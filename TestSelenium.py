#Need to install chrome driver and put it into proper location first
#https://blog.csdn.net/weixin_44318830/article/details/103339273
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
