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
domain = 'https://www.cv.ee'
jobs = []
if req.status_code == 200:
    bsObj = BS(req.content, "html.parser")
    div_list = bsObj.find_all('div', attrs={'class': 'cvo_module_offer_content'})
    for div in div_list:
        title = div.find('h2')
        href = title.a['href']
        #short = div.p.text
        company = "No name"
        logo = div.find('img')
        if logo:
            company = logo['alt']
    jobs.append({'href': domain + href,'title': title.text,'company': company})


handle = codecs.open('cv_.html', "w", 'utf-8')
handle.write(str(jobs))
handle.close()
