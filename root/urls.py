from django.conf.urls import url

from root.views import homepage

urlpatters = [
    url(r'^/$', homepage,
        name="homepage"),
]
