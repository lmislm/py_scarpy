import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
url = 'http://hrb.ganji.com/zpruanjiangongchengshi/'
# 获取页面源码函数
def get_page_resp(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            return resp.text
        return None
    except RequestException:
        return None
#print(get_page_resp(url))

#soup = BeautifulSoup(get_page_resp(url), 'lxml')

