from django.conf.urls import url
from django.contrib.auth import logout

import cauth.views

urlpatterns = [
    url(r"^(?P<year>\d{4})/account/signup/$", cauth.views.SignupView.as_view(),
        name="account_signup"),
    url(r"^(?P<year>\d{4})/account/login/$", cauth.views.LoginView.as_view(),
        name="account_loginview"),
    url(r"^(?P<year>\d{4})/account/logout/$", cauth.views.logout_view,
        name="account_loginout"),
]
