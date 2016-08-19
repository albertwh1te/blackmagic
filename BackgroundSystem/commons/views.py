from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext


def page_not_found(request):
    return render_to_response(template_name='commons/error/404.html')


def page_error(request):
    return render_to_response(template_name='commons/error/500.html')
