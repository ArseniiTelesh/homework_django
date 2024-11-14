from django.db import models

NULLABLE = {"blank": True, "null": True}


class BlogPost(models.Model):
    slug = models.CharField(
        max_length=150, verbose_name="slug (читаемый URL)", **NULLABLE
    )
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Текст записи")
    preview = models.ImageField(
        upload_to="BlogPost_photo/", **NULLABLE, verbose_name="Фото"
    )
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Дата создания", **NULLABLE
    )
    is_published = models.BooleanField(default=True, verbose_name="Признак публикации")
    view_count = models.IntegerField(
        default=0, verbose_name="счетчик просмотров", **NULLABLE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"
