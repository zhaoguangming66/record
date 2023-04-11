import hashlib
import time


def get_time():
    return int(time.time() * 1000)

def md5_encrypt(text):
    md5 = hashlib.new('md5', text.encode('utf-8'))
    return md5.hexdigest()





if __name__ == '__main__':
    print(md5_encrypt('1681132670586_222'))
