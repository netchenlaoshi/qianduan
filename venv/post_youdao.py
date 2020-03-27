import requests

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data = {
    'i': '我和你',
    'from': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15846843229702',
    'sign': '675ff9174c055d8393e20bb793d78af3',
    'ts': '1584684322970',
    'bv': '901200199a98c590144a961dac532964',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
response=requests.post(url, form_data)
print(response.text)
