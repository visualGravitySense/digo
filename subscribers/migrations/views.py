from django.shortcuts import render, redirect, get_object_or_404
from .forms import SubscriberModelForm
from django.views.generic.edit import FormView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.conf import settings
from .models import Subscriber

class SubscriberCreate(CreateView):
    model = Subscriber
    form_class = SubscriberModelForm
    template_name = 'subscribers/create.html'
    success_url = reverse_lazy('create')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            messages.success(request, 'Данные успешно сохранены.')
            return self.form_valid(form)
        else:
            messages.error(request, 'Проверьте правильность заполнения формы')
            return self.form_invalid(form)
