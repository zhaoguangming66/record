import requests

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.birdreport.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://www.birdreport.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'requestId': 'c71a91c6c3237c4f2dc8377c32cce3dd',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sign': '22b60bf2047556924ac2cf0001211f0f',
    'timestamp': '1681360205000',
}

data = 'm5S6WP0Aklfr8t87vi34zZMnrRwGbgAMpxb4lHBtN5qcnO8UiuZPL3eIpJ99ox3iRd10eLHOSfS8n4lCZ0l5n1skQcPgBPY+OINN9OZ/xSoBiOGbpREBLc699Ci1rIAagbF8gmfq8AFHVVPmHtnRxyz+2fh6GVtJB784UyNgass='

response = requests.post('https://api.birdreport.cn/front/activity/search', headers=headers, data=data)
print(response.content.decode())