import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "http://zxgk.court.gov.cn/shixin/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
cookies = {
    # "wzws_sessionid": "gjVmZGQ3ZIAxMTQuODQuODYuMTkzgWQ5YzU0NKBkOp48",
    "lqWVdQzgOVyaS": "5yugrEkf1py4IBnlpJKOx9_aSQycosoaM.krw6xPO78MlTmSMPgNtBo9rC290CtvgrxBXZc.WWhs9xzXaM5Chrq",
    "lqWVdQzgOVyaT": "BIyhYvn.6lKhIzbRcXeNneQgiiyyi7_uL3rB9yLTnMwK5e4RLFJEprdwWDNqy4.udZU7kdcp4rPJs2uVS2g.P.L1peBWO9NVeYVT.eNrNs0KiSj2_oI5awtgPrL80I4VND4km7JYsxI0BCsKWup5xrMt_1_5rwQtqwY7sWFwtftwbth9mPtar2cPqx8BY_T7wxQSdmpUW2Q7Le6RVDmQd9wSVu4rzSdB9ZZEvl_spSa"
}
url = "http://zxgk.court.gov.cn/shixin/"
response = requests.get(url, headers=headers, cookies=cookies, verify=False)

print(response.text)
print(response)