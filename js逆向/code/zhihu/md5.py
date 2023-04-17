import requests


headers = {
    "authority": "www.zhihu.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.zhihu.com/",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "x-ab-param": "",
    "x-ab-pb": "CkYbAD8ARwC0AGkBagF0ATsCzALXAtgCtwPWBFEFiwWMBZ4FMQbrBicHdAh5CGAJ9AlrCr4KcQuHC+AL5QvmC3EMjwzDDPgMEiMAAAAAAQAAAQAAAAAEAQAAAQAAAAAGAgMAAAAAAAAABgACAA==",
    "x-api-version": "3.0.53",
    "x-requested-with": "fetch",
    "x-zse-93": "101_3_3.0",
    # "x-zse-96": "2.0_4cciLOKzNqfcP2i6I2Il8vqkfB+Pet8fjFQtPNH9bQh9Z=6bk5JeDJp4usaXfqqV"
}
cookies = {
    "_zap": "36627082-5d43-41fd-b3aa-52d4040cc65b",
    "d_c0": "\"AIBRdNC9BhWPToawSHkd7XMYmoEcCgzF4t0=|1654009664\"",
    "_xsrf": "Ec5WPpP4D6EXIXs46mC7NZjMF49ogZXa",
    "__snaker__id": "5wHp42MyKSsNCfjG",
    "_9755xjdesxxd_": "32",
    "YD00517437729195%3AWM_TID": "aOL%2FwoQEhG9FAQBEAVaFFhwjRJyA2hcG",
    "q_c1": "8c5f3211766944e1b5c06dca6e253c44|1654339679000|1654339679000",
    "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1658905291",
    "YD00517437729195%3AWM_NI": "ydOY9wr5OdJmwV7D9go0pLJTNyrli1B1izrX8RJ6ZbHEHx6VwHFQeP9r9TIifaWmJsb5tOQK9yiXwoNpuI%2B8drW3WXP7uMSg%2BVo3bf53iX52GrA87lZrPGIkNus4MCVdTUY%3D",
    "YD00517437729195%3AWM_NIKE": "9ca17ae2e6ffcda170e2e6eeb8e47a8bb88f88f15ef8b88fb6c84e938e9ab0d842edacad9ad074bab2c0ccd12af0fea7c3b92abbbc81babc7db2eb8185c967b58af9a5bc6dadf0c0adc9608ea7be8dec3b82efa79bf154fc8e86d7d96a8c9b8899b55eb5988ab2e85cfbaef7b5cc63a6bf998ec979a2ebbcb0d441fba7a7b9f6658eb0bbaaaa34a8ae99d4d65494e9bbaed26de98aa1d4e16ef7eda7b9b83a85ae8fd9b6689aaea0a8cc618eabbdd5d04996bc9cb6dc37e2a3",
    "z_c0": "2|1:0|10:1680062327|4:z_c0|80:MS4xcVN4R0NnQUFBQUFtQUFBQVlBSlZUWGNGRVdWRmFNdkdOX09YVUxSZmdjVnRmalh5b2hvSnd3PT0=|1a2bbf135783a984f818bf018b1c60711155f18c1058d17a92e37c857738b91d",
    "tst": "r",
    "SESSIONID": "wEzgH3jYh2f3zkA2qRnHNZDKHEDgOsDXRhyENtgc1fv",
    "KLBRSID": "f48cb29c5180c5b0d91ded2e70103232|1681535966|1681531403"
}
url = "https://www.zhihu.com/api/v3/feed/topstory/recommend"
params = {
    "action": "down",
    "ad_interval": "3",
    "after_id": "17",
    "desktop": "true",
    "page_number": "4",
    "session_token": "0d021fd9d16f5e6409526dd0263b79a5"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)