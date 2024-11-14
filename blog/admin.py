from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Класс для регистрации продукта в административной панели."""

    list_display = ("title", "created_at", "view_count", "is_published", "slug")
    list_filter = ["created_at"]
    search_fields = ["title"]
