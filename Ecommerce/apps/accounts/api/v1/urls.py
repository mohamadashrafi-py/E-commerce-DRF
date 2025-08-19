from django.urls import path

from .views import (ProfileView, UserLoginView, UserLogoutView,
                    UserRegisterVerifyCodeView, UserRegisterView)

app_name = "accounts"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("verify/", UserRegisterVerifyCodeView.as_view(), name="verify"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
