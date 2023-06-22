import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://ldggzy.hnloudi.gov.cn",
    "Pragma": "no-cache",
    "Referer": "http://ldggzy.hnloudi.gov.cn/siteapps/webpage/page/web/ldcx/gcjs.jsp?id=1&type=2",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
cookies = {
    "JSESSIONID": "887D1133E95BF2476DE745A2F4CCF389",
    "mq4qQammP3BAe0a8": "0728e8f720132ba39eb9d4455a4d15ff",
    "_gscu_204172796": "864501510pb6xl59",
    "_gscbrs_204172796": "1",
    "_gscs_204172796": "86450151cjctxb59|pv:1",
    "yfx_c_g_u_id_10000062": "_ck23061110223113811383030313389",
    "yfx_f_l_v_t_10000062": "f_t_1686450151379__r_t_1686450151379__v_t_1686450151379__r_c_0",
    "arialoadData": "true",
    "1xL8nvQydGCE0KeX": "OVY1RmJ3NmRydWxMd1lyTfZldGvC/mAkhac1+oueiYF+YLjE8EYJ3hlMpWIgoKpTGOq9Lpp0G3VxAfrWisHEaJw2Fvkyr3ArVoOFW5RR/7nMqVZfBbBQW/uzvPXxdNFAcqKCqjrHptxbIqSEnHz2dJ9htXjyDOgbhcnxi9lXsRMViByl5JS0XF7OXeAfaQv8+/uKwmUQmpxA3fxA7FHmLH+R+NkXORXj6YFX2Y5EDmU/4VRtvDea5pFWCQcKkVh/LHJaMA8YGjIuqRaaGSy/F+Kht3DaaRBICS1t8szjuleO2dHynNyCO184o2PY9epoE44WUU/9iN1uanCqKJwOQIbpjxfoiGOgwnJbBzGqpxl4VC5TKQEiVxs3NCQgLSMQ4ijQ4j3bxd4vzZ1gZWORaA=="
}
url = "http://ldggzy.hnloudi.gov.cn/siteapps/webpage/page/web/ldcx/gcjs.jsp"
params = {
    "id": "1",
    "type": "2"
}
data = {
    "region": "",
    "key": "",
    "id": "1",
    "type": "2",
    "thisPage": "4"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data, verify=False)

print(response.text)
print(response.headers)