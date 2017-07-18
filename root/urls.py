from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


from root.views import homepage, coc

urlpatterns = [
    url(r'^$', homepage, name="homepage"),
    url(r'^coc/$', coc, name="coc")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
