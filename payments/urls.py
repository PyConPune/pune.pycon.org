from django.conf.urls import url

import payments.views

urlpatterns = [
    url(r"^webhook/$", payments.views.webhook,
        name="webhook"),
    url(r"^sync/$", payments.views.sync,
        name="sync"),
    url(r"^payment_dashboard/$", payments.views.payment_dashboard,
        name="payment_dashboard"),
]
