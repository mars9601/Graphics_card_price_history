
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
import random
from requests_html import HTMLSession
from time import sleep

delay = random.randint(1,10800)
#sleep(delay)


user_agents = ["Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.26.4 (KHTML, like Gecko) Version/4.1 Safari/532.26.4",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/5362 (KHTML, like Gecko) Chrome/40.0.877.0 Mobile Safari/5362",
            "Opera/9.75 (Windows CE; en-US) Presto/2.11.228 Version/12.00",
            "Opera/8.94 (Windows 95; en-US) Presto/2.8.269 Version/11.00",
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/5351 (KHTML, like Gecko) Chrome/38.0.894.0 Mobile Safari/5351",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_1 rv:3.0; en-US) AppleWebKit/531.3.6 (KHTML, like Gecko) Version/4.0.5 Safari/531.3.6",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_3 rv:5.0; en-US) AppleWebKit/533.30.2 (KHTML, like Gecko) Version/4.0 Safari/533.30.2",
            "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/3.1)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.01) AppleWebKit/534.24.4 (KHTML, like Gecko) Version/5.0.5 Safari/534.24.4",
            "Mozilla/5.0 (iPad; CPU OS 8_0_2 like Mac OS X; sl-SI) AppleWebKit/531.13.3 (KHTML, like Gecko) Version/4.0.5 Mobile/8B115 Safari/6531.13.3"
            ]

ASUS_ROG_STRIX_3070_ti = "https://www.notebooksbilliger.de/pc+hardware/grafikkarten/nvidia/geforce+rtx+3070+ti+nvidia/asus+rog+strix+geforce+rtx+3070+ti+oc+8gb+gddr6x+grafikkarte+720422"
ASUS_TUF_3070_ti = "https://www.notebooksbilliger.de/pc+hardware/grafikkarten/nvidia/geforce+rtx+3070+ti+nvidia/asus+tuf+geforce+rtx+3070+ti+oc+8gb+gddr6x+grafikkarte+720436"
ASUS_ROG_STRIX_3080 = "https://www.notebooksbilliger.de/pc+hardware/grafikkarten/nvidia/geforce+rtx+3080+nvidia/asus+rog+strix+geforce+rtx+3080+v2+oc+10gb+gddr6x+grafikkarte+725967"
ASUS_TUF_3080 = "https://www.notebooksbilliger.de/pc+hardware/grafikkarten/nvidia/geforce+rtx+3080+nvidia/asus+tuf+gaming+geforce+rtx+3080+oc+12g+grafikkarte+755273"



def get_url_content(arg1,arg2):
    now = datetime.utcnow()
    name = arg2
    session = HTMLSession()
    headers = requests.utils.default_headers()
    headers.update({"User-Agent":random.choice(user_agents)})
    page = session.get(arg1,headers=headers)
    if page.status_code == 200:
        print('Web site exists')
        soup = BeautifulSoup(page.content,"lxml")
        naa = soup.find('div',attrs={'class':'soldOut'})
        if naa == None:
            div = soup.find('div',attrs={'class':'right_column pdw_rc'})
            if div == None:
                print('User-Agent not compatible')
                with open("log.txt", "a+") as f:
                    eco = str(now)+" "+str(name)+" User-Agent not compatible\n"
                    f.write(str(eco))
                return(None)
            else:
                rows = div.find('div',attrs={'class':'product-price__wrapper'})
                rawprice = rows.text
                graka = rawprice.replace('\n','').replace(' ','').split(",")
                output = int(graka[0].replace('.', ''))
                with open("log.txt", "a+") as f:
                    eco = str(now)+" "+str(name)+" "+str(output)+"\n"
                    f.write(str(eco))
                return(output)
        else:
            print('Out of Stock')
            with open("log.txt", "a+") as f:
                eco = str(now)+" "+str(name)+" Out of Stock\n"
                f.write(str(eco))
            return(None)
    else:
        print('Web site does not exist')
        with open("log.txt", "a+") as f:
            eco = str(now)+" "+str(name)+" Web site does not exist\n"
            f.write(str(eco))
        return(None)
        

rog70 = get_url_content(ASUS_ROG_STRIX_3070_ti,"ASUS_ROG_STRIX_3070_ti")
tuf70 = get_url_content(ASUS_TUF_3070_ti,"ASUS_TUF_3070_ti")
rog80 = get_url_content(ASUS_ROG_STRIX_3080,"ASUS_ROG_STRIX_3080")
tuf80 = get_url_content(ASUS_TUF_3080,"ASUS_TUF_3080")

now = datetime.utcnow()

print(rog70,tuf70,rog80,tuf80)


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












