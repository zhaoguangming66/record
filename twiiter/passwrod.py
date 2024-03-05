import json

import requests
from loguru import logger

from twiiter.tw_utils import guest_token
from utils.settings import proxies

sss = requests.session()


def step1():
    x_guest_token = guest_token()
    # TheobaldMo6042----jwyd4530----bagaanmeandm@hotmail.com----Bc5Q5i46----RIFZGEID567BPCGF----ny7xf69gg97f
    headers = {
        'authority': 'api.twitter.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://twitter.com',
        'pragma': 'no-cache',
        'referer': 'https://twitter.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-guest-token': x_guest_token,

    }
    url = "https://api.twitter.com/1.1/onboarding/task.json"
    params = {
        "flow_name": "login"
    }
    data = {
        "input_flow_data": {
            "flow_context": {
                "debug_overrides": {},
                "start_location": {
                    "location": "unknown"
                }
            }
        },
        "subtask_versions": {
            "action_list": 2,
            "alert_dialog": 1,
            "app_download_cta": 1,
            "check_logged_in_account": 1,
            "choice_selection": 3,
            "contacts_live_sync_permission_prompt": 0,
            "cta": 7,
            "email_verification": 2,
            "end_flow": 1,
            "enter_date": 1,
            "enter_email": 2,
            "enter_password": 5,
            "enter_phone": 2,
            "enter_recaptcha": 1,
            "enter_text": 5,
            "enter_username": 2,
            "generic_urt": 3,
            "in_app_notification": 1,
            "interest_picker": 3,
            "js_instrumentation": 1,
            "menu_dialog": 1,
            "notifications_permission_prompt": 2,
            "open_account": 2,
            "open_home_timeline": 1,
            "open_link": 1,
            "phone_verification": 4,
            "privacy_options": 1,
            "security_key": 3,
            "select_avatar": 4,
            "select_banner": 2,
            "settings_list": 7,
            "show_code": 1,
            "sign_up": 2,
            "sign_up_review": 4,
            "tweet_selection_urt": 1,
            "update_users": 1,
            "upload_media": 1,
            "user_recommendations_list": 4,
            "user_recommendations_urt": 1,
            "wait_spinner": 3,
            "web_modal": 1
        }
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, params=params, data=data, proxies=proxies, timeout=10)
    json_res_data = response.json()
    flow_token_step_1 = json_res_data['flow_token']

    logger.info(f"step1:{json_res_data}--{flow_token_step_1}")
    step2(flow_token_step_1,x_guest_token)


def step2(flow_token: str,x_guest_token:str):
    headers = {
        "authority": "api.twitter.com",
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://twitter.com",
        "pragma": "no-cache",
        "referer": "https://twitter.com/",
        "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
         "x-guest-token": x_guest_token,

    }
    url = "https://api.twitter.com/1.1/onboarding/task.json"
    data = {
        "flow_token": flow_token,
        "subtask_inputs": [
            {
                "subtask_id": "LoginJsInstrumentationSubtask",
                "js_instrumentation": {
                    "response": "{\"rf\":{\"aaddc62bdbb45b3c81f383efeb2a5b8b4ba57115a04d01617db5bbaaf0a8de32\":0,\"ab05f243631f87157dccfcb8e0837d415f5a696907a8261a9e180b2522025125\":-1,\"a9f16c57a151a7ba01efec5439768a10bdf151ef741c194d37f1a7a362f2a74f\":0,\"a7b1e93764b2eb75525e2f94ffc4fe0fc391df716daeac842ffb50d2507132d4\":0},\"s\":\"jSxXtLvH8wpHy2Fz7HNCKcObFS4XxJFUSiyG0vreuhZdrOxrxFAtl-96S1vlMGejfzNRjTf8Ivb9mEO_-loHR-_Jz6PCAcR6LmGzZGGQDdHjHvOFK6ZSEtQ1MB_b6j9if2E01tL-5HmVEC6xLhdSlX-omMBbYzC8acb-6gqV6PK8l1aoL-5n17HxNnhqQJQA2Z7XEz-Hfy-5_vA6dZcBEKfEjp3Y_py7zJQ98KsQCu5P85AiVcZAEFF2IkxELPpRvsd0wSBilHY_-XhHNfSj9tyTbSNmT3cgcMpoe8qABa-JuN5i9Iby73TSTV1Qwtxj4PZUkfw6-r6xeGMLB79K5gAAAYhxVmpY\"}",
                    "link": "next_link"
                }
            }
        ]
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data, proxies=proxies, timeout=10)
    logger.info(f"step2:{response.json()}")


if __name__ == '__main__':
    step1()
