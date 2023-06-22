import execjs
import requests
import json

from utils.deciphering import md5_encrypt


def get():
    file = """
    function get_sign() {
    var t =("000000" + Math.floor(999999 * Math.random())).slice(-6)
    , o = (new Date).getTime();
    var data = o + "_" + t + "_" + "sdxxqbrolkjwrgoiuyhasdglksjlaghnow32429asnnhg"

    return [o,t,data]
}

    """
    ctx = execjs.compile(file)
    data = ctx.call("get_sign")
    return data

def req():
    import requests

    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.51sdx.com",
        "Pragma": "no-cache",
        "Referer": "https://www.51sdx.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    sign_list=get()
    url = "https://int.51sdx.com/niuzy/uinfo/univ/queryUniv"
    verifySign=md5_encrypt(sign_list[2])
    params = {
        "univName": "",
        "provId": "",
        "univType": "",
        "zbType": "",
        "departType": "",
        "isPublic": "",
        "feature": "",
        "is985": "",
        "is211": "",
        "isFirstClass": "",
        "isFirstLevel": "",
        "hasMaster": "",
        "isIndependent": "",
        "pageSize": "10",
        "pageNum": "10",
        "verifyTimestamp": sign_list[0],
        "verifyNonce": sign_list[1],
        "channel": "sdx",
        "channelId": "sdx",
        "channelCode": "sdx",
        "comeFrom": "",
        "verifySign": verifySign
    }
    response = requests.get(url, headers=headers, params=params)

    print(response.text)
    print(response)
if __name__ == '__main__':
    req()