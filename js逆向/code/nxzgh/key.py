import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Origin': 'https://www.nxzgh.org.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.nxzgh.org.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'key': 'bXyulqGYo8OsegO9F04oH01Hj5dx9PpMcS055MYae2n/9jrAKD2sUlLsyhKhXNU0v3SXtTGbXaRFoxKmFxsYniDyGtrl0RithutabV3DPK/yIh0oYuwsPuUqJ0MV0KoD39AYP1xT001agXwuLfCUTZM1TdxIbLarWDTp8I6Efsc=',
    # 'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
}

json_data = '/FFrM0T5CI7qwH7gReou/MxIOPcdaFTU4DJ2hBPceCM4UD8szfW9wYSQrUg5l8b+Ss3GPIzFX172xZM7BmBTkcI/Q2asp6VhFyNpiBt/6H0='

response = requests.post('https://nx.httdmall.com/zgh-web/article/plate/list', headers=headers, json=json_data)
print(response.headers)
print(response.content.decode())