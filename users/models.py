from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import EmailField

NULLABLE = {"blank": True, "null": True}

class User(AbstractUser):
    username = None
    email = EmailField(uniqe=True, verbose_name='почта')

    phone = models.CharField(max_length=40, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
