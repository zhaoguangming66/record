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
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "x-b3-traceid": "1233b72847c45721",
    "x-s": "siMGO2qBZ6TKZBkUsYFL16TGs6qk0YOvZ6OksB5GOis3",
    # "x-s-common": "2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1PjhIHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHUN0Z1+aHVHdWMH0ijP/W7+9HUPAHEPA8CPem3+nYM2oPI49S74d+T+f+AqgbUyAHhqepAJ0HMPeZIPePh+ArAPsHVHdW9H0il+0WlPADhP0rEP/HlNsQh+UHCHd+k/L4OPdbsn08LaMksyMpAnL8PP/8Lz7P9qnVInLR9n08Oy7+s+L4OygPAHjIj2eWjwjQQPAYUaBzdq9k6qB4Q4fpA8b878FSet9RQzLlTcSiM8/+n4MYP8F8LagY/P9Ql4FpUzfpS2BcI8nT1GFbC/L88JdbFyrSiafprwLMra7pFLDDAa7+8J7QgabmFz7Qjp0mcwp4fanD68p40+fp8qgzELLbILrDA+9p3JpHlLLI3+LSk+d+DJfRAyfRL+gSl4bYlqg48qDQlJFShtUTozBD6qM8FyFShPo+h4g4U+obFyLS3qd4QyaRAy9+0PFSe/B8QPFRSPopFJeHIzbkA/epSzb+t8nkn4AmQynpS2b87/sTc4BRUqgziLrSN8gY8wBRQcMHlaLpUL94n4FQoqgzaagYbGnpr8Bpn4g4xaLPIqAbl4BEQy7mNanYrqfpSP7+8q7H9GMLMqMSl4okYzBzS8dklPgkDN9pgpF8wagW68n8M4oSQznpS8SmFzfRVy/4OJM8oag8d8nSl4oL6nn4S2BklJLS3/o4QyLzcz9bTyDS9yBF3a/WhanSC4LQn49lQ4D4B+Bp98Lz/+9Ll4gzeaLP7qFz0O/FjNsQhwaHC+/rF+0cEweclNsQhP/Zjw0HMKc==",
    "x-t": "1681398219121"
}
cookies = {
    # "xhsTrackerId": "89eb44ca-147d-4168-a5a9-1f9f6ce77fdc",
    # "xhsTrackerId.sig": "Xirc1iAO4xq-6_NTGmdZnOCYTwbEwbApZnE2mxo5W8I",
    # "extra_exp_ids": "yamcha_0327_clt,h5_1208_exp3,ques_exp2",
    # "extra_exp_ids.sig": "R9-3fNlUKJgR5JjIEKiebpE30kz-x61IiZc29dZTIJw",
    # "websectiga": "7750c37de43b7be9de8ed9ff8ea0e576519e8cd2157322eb972ecb429a7735d4",
    # "sec_poison_id": "6ab9057a-f9e5-4a29-a1dc-4a46b2209e83",
    # "webBuild": "2.0.5",
    # "xsecappid": "xhs-pc-web",
    # "a1": "1877b232936z00k5huxs0wiwvsm6csqqrk28p5sn250000387130",
    # "webId": "549de2eb2caf56ca3c6f3cfbfdec5e82",
    # "gid": "yYWWDJqqKKFfyYWWDJqJjT2MqKu88T2x7CM8JIJE3EhM6Y28KSMAAU888qYWyq882yYySjyY",
    # "gid.sign": "JddJkAFhPqBbVU1zvcWdAYrropg=",
    "web_session": "030037a30b4d1845d1d1205f40234a90b9d651"
}
url = "https://edith.xiaohongshu.com/api/sns/web/v1/feed"
data = {
    "source_note_id": "63f5e7be0000000013013874"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)