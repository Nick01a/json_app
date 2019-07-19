import urllib.request, json
import scrapping
import requests
from bs4 import BeautifulSoup

url = "https://opendata.city-adm.lviv.ua/dataset/zasidannia-04-04-2019"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

a = soup.findAll('a', {"class":"heading"})



def collect_all_json(href_arr):
    arr=[]
    for i in range(len(href_arr)):
        with urllib.request.urlopen(href_arr[i]) as url:
            data = json.loads(url.read().decode())
            data = [data]
            arr.append(data)
    return arr

# with urllib.request.urlopen(scrapping.collect_all_href(a)[0]) as url:
#     data = json.loads(url.read().decode())
#     # print(data)
#     data = [data]
#     # print(data)
#     data.append(scrapping.collect_all_href(a)[1])


# print(collect_all_json(scrapping.collect_all_href(a)))
#
with open('data_test.json', 'w', encoding='utf8') as json_f:
    json.dump(collect_all_json(scrapping.collect_all_href(a)), json_f, ensure_ascii=False)

