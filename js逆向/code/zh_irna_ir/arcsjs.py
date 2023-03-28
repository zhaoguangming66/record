import re
import requests
import execjs
from utils.settings import proxies


def test():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }

    url = "https://zh.irna.ir/news/85067233/%E6%88%91%E5%9B%BD%E5%A4%96%E9%95%BF%E4%B8%8E%E6%B2%99%E7%89%B9%E5%A4%96%E9%95%BF%E9%80%9A%E7%94%B5%E8%AF%9D"
    response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
    res = re.search("type=\"text/javascript\">(.*?); var hash", response.content.decode(), re.S).group(1)
    txt = f"""
        function getck() {{
        {res}
        return _0x2d84('0x1');
        }}

        """
    ctx = execjs.compile(txt)
    ck = ctx.call("getck")
    print(ck)
    cookies = {
        "__arcsjs": ck
    }
    response = requests.get(url, headers=headers, proxies=proxies,cookies=cookies, timeout=10)
    print(response.content.decode())


if __name__ == '__main__':
    test()

