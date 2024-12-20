# Generated by Django 5.0.3 on 2024-04-02 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="slug (читаемый URL)",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Заголовок")),
                ("body", models.TextField(verbose_name="Текст записи")),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="BlogPost_photo/",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        auto_now_add=True, null=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True, verbose_name="Признак публикации"
                    ),
                ),
                (
                    "view_count",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        null=True,
                        verbose_name="счетчик просмотров",
                    ),
                ),
            ],
            options={
                "verbose_name": "запись",
                "verbose_name_plural": "записи",
            },
        ),
    ]
