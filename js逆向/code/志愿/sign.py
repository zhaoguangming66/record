from utils.deciphering import md5_encrypt,get_time


def req():
    import requests

    headers = {
        "authority": "www.jizhy.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.jizhy.com/44/rank/school",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    cookies = {
        "PI": "44"
    }
    page = 1
    page_len = 20
    ts = get_time()
    data_=f'{{app_id=98357f659cf8fb6001cff80f7c6b85f2&diploma_id=7&page={page}&page_len={page_len}&platform=desktop&ts={ts}&v=210&wenli=0}}&key=146fd1e66513611ac7af69f21f1d7725'
    sign=md5_encrypt(data_).upper()
    url = "https://www.jizhy.com/open/sch/rank-list"
    params = {
        "page": f"{page}",
        "page_len": f"{page_len}",
        "diploma_id": "7",
        "wenli": "0",
        "app_id": "98357f659cf8fb6001cff80f7c6b85f2",
        "ts": f"{ts}",
        "platform": "desktop",
        "v": "210",
        "sign": sign
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    print(response.text)
    print(response)
if __name__ == '__main__':
    req()