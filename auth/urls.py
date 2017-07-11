from django.conf.urls import url

import auth.views

urlpatterns = [
    url(r"^account/signup/$", auth.views.SignupView.as_view(),
        name="account_signup"),
    url(r"^account/login/$", auth.views.LoginView.as_view(),
        name="account_loginview"),
]
