from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseBadRequest

import settings
import logging


# Create your views here.

def home(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def blog(request, key):
    logging.error(key)
    template = loader.get_template('blog.html')
    context = RequestContext(request, {'key': key})
    return HttpResponse(template.render(context))