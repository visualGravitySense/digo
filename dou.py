import requests
from bs4 import BeautifulSoup as BS
import codecs
import time
session = requests.Session()
headers = {'User-Agent': 'Safari/12.1.2 (MacOS Mojave 10.14.6) Gecko/20100101 Firefox/47.0',
            'Accept':'text/html,application/xhtml+xml,application/xhtml;q=0.9,*/*;q=0.8'
        }
base_url = 'https://jobs.dou.ua/vacancies/?category=Python'


jobs = []
urls = []
urls.append(base_url)

for url in urls:
    time.sleep(2)
    req = session.get(url, headers=headers)
    if req.status_code == 200:
        bsObj = BS(req.content, "html.parser")
        div = bsObj.find('div', attrs={'id': 'vacancyListId'})
        if div:
            li_list = bsObj.find_all('li', attrs={'class': 'l-vacancy'})
            for li in li_list:
                a = li.find('a', attrs={'class': 'vt'})
                title = a.text
                href = a['href']
                short = 'No description'
                company = "No name"
                a_company = li.find('a', attrs={'class': 'company'})
                if a_company:
                    company = a_company.text
                descr = li.find('div', attrs={'class': 'sh-info'})
                if descr:
                    short = descr.text
                    jobs.append({'href': href,
                            'title': title,
                            'descripti': short,
                            'company': company})



template = '<!doctype html><html lang="en"><head><meta charset="utf-8"><head><body>'
end = '</body></html>'
content = '<h2> Dou</h2>'
for job in jobs:
    contnet += '<a href="{href}" target="_blank">{title}</a><br/><p>{descript}</p><p>{company}</p><br/>'.format(**job)
    content += '<hr/><br/><br/>'
data = template + content + end
handle = codecs.open('jobs.html', "w", "utf-8")
handle.write(str(data))
handle.close()
