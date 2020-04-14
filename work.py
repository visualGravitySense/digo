import requests
from bs4 import BeautifulSoup as BS
import codecs
import time

session = requests.Session()
headers = {'User-Agent': 'Safari/12.1.2 (MacOS Mojave 10.14.6) Gecko/20100101 Firefox/47.0',
            'Accept':'text/html,application/xhtml+xml,application/xhtml;q=0.9,*/*;q=0.8'
        }
url = 'https://www.work.ua/jobs-kyiv-python'
req = session.get(url, headers=headers)
if req.status_code == 200:
    bsObj = BS(req.content, "html.parser")
    div = bsObj.find('div', attrs={'class': 'job-link'})
    print(div.find('h2').text)
# data = bsObj.prettify()#.encode('utf8')

handle = codecs.open('div.html', "w", "utf-8")
handle.write(str(div.find('p', attrs={'class': 'overflow'}).text))
handle.close()
