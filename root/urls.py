from django.conf.urls import url

from root.views import homepage

urlpatterns = [
    url(r'^$', homepage,
        name="homepage"),
]
