#__author__=='huajianzhang'
#爬取120集的苗疆蛊事 艾宝良版有声小说
#_*_coding=utf-8 _*
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import openpyxl
import time

#用Chrome获得详情页源代码
def get_pageSouce(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    try:
        driver.get(url)
        time.sleep(2)
    except Exception as e:
        f.close()
        print('发生了{}错误!'.format(e))
    a = driver.page_source
    time.sleep(2)
    driver.close()
    return a

#使用BeautifulSoup定位音频地址
def get_address(url):
    soup=BeautifulSoup(get_pageSouce(url),'lxml')
    ads=soup.select('#jp_audio_0')
    for ad in ads:
        address=ad.get('src')
        return address

#主函数入口
if __name__=='__main__':
    #一共120集
    urls=['http://www.ting56.com/video/14144-0-{}.html'.format(number) 
          for number in range(81,120)]
    f=open('mjgs.txt','a',encoding='utf-8')
    count=0
    try:
        for url in urls:
            gds=get_address(url)
            count=count+1
            print('第{0}条，被写入！\n{1}'.format(count,gds))
            gds='\n'+gds+'\n'
            f.write(gds)
    except Exception as e:
        print('{}写入异常！'.format(e))
    finally:
        print('写入完成！')
        f.close()
