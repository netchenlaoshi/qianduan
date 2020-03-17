import requests

url="http://www.cntour.cn/"

response=requests.get(url)
print(response.text)

# soup=BeautifulSoup(response.text,'lxml')
# data=soup.select()
#
# print(data)
#
# for item in data:
#     result={
#         'title':item.get_text(),
#         'link':item.get('href')
#     }
#     print(result)