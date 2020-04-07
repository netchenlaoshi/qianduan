import requests
import time
import random

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    s=str(random.randint(0,10))
    t=get_ts()
    # print("random=",s)
    # print("ts=",t)
    # print("salt=",t+s)
    return t+s
    #return '15846843229702'


def get_sign():
    return '675ff9174c055d8393e20bb793d78af3'


def get_ts():
    t=time.time()
    ts=str(int(round((t*1000))))
    return ts
    #return '1584684322970'


form_data = {
    'i': '我和你',
    'from': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': '901200199a98c590144a961dac532964',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
response=requests.post(url, data=form_data)
print(response.text)
