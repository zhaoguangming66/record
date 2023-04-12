import requests
import execjs


def getdata(text):
    res = open("sign.js", "r", encoding="utf8").read()
    ctx = execjs.compile(res)
    return ctx.call("get_data", text)

def req():
    text = "page=1&limit=20"
    head=getdata(text)
    print(head)

    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://www.birdreport.cn",
        "Pragma": "no-cache",
        "Referer": "http://www.birdreport.cn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "requestId": head[1],
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sign": head[2],
        "timestamp": str(head[0]),
        "Access-Control-Request-Headers": "requestid,sign,timestamp",
        "Access-Control-Request-Method": "POST"
    }
    url = "https://api.birdreport.cn/front/activity/search"

    data = {
        head[3]
    }
    response = requests.options(url, headers=headers, data=data)

    print(response.text)
    print(response)
if __name__ == '__main__':
    req()