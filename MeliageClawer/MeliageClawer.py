from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import sql
import re

gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
html = urlopen("https://www.ana.co.jp/wws/us/e/asw_common/amc/reference/tameru/flightmile/dom/chart.html",context=gcontext)
bs = BeautifulSoup(html,"lxml")
cities = bs.findAll("div",{"class":"toggle-box"})
DBM = sql.MileageDBManager()
for city in cities:
    print(city["id"])
    DBM.insertNewCity(city["id"])
    temp = city.findAll("tr")
    for a in temp:
        data = list(a.findAll("td"))
        #print(data)
        if data.__len__() == 6:
            DBM.insertNewConnectData(city["id"],data[0].text,int(re.sub(",","",data[1].text),10),int(data[2].text,10),int(data[3].text,10))

print(DBM.isInCityList("abc"))
