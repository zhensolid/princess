import requests
import os
from bs4 import BeautifulSoup

# 先创建一个images文件夹
if not os.path.exists('E:/images'):
    os.mkdir('E:/images')
# 需要抓取网页的地址
url = 'https://www.3dmgame.com/bagua/5745.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

# 请求网页
response = requests.get(url, headers=headers)

# 解析网页
soup = BeautifulSoup(response.text, 'lxml')

# key 找到图片所在的div 注意图片div的class
img_div = soup.find('div', class_='news_warp_center')

# 找到所有图片博包含img 的标签
imgs = img_div.find_all('img')

# 下载每一张图片
for img in imgs:
    # 获取图片的url
    img_url = img['src']
    # 请求图片
    img_response = requests.get(img_url)
    # 保存图片到指定的位置
    with open('E:/images/' + img_url.split('/')[-1], 'wb') as f:
        f.write(img_response.content)
        print('保存成功：', img_url.split('/')[-1])
