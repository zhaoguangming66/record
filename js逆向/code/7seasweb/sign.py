import time

from utils.deciphering import md5_encrypt


def get_time():
    return int(time.time() * 1000)


def get_sign(timeS):
    Vb = [7, 182, 121, 86, 122, 92, 74, 190, 29, 241, 178, 16, 60, 94, 220, 166, 86, 231, 136, 37, 135, 149, 213, 133,
          118, 125, 234, 102, 245, 10, 195, 168, 85, 40, 103, 20, 6, 231, 203, 104, 172, 46, 0, 54, 87, 47, 210, 226,
          84, 233, 198, 163, 3, 198, 7, 51, 189, 241, 109, 70, 98, 253, 130, 207, 163, 80, 21, 178, 83, 164, 156, 147,
          152, 85, 142, 248, 193, 12, 21, 113, 66, 106, 164, 241, 93, 114, 177, 196, 246, 240, 86, 174, 202, 119, 68,
          69, 33, 27, 147, 64, 73, 137, 82, 118, 44, 100, 184, 59, 249, 141, 81, 165, 128, 44, 146, 57, 247, 173, 175,
          89, 31, 6, 222, 90, 29, 145, 28, 219, 111, 173, 193, 232, 229, 212, 180, 124, 62, 97, 115, 45, 206, 205, 1,
          223, 94, 206, 96, 183, 131, 209, 57, 169, 243, 53, 5, 186, 136, 120, 151, 252, 61, 47, 249, 54, 42, 56, 176,
          37, 22, 167, 8, 140, 246, 33, 200, 34, 188, 144, 72, 53, 154, 13, 26, 217, 250, 204, 112, 170, 66, 63, 182,
          225, 187, 65, 23, 116, 194, 72, 126, 128, 214, 9, 197, 36, 96, 48, 14, 227, 250, 146, 102, 67, 225, 138, 77,
          215, 27, 107, 35, 101, 160, 18, 157, 155, 224, 147, 229, 210, 227, 244, 220, 65, 164, 58, 16, 43, 150, 237,
          27, 30, 169, 180, 52, 17, 148, 166, 117, 52, 216, 137, 252, 79, 59, 34, 177, 167]
    txt = str(timeS) + "_" + str(Vb[timeS % len(Vb)])
    return md5_encrypt(txt).upper()

def req():
    import requests
    import json
    t = get_time()
    sign=get_sign(t)
    headers = {
        "authority": "api.7seasweb.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://www.7seasweb.com",
        "pragma": "no-cache",
        "referer": "https://www.7seasweb.com/",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sign": sign,
        "timestamp": str(t),
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    url = "https://api.7seasweb.com/api/asset/findNftPageList"
    data = {
        "page": 26,
        "size": 16,
        "filterCondition": 2
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)

    print(response.text)
    print(response)
if __name__ == '__main__':
    req()
