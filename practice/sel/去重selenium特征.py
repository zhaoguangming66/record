import time

from selenium import webdriver


def get_driver():
    # 浏览器配置对象
    options = webdriver.ChromeOptions()
    # 以开发者模式启动浏览器
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 屏蔽以开发者运行提示框
    options.add_experimental_option('useAutomationExtension', False)
    # 屏蔽保存密码提示框
    preferences = {
        "webrtc.ip_handling_policy": "disable_non_proxied_udp",
        "webrtc.multiple_routes_enabled": False,
        "webrtc.nonproxied_udp_enabled": False
    }
    # 关闭webrtc 避免找到真实IP地址
    options.add_experimental_option("prefs", preferences)
    prefs = {'credentials_enable_service': False, 'profile.password_manager_enabled': False}
    options.add_experimental_option('prefs', prefs)
    # chrome 88 或更高版本的反爬虫特征处理
    options.add_argument('--disable-blink-features=AutomationControlled')
    # 浏览器对象
    driver = webdriver.Chrome(options=options)
    # 读取脚本 下载 stealth.min.js 到本地
    with open('stealth.min.js', mode='r', encoding='utf-8') as f:
        string = f.read()
    # 移除 selenium 中的爬虫特征
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': string})
    driver.maximize_window()
    return driver


if __name__ == '__main__':
    t=time.time()
    # drvier=webdriver.Chrome()
    drvier = get_driver()
    drvier.get('https://www.zhipin.com/web/geek/job?query=%E7%88%AC%E8%99%AB&city=101020100&page=2')
    time.sleep(5)
    data=drvier.get_cookies()
    print(data)
    print(time.time()-t)