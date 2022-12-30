import requests
import os

# 抓取图片的url
url = 'https://img.3dmgame.com/uploads/images2/news/20221228/1672209475_919094.jpg'

# 发送get请求
resp = requests.get(url)

# 保存图片
if resp.status_code == 200:
    # 获取图片名
    file_name = os.path.basename(url)
    # 保存图片
    with open(file_name, 'wb') as f:
        f.write(resp.content)


