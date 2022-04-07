
from asyncio.windows_events import NULL
from genericpath import exists
from operator import contains
from bs4 import BeautifulSoup
from matplotlib.pyplot import text
import requests
import mysql.connector
from datetime import datetime


def get3070_ti_ventus():
  url = f'https://www.mindfactory.de/product_info.php/8GB-MSI-GeForce-RTX-3070-Ti-VENTUS-3X-OC-8G-DDR6--Retail-_1415002.html'
  page = requests.get(url)
  if page.status_code == 200:
    print('Web site exists')
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find('div',attrs={'class':'pprice'})
    naa = soup.find('div',attrs={'class':'not_available_anymore'})
    if naa == None:
      rows = div.find_all('span')
      rawprice = rows[1].text.split()
      if len(rawprice) > 1:
        graka = rawprice[1].split(",")
      else: 
        rows = div.contents[4]
        graka = rows.replace('\xa0','').split(",")
      output = int(graka[0].replace('.', ''))
      return(output)
    else:
      print('Out of Stock')
      return(None)
  else:
    print('Web site does not exist')
    return(None)
  
  
def get3070_ti_trio():
  url = f'https://www.mindfactory.de/product_info.php/8GB-MSI-GeForce-RTX-3070-Ti-GAMING-X-TRIO-Aktiv-PCIe-4-0-x16-_1415003.html'
  page = requests.get(url)
  if page.status_code == 200:
    print('Web site exists')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find('div',attrs={'class':'pprice'})
    naa = soup.find('div',attrs={'class':'not_available_anymore'})
    if naa == None:
      rows = div.find_all('span')
      rawprice = rows[1].text.split()
      if len(rawprice) > 1:
        graka = rawprice[1].split(",")
      else: 
        rows = div.contents[4]
        graka = rows.replace('\xa0','').split(",")
      output = int(graka[0].replace('.', ''))
      return(output)
    else:
      print('Out of Stock')
      return(None)
  else:
    print('Web site does not exist')
    return(None)
  

def get3080_ventus():  
  url = f'https://www.mindfactory.de/product_info.php/12GB-MSI-GeForce-RTX-3080-VENTUS-3X-PLUS-OC-LHR-GDDR6X-3xDP-1-4a-1xHDMI_1443612.html'
  page = requests.get(url)
  if page.status_code == 200:
    print('Web site exists')
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find('div',attrs={'class':'pprice'})
    naa = soup.find('div',attrs={'class':'not_available_anymore'})
    if naa == None:
      rows = div.find_all('span')
      rawprice = rows[1].text.split()
      if len(rawprice) > 1:
        graka = rawprice[1].split(",")
      else: 
        rows = div.contents[4]
        graka = rows.replace('\xa0','').split(",")
      output = int(graka[0].replace('.', ''))
      return(output)
    else:
      print('Out of Stock')
      return(None)
  else:
    print('Web site does not exist')
    return(None)
  

def get3080_trio():
  url = f'https://www.mindfactory.de/product_info.php/12GB-MSI-GeForce-RTX-3080-GAMING-Z-TRIO-LHR-GDDR6X--Retail-_1440262.html'
  page = requests.get(url)
  if page.status_code == 200:
    print('Web site exists')
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find('div',attrs={'class':'pprice'})
    naa = soup.find('div',attrs={'class':'not_available_anymore'})
    if naa == None:
      rows = div.find_all('span')
      rawprice = rows[1].text.split()
      if len(rawprice) > 1:
        graka = rawprice[1].split(",")
      else: 
        rows = div.contents[4]
        graka = rows.replace('\xa0','').split(",")
      output = int(graka[0].replace('.', ''))
      return(output)
    else:
      print('Out of Stock')
      return(None)
  else:
    print('Web site does not exist')
    return(None)
  

v70 = get3070_ti_ventus()
t70 = get3070_ti_trio()
v80 = get3080_ventus()
t80 = get3080_trio()

print(v70,t70,v80,t80)


now = datetime.utcnow()

mydb = mysql.connector.connect(
  host="192.168.111.21",
  user="mars9601",
  password="admin123",
  database="mind"
)

mycursor = mydb.cursor()

sql = "INSERT INTO mindscraper (time, RTX3070_ti_ventus, RTX3070_ti_trio, RTX3080_ventus, RTX3080_trio) VALUES(%s, %s, %s, %s, %s)"
val = (now, v70, t70, v80, t80)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
