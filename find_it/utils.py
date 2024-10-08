import requests
from bs4 import BeautifulSoup as BS
import codecs
import time
import datetime
import random

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

def djinni(base_url):
    session = requests.Session()
    domain = 'https://djinni.co'
    jobs = []
    urls = []
#    errors = []
    urls.append(base_url)
    urls.append(base_url+'&page=2')

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
                # company = "No name"
                descr = li.find('div', attrs={'class': 'list-jobs__description'})
                if descr:
                    short = descr.text
                jobs.append({'href': domain + href,
                            'title': title,
                            'descript': short,
                            'company': "No name"})

    return jobs

def rabota(base_url):
    session = requests.Session()
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

    for url in urls:
        time.sleep(2)
        req = session.get(url, headers=headers)
        if req.status_code == 200:
            bsObj = BS(req.content, "html.parser")
            div_list = bsObj.find_all('div', attrs={'class': 'offer_primary'})
            for div in div_list:
                title = div.find('h2')
                href = title.a['href']
                company = "No name"
                logo = div.find('li', {"class": "offer-company"})
                if logo:
                    company = logo('a')
                jobs.append({'href': domain + href,
                             'title': title.text,
                             'descript': "No name",
                             'company': company})

    return jobs