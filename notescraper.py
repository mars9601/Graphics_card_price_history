
from asyncio.windows_events import NULL
from genericpath import exists
from operator import contains
from bs4 import BeautifulSoup
from matplotlib.pyplot import text
from pytz import timezone
import requests
import mysql.connector
from datetime import datetime
import pytz
import lxml

def ASUS_ROG_STRIX_3070_ti():
    headers = requests.utils.default_headers()
    headers.update({"User-Agent":"Mozilla/5.0"})
    page = requests.get("https://www.notebooksbilliger.de/pc+hardware/grafikkarten/nvidia/geforce+rtx+3070+ti+nvidia/asus+rog+strix+geforce+rtx+3070+ti+oc+8gb+gddr6x+grafikkarte+720422",headers=headers)
    if page.status_code == 200:
        print('Web site exists')
        soup = BeautifulSoup(page.content,'lxml')
        naa = soup.find('div',attrs={'class':'soldOut'})
        if naa == None:
            div = soup.find('div',attrs={'class':'right_column pdw_rc'})
            rows = div.find('span',attrs={'class':'product-price__regular js-product-price'})
            rawprice = rows.contents[0]
            graka = rawprice.replace('\n','').replace(' ','').split(",")
            output = int(graka[0].replace('.', ''))
            return(output)
        else:
            print('Out of Stock')
            return(None)
    else:
        print('Web site does not exist')
        return(None)
        
def ASUS_TUF_3070_ti():
    headers = requests.utils.default_headers()
    headers.update({"User-Agent":"Mozilla/5.0"})
    page = requests.get("https://www.notebooksbilliger.de/pc+hardware/grafikkarten/nvidia/geforce+rtx+3070+ti+nvidia/asus+tuf+geforce+rtx+3070+ti+oc+8gb+gddr6x+grafikkarte+720436",headers=headers)
    if page.status_code == 200:
        print('Web site exists')
        soup = BeautifulSoup(page.content,'lxml')
        naa = soup.find('div',attrs={'class':'soldOut'})
        if naa == None:
            div = soup.find('div',attrs={'class':'right_column pdw_rc'})
            rows = div.find('span',attrs={'class':'product-price__regular js-product-price'})
            rawprice = rows.contents[0]
            graka = rawprice.replace('\n','').replace(' ','').split(",")
            output = int(graka[0].replace('.', ''))
            return(output)
        else:
            print('Out of Stock')
            return(None)
    else:
        print('Web site does not exist')
        return(None)

def ASUS_ROG_STRIX_3080():
    headers = requests.utils.default_headers()
    headers.update({"User-Agent":"Mozilla/5.0"})
    page = requests.get("https://www.notebooksbilliger.de/pc+hardware/grafikkarten/nvidia/geforce+rtx+3080+nvidia/asus+rog+strix+geforce+rtx+3080+v2+oc+10gb+gddr6x+grafikkarte+725967",headers=headers)
    if page.status_code == 200:
        print('Web site exists')
        soup = BeautifulSoup(page.content,'lxml')
        naa = soup.find('div',attrs={'class':'soldOut'})
        if naa == None:
            div = soup.find('div',attrs={'class':'right_column pdw_rc'})
            rows = div.find('span',attrs={'class':'product-price__regular js-product-price'})
            rawprice = rows.contents[0]
            graka = rawprice.replace('\n','').replace(' ','').split(",")
            output = int(graka[0].replace('.', ''))
            return(output)
        else:
            print('Out of Stock')
            return(None)
    else:
        print('Web site does not exist')
        return(None)

def ASUS_TUF_3080():
    headers = requests.utils.default_headers()
    headers.update({"User-Agent":"Mozilla/5.0"})
    page = requests.get("https://www.notebooksbilliger.de/pc+hardware/grafikkarten/nvidia/geforce+rtx+3080+nvidia/asus+tuf+gaming+geforce+rtx+3080+oc+12g+grafikkarte+755273",headers=headers)
    if page.status_code == 200:
        print('Web site exists')
        soup = BeautifulSoup(page.content,'lxml')
        naa = soup.find('div',attrs={'class':'soldOut'})
        if naa == None:
            div = soup.find('div',attrs={'class':'right_column pdw_rc'})
            rows = div.find('span',attrs={'class':'product-price__regular js-product-price'})
            rawprice = rows.contents[0]
            graka = rawprice.replace('\n','').replace(' ','').split(",")
            output = int(graka[0].replace('.', ''))
            return(output)
        else:
            print('Out of Stock')
            return(None)
    else:
        print('Web site does not exist')
        return(None)

rog70 = ASUS_ROG_STRIX_3070_ti()
tuf70 = ASUS_TUF_3070_ti()
rog80 = ASUS_ROG_STRIX_3080()
tuf80 = ASUS_TUF_3080()

print(rog70,tuf70,rog80,tuf80)


now = datetime.now()

mydb = mysql.connector.connect(
  host="192.168.111.21",
  user="mars9601",
  password="admin123",
  database="mind"
)

mycursor = mydb.cursor()

sql = "INSERT INTO notescraper (time, ASUS_ROG_STRIX_3070_ti, ASUS_TUF_3070_ti, ASUS_ROG_STRIX_3080, ASUS_TUF_3080) VALUES(%s, %s, %s, %s, %s)"
val = (now, rog70,tuf70,rog80,tuf80)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")












