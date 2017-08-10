from django.conf.urls import url

import payments.views

urlpatterns = [
    url(r"^webhook/$", payments.views.webhook,
        name="webhook"),
]
