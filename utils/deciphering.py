import hashlib
import time
import binascii
from pyDes import des, CBC, PAD_PKCS5
from Crypto.Cipher import AES


def get_time():
    return int(time.time() * 1000)


def md5_encrypt(text):
    md5 = hashlib.new('md5', text.encode('utf-8'))
    return md5.hexdigest()


def sha1_encrypt(text):
    sha1 = hashlib.sha1()
    sha1.update(text.encode('utf-8'))
    print(sha1.hexdigest())


def des_encrypt(key, text, iv):
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(text, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_decrypt(key, text, iv):
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(text), padmode=PAD_PKCS5)
    return de


# 需要补位，str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)


# 需要加密的字符串
def aes_encrypt(data, key):
    # 初始化加密器
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return aes.encrypt(data.encode('utf-8'))


# 解密数据
# decrypted_data = aes.decrypt(base64.b64decode(encrypted_data)).decode('utf-8')


if __name__ == '__main__':
    print(aes_encrypt(
        "qz4LbW++jEmQhEUD+xAljyIWADB3Ns44ksZfKr6Udf0u6cVUJT2gzD18ofqFYlixgCxwV/R4x3cS2UU3Wk/wrCd/TR4Py2QGXdysXCZOgik+mwSgFiEvRaOJzZ+lMlUen0zA0uHPYgVhYA/YmyTxKzE+T4KYAICYhfjG7WQdIp+S7nwnqOId2XrmKMkzbh/KLOz0Vb+B1GSMt710uign14bd3/X8a6M7ub55hgQWuDqODz/FsaY+GtH50iSS1wxLSYhr5gnhW//qCrup5eIxDuFu4/2WRFAe5Ejp5QmG0nuuYdvtYvDrsBTjS+BtFII77J5MdswyARxS28s6VQAeHwWtoQ+DKFqiXhqX1GKMbL1xUFSoC/q16HZ9RtnHsV0FL+ryYE2Fq2JflDhkcMxfb5k91UKNMH7ldzbIl5UaddhrqxKbXtWu/lfl7HVjIqFrbh3oGMICac7XI0w+TP3uTGrJahpN/U56O0JIX176Os4yBt/2C4HTblWixGSj7IjrZvPXX42qo7xUl3s2lc9Tj+xbsGvKCeFp9VsyO0LuaekCAOjyTPIf2fiOj/WCHxBMulr589/L9jekX9XowUUmnB/rQb938rWbu3c648qat9HfRWBJ34jA5QezszMsL38hyiWLh1WMYCKTiYSSt6O/V8j+oeh7usL1Y5zj9EbuRxzZQ3rh2Nvpy3tVbDtwZVoyQqjid/uYnPjC6olU6hLwCpVEIWZYCZvzeX4jjqiHIKpBCwyMJhoqoNBc11TV2m3T",
        "OICYELAKFRATEYZW"))