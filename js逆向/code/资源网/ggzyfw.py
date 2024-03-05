import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import requests
import json
import hashlib
import time

def get_time():
    return int(time.time() * 1000)


def md5_encrypt(text):
    md5 = hashlib.new('md5', text.encode('utf-8'))
    return md5.hexdigest()
import execjs
def get(text):
    file = 'sign.js'
    ctx = execjs.compile(open(file,"r",encoding="utf8").read())
    data = ctx.call("tripleAesDecrypt",text)
    print(data) # 12

def req():
    ts = get_time()
    sign_data = f'3637CB36B2E54A72A7002978D0506CDFBeginTime2022-10-18 00:00:00createTime[]EndTime2023-04-18 23:59:59GGTYPE1KINDGCJSpageNo7pageSize20timeType6total3745ts{ts}'
    sign=md5_encrypt(sign_data)
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://ggzyfw.fujian.gov.cn",
        "Pragma": "no-cache",
        "Referer": "https://ggzyfw.fujian.gov.cn/business/list/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "portal-sign": sign,

    }
    url = "https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo"
    data = {
        "pageNo": 7,
        "pageSize": 20,
        "total": 3745,
        "AREACODE": "",
        "M_PROJECT_TYPE": "",
        "KIND": "GCJS",
        "GGTYPE": "1",
        "PROTYPE": "",
        "timeType": "6",
        "BeginTime": "2022-10-18 00:00:00",
        "EndTime": "2023-04-18 23:59:59",
        "createTime": [],
        "ts": ts
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    data = response.json()['Data']
    get(data)
if __name__ == '__main__':
    req()