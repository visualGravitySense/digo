import requests
from bs4 import BeautifulSoup as BS
import codecs
import time

session = requests.Session()
headers = {'User-Agent': 'Safari/12.1.2 (MacOS Mojave 10.14.6) Gecko/20100101 Firefox/47.0',
            'Accept':'text/html,application/xhtml+xml,application/xhtml;q=0.9,*/*;q=0.8'
        }
base_url = 'https://djinni.co/jobs/?location=Киев&primary_keyword=Python'

domain = 'https://djinni.co'
jobs = []
urls = []
urls.append(base_url)
req = session.get(base_url, headers=headers)
#if req.status_code == 200:
#    bsObj = BS(req.content, "html.parser")
#    div = bsObj.find('div', attrs={'class': 'job-link'})
#    print(div.find('h2').text)




for url in urls:
    time.sleep(2)
    req = session.get(url, headers=headers)
    if req.status_code == 200:
        bsObj = BS(req.content, "html.parser")
        li_list = bsObj.find_all('li', attrs={'class': 'list-jobs__item'})
        for li in li_list:
            div = li.find('div', attrs={'class': 'list-jobs__title'})
            title = div.a.text
            href = div.a['href']
            short = 'No description'
            descr = li.find('div', attrs={'class': 'list-jobs__description'})
#            if descr:
#                short = descr.p.text
            jobs.append({'href': domain + href,
                        'title': title,
                        'descript': short,
                        'company': "No name"})

template = '<!doctype html><html lang="en"><head><meta charset="utf-8"><head><body>'
end = '</body></html>'
content = '<h2> Djinni.co</h2>'
for job in jobs:
    contnet += '<a href="{href}" target="_blank">{title}</a><br/><p>{descript}</p><p>{company}</p><br/>'.format(**job)
    content += '<hr/><br/><br/>'
data = template + content + end
handle = codecs.open('djinni.html', "w", "utf-8")
handle.write(str(data))
handle.close()
