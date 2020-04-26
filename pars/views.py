from django.shortcuts import render
from .utils import *
from .models import *
def home(request):
    jobs = djinni()
    city = City.objects.get(name='Lviv')

    return render(request, 'base.html')
