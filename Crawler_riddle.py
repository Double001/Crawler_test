# -*- coding=utf-8 -*-
# author = Double; Date: 2020/02/15

import requests
from bs4 import BeautifulSoup as bf
import os.path
import time

f = open('/Users/****/Desktop/Riddle.txt', 'w+')
for i in range(1,4):
    url = 'http://duanziwang.com/page/'+str(i) # 将i转换成str
    # 爬取前400页，观察>>>http://duanziwang.com/page/3/
    res = requests.get(url).text  # 此处要加text，否则返回值是 Respond 200。
    soup = bf(res, 'lxml')
    contents = soup.find_all('div', {'class': 'post-content'})
    for content in contents:
        f.write(content.get_text()+'\n')
        print(content.get_text())
    time.sleep(0.5)
f.close()
