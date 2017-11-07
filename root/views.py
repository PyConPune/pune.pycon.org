from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def homepage(request):
    return render(request, template_name='index.html', context={'page': 'home'})


def coc(request):
    return render(request, template_name='coc.html', context={'page': 'coc'})


def volunteer(request):
    # Dummy List of Volunteers, will be fetched from DB later
    list_of_volunteers = [
        {"name": "Volunteer 1", "description": "Enthusiastic Volunteer",
         "image": "img/anonymous.png", "github": "http://github.com",
         "twitter": "http://twitter.com"
        },
        {"name": "Volunteer 2", "description": "Enthusiastic Volunteer",
         "image": "img/anonymous.png", "github": "http://github.com",
         "twitter": "http://twitter.com"
        },
        {"name": "Volunteer 3", "description": "Enthusiastic Volunteer",
         "image": "img/anonymous.png", "github": "http://github.com",
         "twitter": "http://twitter.com"
        },
        {"name": "Volunteer 4", "description": "Enthusiastic Volunteer",
         "image": "img/anonymous.png", "github": "http://github.com",
         "twitter": "http://twitter.com"
        },
        {"name": "Volunteer 5", "description": "Enthusiastic Volunteer",
         "image": "img/anonymous.png", "github": "http://github.com",
         "twitter": "http://twitter.com"
        },
        {"name": "Volunteer 6", "description": "Enthusiastic Volunteer",
         "image": "img/anonymous.png", "github": "http://github.com",
         "twitter": "http://twitter.com"
        }
    ]

    return render(request, template_name='volunteer.html',
                context={'page': 'volunteer', 'volunteer_list': list_of_volunteers })

def be_volunteer(request):
    return render(request, template_name='be_volunteer.html', context={'page': 'be_volunteer'})

def about(request):
    return render(request, 'about.html', context={'page': 'about'})


def sponsors(request):
    return render(request, 'sponsors.html', context={'page': 'sponsors'})

def travelling(request):
    # Info taken from: https://www.mapsofindia.com/pune/travel-to-pune.html
    return render(request, 'travelling.html', context={'page': 'travelling'})
