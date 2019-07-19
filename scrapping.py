# import requests
# from bs4 import BeautifulSoup
#
url = "https://opendata.city-adm.lviv.ua/dataset/zasidannia-04-04-2019"

def collect_all_href(tag):
    arr=[]
    for i in range(len(tag)):
        arr.append(str(tag[i]).split()[2].replace('href="/dataset/zasidannia-04-04-2019', url)[:-1] + "/download/gol" + str(tag[i]).split()[4][:-1] + "_p" +str(tag[i]).split()[6][:-2])

    #print(len(arr))                                      #193

    return arr


# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, 'html.parser')
#
# a = soup.findAll('a', {"class":"heading"})
# print(a[0])
# print(str(a[0]).split()[4][:-1])
# print(str(a[0]).split()[6][:-2])




