from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import (BlogPostCreateView, BlogPostDeleteView,
                        BlogPostDetailView, BlogPostListView,
                        BlogPostUpdateView)

app_name = BlogConfig.name

urlpatterns = [
    path("blog_create/", never_cache(BlogPostCreateView.as_view()), name="create"),
    path("blog_list/", BlogPostListView.as_view(), name="blog_list"),
    path("blog_detail/<int:pk>/", BlogPostDetailView.as_view(), name="blog_detail"),
    path("blog_update/<int:pk>/", BlogPostUpdateView.as_view(), name="update"),
    path("blog_delete/<int:pk>/", BlogPostDeleteView.as_view(), name="delete"),
]
