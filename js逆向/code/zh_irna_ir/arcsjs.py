import json
import re
from urllib.parse import urljoin

import redis
import requests
import execjs
from lxml import etree

from utils.settings import proxies
redis_cli = redis.Redis(decode_responses=True)
def url_list():
    urls_str="""
    https://en.irna.ir/
    https://ar.irna.ir/
    https://zh.irna.ir/
    https://tr.irna.ir/
    https://es.irna.ir/
    https://ru.irna.ir/
    https://ur.irna.ir/
    https://de.irna.ir/
    https://fr.irna.ir/
    """
    return [url.strip() for url in urls_str.split("\n") if url.strip()]

def test(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    # url = "https://fr.irna.ir/news/85075322/Signature-d-une-d%C3%A9claration-conjointe-entre-l-Iran-et-l-Arabie"

    response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
    print(f"第一次页面：{response.content.decode()}")
    res = re.search("type=\"text/javascript\">(.*?); var hash", response.content.decode(), re.S).group(1)
    txt = f"""
        function getck() {{
        {res}
        return _0x2d84('0x1');
        }}
        """
    print(f"js==>{txt}")
    ctx = execjs.compile(txt)
    ck = ctx.call("getck")
    cookies = {
        "__arcsjs": ck
    }
    print(f"cookies:{cookies}")
    response = requests.get(url, headers=headers, proxies=proxies,cookies=cookies, timeout=10)
    print(response.content.decode())
    return response.content.decode()




def main():
    res=test('https://fr.irna.ir/service/Infos')
    root=etree.HTML(res)
    data=root.xpath("//div[@class='desc']/h3/a")
    for page in data:
        title = page.xpath('.//text()|./@title')[0]
        url = page.xpath('./@href')[0]
        print(url)
if __name__ == '__main__':
    main()
