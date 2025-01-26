from django.contrib.auth.views import LoginView, LogoutView
from users.views import UserRegisterView, email_verification, verification_process, verification_success, \
    UserResetPasswordView

from django.urls import path

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("verification_process/", verification_process, name="verification_process"),
    path("email-confirm/<str:token>", email_verification, name='email_verification'),
    path("verification_success/", verification_success, name='verification_success'),
    path("login/", LoginView.as_view(template_name='users/login.html'), name="login"),
    path("reset_password/", UserResetPasswordView.as_view(template_name='users/reset_password.html'), name="reset_password"),
    path("logout/", LogoutView.as_view(), name="logout"),

]
