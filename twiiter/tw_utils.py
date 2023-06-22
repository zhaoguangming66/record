import json

import requests
from loguru import logger

from utils.settings import proxies


def guest_token():
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    }
    for i in range(5):
        try:
            url_token = 'https://api.twitter.com/1.1/guest/activate.json'
            token = json.loads(requests.post(url_token, headers=headers, proxies=proxies, timeout=10).text)[
                'guest_token']
            logger.info(f"获取到{token}---")
            return token
        except Exception as e:
            logger.info(f"获取token--{e}")

if __name__ == '__main__':
    data = guest_token()
    print(data)