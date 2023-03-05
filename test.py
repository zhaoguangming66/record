import requests
from curl_cffi import requests as eq


headers = {
    "authority": "mvnrepository.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
cookies = {
    "MVN_SESSION": "eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InVpZCI6IjU1NTdiMzMwLTA1OGEtMTFlZC1iMTRiLWM1OWRiMTVjMjg3ZCJ9LCJleHAiOjE3MDk0ODA2MjgsIm5iZiI6MTY3Nzk0NDYyOCwiaWF0IjoxNjc3OTQ0NjI4fQ.LRlGfLCgi-fPu6ptOxPb2NoduNIau_lgAryF5otC3p0",
    "__cf_bm": "t184.90J_dC62hBy.EdAo6lE5Bdo9nXaERA5Q6rhXm4-1677944630-0-AdELEBE+faAYD8GtQuoncSpWxoMdjb5Lx5rBIXVctrsHIm38lBtooGMqKW/CO5g3axI+nSVTbpC6J2KX8KuakCdq0XU2PTPO3b3BYP0tgDNyMeFKqXf0MK55D1IqgMngrqSgRG/HnthIZbsX8uxoTB7VpFJcc9M0UbUVBuTE9kvxJRhGL43shtOrjK0FarqLVg=="
}
url = "https://mvnrepository.com/"
response = eq.get(url,impersonate="chrome101")

print(response.text)
print(response)