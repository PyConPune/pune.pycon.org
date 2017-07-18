from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, template_name='index.html', context={'page': 'home'})

def coc(request):
    return render(request, template_name='coc.html', context={'page': 'coc'})
