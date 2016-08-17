from django.shortcuts import render
from .models import House
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'houses/home-rent.html'
