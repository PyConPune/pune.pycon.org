"""pyconpune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import cauth.urls
import root.urls
import ticket.urls
import payments.urls
from django.conf import settings

urlpatterns = [
    url(settings.BASE_URL, include([
        url(r'^admin/', admin.site.urls),
        url(r'', include(root.urls)),
        url(r'', include(cauth.urls)),
        url(r'^jet/', include('jet.urls', 'jet')),
        url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
        url(r'^account/', include('account.urls')),
    ]))
]
