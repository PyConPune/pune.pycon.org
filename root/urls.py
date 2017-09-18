from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

import root.views

urlpatterns = [
    url(settings.BASE_URL, include([
        url(r'^$', root.views.homepage,
            name="homepage"),
        url(r'^coc/$', root.views.coc,
            name="coc"),
        url(r'^about/$', root.views.about,
            name="about")
    ]))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
