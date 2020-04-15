import requests
from bs4 import BeautifulSoup as BS
import codecs
import time

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
url = 'https://www.neti.ee/cgi-bin/teema/ARI/Too_ja_Personal/'
req = session.get(url, headers=headers)
if req.status_code == 200:
    bsObj = BS(req.content, "html.parser")
    div = bsObj.find('div', attrs={'class': 'result-item company fc-bi-ok'})
#    print(div.find('h2').text)
#data = bsObj.prettify()#.encode('utf8')

handle = codecs.open('neti.html', "w", 'utf-8')
handle.write(str(div.contents))
#handle.write(str(div.find('p', attrs={'class': 'overflow'}).text))
handle.close()
