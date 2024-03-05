import json
import re
import execjs
import requests


def get(text):
    ctx = execjs.compile(open('data.js').read())
    data = ctx.call("r", text)
    return data


def get_text():
    headers = {
        "authority": "www.360kuai.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }

    url = "https://www.360kuai.com/9ce8fd476e917dc89"
    params = {
        "f252c13b3f5c8959a9b275056b558abf": ""
    }
    response = requests.get(url, headers=headers, params=params)
    data = re.search("window.__INITIAL_DATA__ = '\\\\\n(.*?)'", response.content.decode(), re.S).group(1)
    wenzi = get(data)
    print(json.loads(wenzi))


if __name__ == '__main__':
    get_text()
