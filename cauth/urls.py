from django.conf.urls import url
from django.contrib.auth import logout

import cauth.views

urlpatterns = [
    url(r"^account/signup/$", cauth.views.SignupView.as_view(),
        name="account_signup"),
    url(r"^account/login/$", cauth.views.LoginView.as_view(),
        name="account_loginview"),
    url(r"^account/logout/$", cauth.views.logout_view,
        name="account_loginout"),
]
