import requests
import json
import random
import time

config = json.load(open('./config.json'))
game_version = config["game_version"]
authkey = config["authkey"]
prop = config["prop"]

def getRandChar(n):
    l = []
    sample = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #sample = random.sample(string.ascii_letters + string.digits, 62)
    #sample = sample + list('!@#$%^&*()-+=.')
    for i in range(n):
        char = random.choice(sample)
        l.append(char)
    return ''.join(l)

if prop == 1:
    cdkey = input("请输入cdkey:")
    url = 'https://hk4e-api.mihoyo.com/common/apicdkey/api/exchangeCdkey?sign_type=2&auth_appid=apicdkey&authkey_ver=1&cdkey=' + cdkey + '&lang=zh-cn&device_type=pc&game_version=' + game_version + '&plat_type=pc&authkey=' + authkey + '&game_biz=hk4e_cn'
    headers = {"User-Agent": "UnityPlayer/2017.4.30f1 (UnityWebRequest/1.0, libcurl/7.51.0-DEV)",
               "Accept": "*/*",
               "Accept-Encoding": "identity",
               "X-Unity-Version": "2017.4.30f1"
              }
    res = requests.get(url=url,headers=headers)
    res = json.loads(res.text)
    if res['retcode']!=0:
        print('兑换失败，错误信息：%s，错误码：%d' %(res['message'],res['retcode']))
    else :
        print('兑换成功，兑换码为：%s' %(cdkey))
else:
    times = input('请输入穷举次数:')
    times = int(times)
    for i in range(times):
        cdkey = getRandChar(12)
        print(cdkey)
        url = 'https://hk4e-api.mihoyo.com/common/apicdkey/api/exchangeCdkey?sign_type=2&auth_appid=apicdkey&authkey_ver=1&cdkey=' + cdkey + '&lang=zh-cn&device_type=pc&game_version=' + game_version + '&plat_type=pc&authkey=' + authkey + '&game_biz=hk4e_cn'
        headers = { 
                    "User-Agent": "UnityPlayer/2017.4.30f1 (UnityWebRequest/1.0, libcurl/7.51.0-DEV)",
                    "Accept": "*/*",
                    "Accept-Encoding": "identity",
                    "X-Unity-Version": "2017.4.30f1"
                  }
        res = requests.get(url=url,headers=headers)
        res = json.loads(res.text)
        if res['retcode']!=0:
            print('兑换失败，错误信息：%s，错误码：%d' %(res['message'],res['retcode']))
            time.sleep(5)
        else :
            print('兑换成功，兑换码为：%s' %(cdkey))
            time.sleep(5)        
