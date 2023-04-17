import requests
import json


headers = {
    "authority": "edith.xiaohongshu.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
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
    "x-b3-traceid": "73dbe080e40d5dea",
    "x-s": "O2Tp0gvGs2spOBT+sisLsgT+Z25CZ2w6OgV6slAKsjv3",
    # "x-s-common": "2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1PjhIHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHUN0Z1+aHVHdWMH0ijP/W7+9chP/W9P/pAJArhJA47J9kFPBQdy7mjq/zU4Apk20SVJAHhGfrMPeZIPePl+0c9+aHVHdW9H0il+0Wl+ecE+0Hl+0qlNsQh+UHCHDuUpoZI878oqAQAqrRspsTAyg+Pq94LtMiU+L+yPdq9/94n+d+VcLTAydGAHjIj2eWjwjQQPAYUaBzdq9k6qB4Q4fpA8b878FSet9RQzLlTcSiM8/+n4MYP8F8LagY/P9Ql4FpUzfpS2BcI8nT1GFbC/L88JdbFyrSiafprwLMra7pFLDDAa7+8J7QgabmFz7Qjp0mcwp4fanD68p40+fp8qgzELLbILrDA+9p3JpHlLLI3+LSk+d+DJfRAyfRL+gSl4bYlqg48qDQlJFShtUTozBD6qM8FyFShPo+h4g4U+obFyLS3qd4QyaRAy9+0PFSe/B8QPFRSPopFJeHIzbkA/epSzb+t8nkn4AmQynpS2b87/sTc4BRUqgzi47kt8nTTpAzQ2sTkanYULdkn494NLoz8a/+zLBRUa9L9qgziagW6qA8n4BRQyLM6anSiq9Es+fp/8BP9qf89q9kM4rTUnf4S8f+Uwn4fa9p8GMmAagYt8p+n4BEQz/8S8opFagQTpDpF+Fl1agWMqA+l4bQ1GA4Spf8otFS3G74QyLYF+emj/LS9yobFLAYdanSk8dmn4FbQcFYnafuA8p+I8np3LoznagWA8/mxaeFjNsQhwaHCN/ch+AqFPAqINsQhP/Zjw0YR",
    "x-t": "1681449621671"
}
cookies = {
    # "xhsTrackerId": "eef325c5-631c-4631-9fb7-e8db6c8cd573",
    # "xhsTrackerId.sig": "p5zlTDKbRXbhlc9SEpXOi7OS6Fw-XFgppvMpnvJIuzY",
    "a1": "1877d818615so18o7wojt0bgkpbq4rw5iz9lo28ba50000316465",
    "webId": "17541332485a9892d3cd6cbade492573",
    # "smidV2": "202210091053305a5aa05bfa8d5948448c5c134fbcd4ca007cf1d97705c74b0",
    "gid": "yYWWfYyYWq3JyYWWfYyYKuJYy2MlyYlWElV9jD08DkTUD128A4FE2l888qyK4K284iiqDdi2",
    # "gid.sign": "lfimEOT21FlroDzP7tsQSwJe058=",
}
url = "https://edith.xiaohongshu.com/api/sns/web/v1/login/activate"
data = {}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)