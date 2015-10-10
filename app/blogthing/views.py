from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseBadRequest


# Create your views here.

def blog(request, key):
    template = loader.get_template('blog.html', {"key": key})
    context = RequestContext(request)
    return HttpResponse(template.render(context))