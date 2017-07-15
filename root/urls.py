from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


from root.views import homepage

urlpatterns = [
    url(r'^$', homepage,
        name="homepage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
