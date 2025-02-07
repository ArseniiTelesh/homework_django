from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import (ContactsView, ProductCreateView, ProductDeleteView,
                           ProductDetailView, ProductListView,
                           ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("", cache_page(60)(ProductListView.as_view()), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("create/", never_cache(ProductCreateView.as_view()), name="create_product"),
    path("product_detail/<int:pk>", ProductDetailView.as_view(), name="view_product"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="update_product"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="delete_product"),
]
