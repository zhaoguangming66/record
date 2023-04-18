// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function tripleAesEncrypt(text) {
    var key = CryptoJS.enc.Utf8.parse("BE45D593014E4A4EB4449737660876CE"),
        iv = CryptoJS.enc.Utf8.parse("A8909931867B0425"),
        srcs = CryptoJS.enc.Utf8.parse(text),
        // CBC 加密方式，Pkcs7 填充方式
        encrypted = CryptoJS.AES.encrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
    return encrypted.toString();
}

function tripleAesDecrypt(text) {
    var key = CryptoJS.enc.Utf8.parse("BE45D593014E4A4EB4449737660876CE"),
        iv = CryptoJS.enc.Utf8.parse("A8909931867B0425"),
        srcs = text,
        // CBC 加密方式，Pkcs7 填充方式
        decrypted = CryptoJS.AES.decrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
    return decrypted.toString(CryptoJS.enc.Utf8);
}
