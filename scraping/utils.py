import requests
from bs4 import BeautifulSoup as BS
import codecs
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }

def djinni(base_url):
    session = requests.Session()
    domain = 'https://djinni.co/'
    jobs = []
    urls = []
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
                descr = li.find('div', attrs={'class': 'list-jobs__description'})
                if descr:
                    short = descr.text
                jobs.append({'href': domain + href,
                            'title': title,
                            'descript': short,
                            'company': "'No name'"})
    return jobs

def rabota(base_url):
    session = requests.Session()
    domain = 'https://rabota.ua'
    jobs = []
    urls = []
    #yesterday = datetime.date.today()-datetime.timedelta(1)
    #one_day_ago = yesterday.strftime('%d.%m.%Y')
    #base_url = base_url + one_day_ago
    urls.append(base_url)

    req = session.get(base_url, headers=headers)
    if req.status_code == 200:
        bsObj = BS(req.content, "html.parser")
        pagination = bsObj.find('dl', attrs={'id': 'ctl00_content_ctl00_gridList_ctl23_pagerInnerTable'})
        if pagination:
            pages = pagination.find_all('a', attrs={'class': 'f-always-blue'})
            for page in pages:
                urls.append(domain + page['href'])

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

    return jobs

def work(base_url):
    session = requests.Session()
    domain = 'https://www.work.ua'
    jobs = []
    urls = []
    urls.append(base_url)
    req = session.get(base_url, headers=headers)

    '''
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
        req = session.get(url, headers=headers)
        if req.status_code == 200:
            bsObj = BS(req.content, "html.parser")

    '''
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


    return jobs

def dou(base_url):
    session = requests.Session()
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
                                'descript': short,
                                'company': company})
    return jobs


'''
import requests
from bs4 import BeautifulSoup as BS
import codecs
import time
import datetime

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
def djinni():
    session = requests.Session()
    base_url = 'https://djinni.co/jobs/?primary_keyword=Python&location=Киев'

    domain = 'https://djinni.co/'
    jobs = []
    urls = []
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
                #company = "No name"
                descr = li.find('div', attrs={'class': 'list-jobs__description'})
    #            if descr:
    #                short = descr.p.text
                jobs.append({'href': domain + href,
                            'title': title,
                            'descript': short,
                            'company': "'No name'"})
                return jobs

def rabota():
    session = requests.Session()
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
                    logo = tr.find('div', attrs={'class': 'card-logo'})
                    if logo:
                        company = logo.a.text
                    div = tr.find('div', attrs={'class': 'card-description'})
                    if div:
                        short = p.text
                    jobs.append({'href': href,
                                'title': title,
                                'descript': short,
                                'company': company})
    return jobs

def work():
    session = requests.Session()
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
        req = session.get(url, headers=headers)
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
                    jobs.append({'href': href,
                                'title': title,
                                'descript': short,
                                'company': company})

    return jobs
'''
