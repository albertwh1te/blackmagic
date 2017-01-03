 # utils for crawler  and etc
import requests

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control':'no-cache',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    # 'Host': 'xueqiu.com',
    'Upgrade-Insecure-Requests': '1',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'}
    # 'Cookie':'s=2wm617ttsk; __utma=1.249544209.1466925920.1466925920.1476342801.2; __utmz=1.1466925920.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); xq_a_token=eede0debf432b63396da4e0ca2e05cfb9506e1cc; xq_r_token=9a57bb72fa5dfc3705ad8861a649e6b4d8f4b6e7; Hm_lvt_1db88642e346389874251b5a1eded6e3=1476342763,1476517717; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1476517717;'}
