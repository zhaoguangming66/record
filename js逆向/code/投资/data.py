import execjs
import requests
import json

def get():
    file = """
    function get_sign() {
    var sig = "";
    var chars = "0123456789abcdef";
    var curTime = parseInt(Math.random() * (9999 - 1000 + 1) + 1000) + "" + Date.parse(new Date());
    sig = chars.charAt(parseInt(Math.random() * (15 - 15 + 1) + 10)) + chars.charAt(curTime.length) + "" + curTime;
    var key = "";
    var keyIndex = -1;
    for (var i = 0; i < 6; i++) {
        var c = sig.charAt(keyIndex + 1);
        key += c;
        keyIndex = chars.indexOf(c);
        if (keyIndex < 0 || keyIndex >= sig.length) {
            keyIndex = i;
        }
    }
    var timestamp = parseInt(Math.random() * (9999 - 1000 + 1) + 1000) + "_" + key + "_" + Date.parse(new Date());
    t = timestamp.replace(/\+/g, "_");
    var tkey = "";
    var tkeyIndex = -1;
    for (var i = 0; i < 6; i++) {
        var c = timestamp.charAt(tkeyIndex + 1);
        tkey += c;
        tkeyIndex = chars.indexOf(c);
        if (tkeyIndex < 0 || tkeyIndex >= timestamp.length) {
            tkeyIndex = i;
        }
    }
    return "?s=" + sig + "&t=" + t  + "&o=" + tkey
}
    
    """
    ctx = execjs.compile(file)
    data = ctx.call("get_sign")
    return data


def req():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    sign=get()
    url = "http://tzxm.jxzwfww.gov.cn/icity/api-v2/jxtzxm.app.icity.ipro.IproCmd/getDisplayListByPage" + sign
    data = {
        "page": "2",
        "rows": "10",
        "type": "0",
        "projectName": "",
        "projectCode": ""
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data, verify=False)

    print(response.text)
    print(response)
if __name__ == '__main__':
    req()