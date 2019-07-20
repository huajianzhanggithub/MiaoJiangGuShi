# __author__=='huajianzhang'
# # 爬取395集的苗疆蛊事 艾宝良版有声小说
# # _*_coding=utf-8 _*
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re


# 用Chrome获得详情页源代码
def get_pageSouce(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        driver.switch_to.frame(0)
        time.sleep(1)
    except Exception as e:
        f.close()
        print('发生了{}错误!'.format(e))
    a = driver.page_source
    driver.close()
    return a


# 使用正则表达式定位音频地址
def get_address(url):
    # soup = BeautifulSoup(get_pageSouce(url), 'lxml')
    ads = re.findall('<a rel="nofollow" id="download" href="(.*?)" target="_self">', get_pageSouce(url))
    return ads[0]


# 主函数入口 苗疆蛊事_有声小说_艾宝良_我爱听评书网
if __name__ == '__main__':
    # 一共120集
    urls = ['http://www.52tps.com/xz/mjgs_1845/audio_{}.html'.format(number)
            for number in range(1, 396)]
    f = open('mjgs.txt', 'w+', encoding='utf-8')
    count = 0
    try:
        for url in urls:
            gds = get_address(url)
            count = count + 1
            print('第{0}条，被写入！\n{1}'.format(count, gds))
            gds = '\n' + gds + '\n'
            f.write(gds)
    except Exception as e:
        print('{}写入异常！'.format(e))
    finally:
        print('写入完成！')
        f.close()
