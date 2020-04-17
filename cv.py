import requests
from bs4 import BeautifulSoup as BS
import codecs
import time

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
url = 'https://www.cv.ee/toopakkumised/harjumaa/infotehnoloogia'
req = session.get(url, headers=headers)


if req.status_code == 200:
    bsObj = BS(req.content, "html.parser")

    div = bsObj.find('div', attrs={'class': 'cvo_module_offer_content'})



handle = codecs.open('cv.html', "w", 'utf-8')
handle.write(str(div.contents))
handle.close()
