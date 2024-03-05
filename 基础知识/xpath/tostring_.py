import requests
from lxml import etree
from lxml.etree import tostring

from utils.settings import proxies


def xpath_extract_content(element, content_xpath='', encoding='utf-8', clear_attrib=True, pretty_print=False,
                          method='html'):
    """提取带标签的内容"""
    content = element.xpath(content_xpath)
    news_content = ''
    if content:
        for element_ in content:
            if clear_attrib:
                element_.attrib.clear()
            news_content += bytes.decode(
                tostring(element_, encoding=encoding, pretty_print=pretty_print, method=method))
    return news_content


def req():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    }
    cookies = {}
    url = 'https://www.bloomeradvance.com/news/front_page/article_e9f7d042-ef36-11ed-8fbb-039036fa1ed8.html'

    response = requests.get(url, headers=headers, cookies=cookies,proxies=proxies)
    root = etree.HTML(response.content.decode())
    data=xpath_extract_content(root,content_xpath="//div[@id='article-body']")
    print(data)
if __name__ == '__main__':
    req()