import requests

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return '15846843229702'


def get_sign():
    return '675ff9174c055d8393e20bb793d78af3'


def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))

    return '1584684322970'


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
