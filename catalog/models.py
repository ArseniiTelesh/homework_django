from django.db import models
from django.db.models import ForeignKey

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Категория")
    description = models.TextField(**NULLABLE, verbose_name="Описание категории")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Продукт (Вещь?)", help_text="Введите название..."
    )
    description = models.TextField(
        **NULLABLE, verbose_name="Описание", help_text="Введите описание..."
    )
    photo = models.ImageField(
        upload_to="Product_photo/", **NULLABLE, verbose_name="Фото"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Выберете категорию",
    )
    price = models.IntegerField(
        **NULLABLE, verbose_name="Цена", help_text="Укажите цену"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата последнего изменения"
    )
    owner = ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец', help_text="Создан пользователем",
                       **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт (Вешь?)"
        verbose_name_plural = "Продукты (Вещи?)"


class Version(models.Model):
    product = ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")

    version_number = models.PositiveIntegerField(
        verbose_name="Номер версии", help_text="Введите номер версии..."
    )
    version_name = models.CharField(
        max_length=300,
        verbose_name="Название версии",
        help_text="Введите название версии...",
    )
    current_version = models.BooleanField(verbose_name="Текущая версия")

    def __str__(self):
        return f"{self.version_number} - {self.version_name}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
