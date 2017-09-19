from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def homepage(request):
    return render(request, template_name='index.html', context={'page': 'home'})


def coc(request):
    return render(request, template_name='coc.html', context={'page': 'coc'})

def volunteer(request):
    return render(request, template_name='volunteer.html', context={'page': 'volunteer'})

def about(request):
    return render(request, 'about.html', context={'page': 'about'})
