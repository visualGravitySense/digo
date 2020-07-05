import requests
from bs4 import BeautifulSoup as BS
import codecs
import time
import datetime
import random

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
"""
base_url = 'https://www.work.ua/ru/jobs-kyiv-python/'
domain = 'https://www.work.ua'
jobs = []
urls = []
urls.append(base_url)
req = session.get(base_url, headers=headers)
if req.status_code == 200:
    bsObj = BS(req.content, "html.parser")
    pagination = bsObj.find('ul', attrs={'class': 'pagination'})
    if pagination:
        pages = pagination.find_all('li', attrs={'class': False})
        for page in pages:
            urls.append(domain + page.a['href'])
for url in urls:
        time.sleep(2)
        if req.status_code == 200:
            bsObj = BS(req.content, "html.parser")
            div_list = bsObj.find_all('div', attrs={'class': 'job-link'})
            for div in div_list:
                title = div.find('h2')
                href = title.a['href']
                short = div.p.text
                company = "No name"
                logo = div.find('img')
                if logo:
                    company = logo['alt']
                jobs.append({'href': domain + href,
                             'title': title.text,
                             'descript': short,
                             'company': company})

#    print(div.find('h2').text)
#    print(title.text)
#    print('www.work.ua' + href)

"""
base_url = 'https://www.cv.ee/toopakkumised/harjumaa/infotehnoloogia/'
domain = 'https://www.cv.ee'
jobs = []
urls = []
urls.append(base_url)
req = session.get(base_url, headers=headers)
if req.status_code == 200:
    bsObj = BS(req.content, "html.parser")
    pagination = bsObj.find('div', attrs={'id': 'page-pagination'})
    if pagination:
        pages = pagination.find_all('li', attrs={'class': False})
        for page in pages:
            urls.append(domain + page.a['href'])

url = 'https://www.cv.ee/toopakkumised/harjumaa/infotehnoloogia/'
req = session.get(url, headers=headers)
domain = 'https://www.cv.ee'
jobs = []
for url in urls:
        time.sleep(2)
        if req.status_code == 200:
            bsObj = BS(req.content, "html.parser")
            div_list = bsObj.find_all('div', attrs={'class': 'offer_primary'})
            for div in div_list:
                title = div.find('h2')
                href = title.a['href']
                jobs.append({'href': domain + href,
                             'title': title.text})

template = '<!doctype html><html lang="en"><head><meta charset="utf-8"></head><body>'
end = '</body></html>'
content = '<h2>Cv.ee</h2>'
for job in jobs:
        content += '<a href="{href}" target_blank">{title}</a><br/><p>{href}</p><br/>'.format(**job)
        content += '<hr/><br/><br/>'
data = template + content + end

handle = codecs.open('cv3.html', "w", 'utf-8')
handle.write(str(data))
handle.close()


