from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField

NULLABLE = {"blank": True, "null": True}

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=40, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)

    token = CharField(max_length=100, verbose_name='Token', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

