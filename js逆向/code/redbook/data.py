import requests


headers = {
    "authority": "edith.xiaohongshu.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "origin": "https://www.xiaohongshu.com",
    "pragma": "no-cache",
    "referer": "https://www.xiaohongshu.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "x-b3-traceid": "c5774bebf2998344",
    # "x-s": 'Oj5l0g4vOYZ6ZBsGOgdkZjaJO2dvZg1+OBv+ZYaUZ213',
    "x-s": 'OBkJZ6TiZgVBOBakOg5iZ6siZg9K0Y1WOiwkZg9p1g93',
    # "x-s-common": "2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1PjhIHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHUN0Z1+aHVHdWMH0ijP/WM+9bDw/+YPAYE87mf2nzhJ7ZU2BVIynlTy7b92/p7PA4iPBYAy9rMPeZIPerM+0c9+sHVHdW9H0il+0WlPAGUw/ZU+/GhNsQh+UHCHd+V8BTynpzVnfkp+DRV+L+OJrF3q943pLRxwL+OySzkPbSBa7P9pomyydGAHjIj2eWjwjQQPAYUaBzdq9k6qB4Q4fpA8b878FSet9RQzLlTcSiM8/+n4MYP8F8LagY/P9Ql4FpUzfpS2BcI8nT1GFbC/L88JdbFyrSiafp/JDMra7pFLDDAa7+8J7QgabmFz7Qjp0mcwp4fanD68p40+fp8qgzELLbILrDA+9p3JpHlLLI3+LSk+d+DJfRAyfRL+gSl4bYlqg48qDQlJFShtUTozBD6qM8FyFShPo+h4g4U+obFyLS3qd4QyaRAy9+0PFSe/B8QPFRSPopFJeHIzbkA/epSzb+t8nkn4AmQynpS2b87/sTc4BRUqgzit9Mt8nTTpAzQ2sTkanYULdkn494NLoz8a/+zLBRUa9L9qgziagW6qA8n4BRQyLM6anSiq9Es+fp/8BP9qf89q9kM4rTUnf4S8f+Uwn4fa9p8GMmAagYt8Lzl4rlQznpSzobFyoQTnflFJFl1agWMqA+l4bQ1GA4Spf8otFS3G74QyLYF+emj/LS9yobFLAYdanSk8dmn4FbQcFYnafuA8p+I8np3LoznagWA8/mD/7+gGAFRHjIj2eDjw0rEPALMP0LhweGVHdWlPsHC+eSR",
    # "x-t": "1681447153730"
    'X-t': "1681482348401"
}
cookies = {
    # "gid.ss": "gSMQ9UOnDuZwH2oRGJG6BW6e4grs67TaYpnrW+8Wmd2xCHYbKbMuNVnD3s6kCI89",
    # "smidV2": "202210091053305a5aa05bfa8d5948448c5c134fbcd4ca007cf1d97705c74b0",
    # "timestamp2": "16728033337028c0dbe5c997bbe4610339f220487e92bbbfa0ccc5078b4e194",
    # "timestamp2.sig": "EJ2EpMX6Is8ziwDYHmg-FtB_rswK5BhTAtwIYufD9VU",
    # "a1": "1857ad93a38ygpfydxop2xk0ilmkqvy5w37h0hska50000156464",
    # "webId": "9a1f689e0bcc4f5b3c413210d053e8e0",
    # "gid": "yY2W0fjqjSE0yY2W0fjq0qxMqYvkUivfClUJWT0CT8316x28TAhv28888y2K4K48ydf8Jjq2",
    # "gid.sign": "DAiDulrjBYvwC9VAND+JeJbWGrc=",
    # "xhsTrackerId": "01f86fd1-68df-4af7-a449-4950c3841ce1",
    # "xhsTrackerId.sig": "AZFEH-2WSL3ti9NxBDFS2nPNkU1N1fk8VwnLfghU8iY",
    "web_session": "030037a30bb22545e9192c2741234a2e399fc4",
    # "xsecappid": "xhs-pc-web",
    # "extra_exp_ids": "yamcha_0327_exp,h5_1208_exp3,ques_exp2",
    # "extra_exp_ids.sig": "tP-EUqmkBBQjAxiuz_uTOZ2UHKu0CJkOe3bWvplEOns",
    # "webBuild": "2.0.5",
    # "acw_tc": "286b5537595bb827a4d850eae1463d48e489e50324c10244f6439cb61a1296fa",
    # "websectiga": "10f9a40ba454a07755a08f27ef8194c53637eba4551cf9751c009d9afb564467",
    # "sec_poison_id": "9924e33c-fe27-4158-bbf6-ba4f35789030"
}
url = "https://edith.xiaohongshu.com/api/sns/web/v1/user_posted"
params = {
    "num": "30",
    "cursor": "",
    "user_id": "63621c5d000000001f01f1c1"
}
# for i in range(100):
proxies = {'https':'175.165.228.212:57738',"http":'175.165.228.212:57738' }
response = requests.get(url, headers=headers, cookies=cookies, params=params,timeout=10,proxies=proxies)

print(response.text)
print(response)