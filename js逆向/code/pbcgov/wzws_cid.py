import re
from urllib.parse import urljoin

import execjs
import requests
sss=requests.session()
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
cookies = {
}
url = "http://www.pbc.gov.cn/rmyh/105208/8532/index2.html"
response = sss.get(url, headers=headers, cookies=cookies, verify=False)
data = re.search("W\(g,v\);}(.*?)function", response.text, re.S).group(1)
print("------------第一次---------------------")
js_code = """
function y() {
    var P = 0;
    var k = 0;
    for (k = 0; k < M.length; k++) {
        P += M['charCodeAt'](k);
    }
    P *= t
    P += 111111
    return 'WZWS_CONFIRM_PREFIX_LABEL' + P
}

function I(v) {
    var u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
    var k = v.length
        , P = '';

    for (var C = 0; C < k;) {
        if ('pPXss' !== 'xZvzW') {
            var x = v['charCodeAt'](C++) & 255;
            if (C == k) {
                if ("okqwf" !== "okqwf") {
                    // SHA
                } else {
                    P += u["charAt"](x >> 2),
                        P += u['charAt']((x & 3) << 4),
                        P += '==';
                    break;
                }
            }
            var d = v['charCodeAt'](C++);
            if (C == k) {
                P += u['charAt'](x >> 2),
                    P += u['charAt'](((x & 3) << 4) | ((d & 240) >> 4)),
                    P += u['charAt']((d & 15) << 2),
                    P += '=';
                break;
            }
            var N = v['charCodeAt'](C++);
            P += u['charAt'](x >> 2),
                P += u['charAt'](((x & 3) << 4) | ((d & 240) >> 4)),
                P += u['charAt'](((d & 15) << 2) | ((N & 192) >> 6)),
                P += u['charAt'](N & 63);
        } else {
            // dsha
        }
    }
    return P;

}
function  get_url(){
    data = y()
    ccc = I(data)
    return Q+'?wzwschallenge=' +ccc
}
"""
abs_code = data + js_code
compile_result = execjs.compile(abs_code)
result = compile_result.call('get_url')
new_url = urljoin(url, result)
new_ck = response.cookies.get_dict()
print(new_ck)
response = requests.get(new_url, headers=headers ,cookies=new_ck,allow_redirects=False,verify=False)
print("------------第二次--------------")
print(response.request.headers)
print(response.cookies.get_dict())
fin_ck = {
    'wzws_sessionid':new_ck.get("wzws_sessionid"),
    'wzws_cid':response.cookies.get_dict().get('wzws_cid')
}
print(fin_ck)
# print(fin_ck)
response = requests.get(url, headers=headers,cookies=fin_ck, verify=False)

print(f"--------------第三次-----------------")
print(response.request.headers)
print(response.content.decode())
