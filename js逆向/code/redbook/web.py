import requests
import json


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://www.xiaohongshu.com",
    "Pragma": "no-cache",
    "Referer": "https://www.xiaohongshu.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "X-s": "Z61bZ6FWO25i1gVvOgwvZgdvOgkUs2s+1iqvslFGZ2T3",
    "X-t": "1681397371498",
}
cookies = {
}

url = "https://edith.xiaohongshu.com/api/sns/web/v1/login/activate"
data = {}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data,timeout=10)

print(response.text)
print(response.headers)