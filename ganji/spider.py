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

soup = BeautifulSoup(get_page_resp(url), 'lxml')
# job_list = soup.select('div.new-dl-company > a')
job_list = soup.select('div.new-dl-wrapper > div > dl')
job_details = [i.get_text("|", strip=True) for i in job_list]
print(job_details[0])
     # print(jobnames)
    # for jobname in zip(jobnames):
    #     data = {
    #         'name': jobname
    #     }
    #     yield data

