import requests
from bs4 import BeautifulSoup as BS
import codecs
import time
import datetime
session = requests.Session()
headers = {'User-Agent': 'Safari/12.1.2 (MacOS Mojave 10.14.6) Gecko/20100101 Firefox/47.0',
            'Accept':'text/html,application/xhtml+xml,application/xhtml;q=0.9,*/*;q=0.8'
        }
base_url = 'https://rabota.ua/jobsearch/vacancy_list?regionId=1&keyWords=Python'

domain = 'https://rabota.ua'
jobs = []
urls = []
urls.append(base_url)

for url in urls:
    time.sleep(2)
    req = session.get(url, headers=headers)
    if req.status_code == 200:
        bsObj = BS(req.content, "html.parser")
        table = bsObj.find('table', attrs={'id': 'ctl00_content_ctl00_gridList'})
        if table:
            tr_list = bsObj.find_all('tr', attrs={'id': True})
            for tr in tr_list:
                p = tr.find('p', attrs={'class': 'card-title'})
                title = p.a.text
                href = p.a['href']
                short = 'No description'
                company = "No name"
                logo = tr.find('p', attrs={'class': 'company-name'})
                if logo:
                    company = logo.a.text
                p = tr.find('div', attrs={'class': 'card-description'})
                if p:
                    short = p.text
                jobs.append({'href': domain + href,
                            'title': title,
                            'descript': short,
                            'company': company})

template = '<!doctype html><html lang="en"><head><meta charset="utf-8"><head><body>'
end = '</body></html>'
content = '<h2> Rabota</h2>'
for job in jobs:
    content += '<a href="{href}" target="_blank">{title}</a><br/><p>{descript}</p><p>{company}</p><br/>'.format(**job)
    content += '<hr/><br/><br/>'
data = template + content + end
handle = codecs.open('rabota.html', "w", "utf-8")
handle.write(str(data))
handle.close()
