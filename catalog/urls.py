from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductDetailView
app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('product_detail/<int:pk>', ProductDetailView.as_view())
]
