from django.shortcuts import render
from django.db import IntegrityError
from scraping.utils import *
from scraping.models import *

def home(request):
    city = City.objects.get(name='Kyiv')
    speciality = Speciality.objects.get(name='Python')
    url_qs = Url.objects.filter(city=city, speciality=speciality)
    site = Site.objects.all()
    url_w = url_qs.get(site=site.get(name='Work.ua')).url_address
    url_dj = url_qs.get(site=site.get(name='Djinni.co')).url_address
    url_r = url_qs.get(site=site.get(name='Rabota.ua')).url_address
    url_dou = url_qs.get(site=site.get(name='Dou.ua')).url_address
    jobs = []
    jobs.extend(djinni(url_dj))
    jobs.extend(rabota(url_r))
    jobs.extend(work(url_w))
    jobs.extend(dou(url_dou))

    for job in jobs:
        vacancy = Vacancy(city=city, speciality=speciality, url=job['href'],
                                title=job['title'], description=job['descript'],
                                company=job['company'])
        try:
            vacancy.save()
        except IntegrityError:
            pass
    return render(request, 'base.html', {'jobs': jobs})
