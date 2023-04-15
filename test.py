import requests


headers = {
    "authority": "www.xiaohongshu.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.xiaohongshu.com/website-login/captcha?redirectPath=https%3A%2F%2Fwww.xiaohongshu.com%2Fuser%2Fprofile%2F565935b0e4251d536ad33629",
    "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
cookies = {
    "xhsTrackerId": "8d99b03a-2e9f-4974-8905-0e435172e078",
    "xhsTrackerId.sig": "bcosZD2uhdbEJW7ysERZnV61DL-1Ycr0aogwTZGqL9A",
    "extra_exp_ids": "yamcha_0327_clt,h5_1208_exp3,ques_exp1",
    "extra_exp_ids.sig": "vC5QSaNvPIi3rt1fMq2Z7QzeL4L1xFj01zjqPbvZPX0",
    "xsecappid": "login",
    "a1": "1877e438d77r52yhf8bgbhqndet6btmdsyyq0oryi50000600444",
    "webId": "17541332485a9892d3cd6cbade492573",
    "websectiga": "3fff3a6f9f07284b62c0f2ebf91a3b10193175c06e4f71492b60e056edcdebb2",
    "sec_poison_id": "7dbbd312-23bb-4319-af86-1135f09f7010",
    "smidV2": "20230414133609335b11e7e4c89a86a213f19d85f24d6200360f9792f46b980",
    "gid": "yYWWd4qj8dMdyYWWd4qYfvlFWWF2JvxiYDkDvv3xAIfd9A28KD96f8888K884448idyjqjqi",
    "gid.sign": "l8l6VxJc6YYb69Z/MQKd4ENct7U="
}
url = "https://www.xiaohongshu.com/user/profile/565935b0e4251d536ad33629"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.headers)
print(response)