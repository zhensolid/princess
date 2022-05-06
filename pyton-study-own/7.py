
import requests
#编写抓取网页文字的函数
def get_html(url):
    try:
        r = requests.get(url='https://www.3dmgame.com/',timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

    except:
        return "爬取失败"
print(get_html('https://www.3dmgame.com/'))

