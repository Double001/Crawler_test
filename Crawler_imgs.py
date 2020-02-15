# -*- coding:utf-8 -*-
# 在国家地理爬取"最新"栏目图片并保存在桌面imgs文件夹内

import requests
from bs4 import BeautifulSoup as bf


url = 'http://www.nationalgeographic.com.cn/animals/'
res = requests.get(url).text
soup = bf(res,"lxml")
img_url = soup.find_all('ul', {"class": "img_list"})

for ul in img_url:
    imgs = ul.find_all('img')
    for img in imgs:
        html = img['src']
        r = requests.get(html, stream = True)
        img_name = html.split('/')[-1]
        with open('/Users/huangfutian/Desktop/imgs/%s' % img_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 128):
                f.write(chunk)
        print ('Saved %s' % img_name)



