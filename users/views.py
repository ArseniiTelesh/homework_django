import secrets

from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, ResetPasswordForm, ProfileUpdateForm
from users.models import User


class UserRegisterView(CreateView):
    """
    Регистрация нового пользователя с подтверждением через email
    """

    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("users:verification_process")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token=token
        user.save()
        host = self.request.get_host()
        url = f'http//{host}/users/email-confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Доброго времени суток, перейдите по ссылке для подтверждения почты: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email, ],
        )
        return super().form_valid(form)


def verification_process(request):
    """
    Страница-заглушка для более четкого понимания действий пользователем
    """
    return render(request, 'users/verification_process.html')


def email_verification (request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:verification_success'))

def verification_success(request):
    """
    Страница-заглушка для более четкого понимания действий пользователем
    """
    return render(request, 'users/verification_success.html')


class UserResetPasswordView(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'users/reset_password.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            if user:
                password = User.objects.make_random_password(length=10)
                user.set_password(password)
                user.save()
                send_mail(
                    subject='Сброс пароля',
                    message=f' Ваш новый пароль {password}',
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[user.email]
                )
            return redirect(reverse('users:login'))
        except User.DoesNotExist:
            return HttpResponse('Пользователь с таким адресом электронной почты не найден.')

class ProfileDetailView(DetailView):
    """Класс для вывода профиля пользователя"""

    model = User

    def get_object(self, queryset=None):
        return self.request.user


class ProfileUpdateView(UpdateView):
    """Класс для вывода формы редактирования профиля пользователя"""

    model = User
    form_class = ProfileUpdateForm
    success_url = reverse_lazy("users:profile_detail")

    def get_object(self, queryset=None):
        return self.request.user
