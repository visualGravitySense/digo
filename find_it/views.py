from django.shortcuts import render
from django.db import IntegrityError
from scraping.utils import *
from scraping.models import *
def home(request):
    city = City.objects.get(name='Lviv')
    speciality = Speciality.objects.get(name='Python')
    url_qs = Url.objects.filter(city=city, speciality=speciality)
    site = Site.objects.all()
    url_w = url_qs.get(site=site.get(name='Work.ua'))
    jobs = []
    jobs.extend(work(url_w.url_address))
    for job in jobs:
        vacancy = Vacancy(city=city, speciality=speciality, url=job['href'],
                                title=job['title'], description=job['descript'],
                                company=job['company'])
        try:
            vacancy.save()
        except IntegrityError:
            pass
    return render(request, 'base.html', {'jobs': jobs})
