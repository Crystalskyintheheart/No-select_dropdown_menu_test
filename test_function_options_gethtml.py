import requests, re
from bs4 import BeautifulSoup

def download_page(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    #res.content返回的是bytes型也就是二进制的数据；可以取得图片，文件
    #res.text返回的是Unicode型的数据；可以取得文本
    #res.json返回的是json格式的数据
    res=requests.get(url, headers=headers)
    res.raise_for_status()
    data =res.content
    return data

def get_li(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    ol = soup.find('div', attrs={'class':'tag-box l'})
    #print(ol)
    name = []  # 下拉列表
    for i in ol.find_all('a'):
        print(i)
        detail = i.get_text()
        name.append(detail)
    print(name)

if __name__ == '__main__':
    doc = download_page('https://www.imooc.com/')
    get_li(doc)