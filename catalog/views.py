from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version
from catalog.services import get_categories_from_cache, get_products_from_cache


class ProductListView(ListView):
    """Класс для вывода главной страницы"""

    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data["object_list"]:
            active_version = Version.objects.filter(
                product=product, current_version=True
            ).first()
            product.active_version = active_version
        return context_data

    def get_queryset(self):
        return get_products_from_cache()


class ContactsView(TemplateView):
    """Класс для вывода страницы с контактами"""

    template_name = "catalog/contacts.html"

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} (почта {phone}) пишет: {message}")
        return render(request, "catalog/contacts.html")

    def get(self, request):
        return render(request, "catalog/contacts.html")


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Класс-контроллер для создания нового продукта"""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        """Метод для вывода формы версии при создании продукта"""

        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(self.request.POST)
        else:
            context_data["formset"] = VersionFormset()
        return context_data

    def form_valid(self, form):
        """Метод для сохранения формы при создании"""

        form.instance.owner = self.request.user  # Устанавливаем текущего пользователя как владельца продукта
        self.object = form.save()
        formset = self.get_context_data()["formset"]

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)

        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDetailView(DetailView):
    """Класс для вывода страницы с деталями товара"""

    model = Product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Класс-контроллер для редактирования продукта"""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        """Метод для вывода формы версии при редактировании продукта"""

        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        """Метод для сохранения формы при редактировании"""

        formset = self.get_context_data()["formset"]
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)

        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        """Метод для выбора формы исходя из прав доступа"""

        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if (
            user.has_perm("catalog.can_change_product_description")
            and user.has_perm("catalog.can_change_product_category")
            and user.has_perm("catalog.can_change_product_status")
        ):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    """Метод для удаления продукта"""

    model = Product
    success_url = reverse_lazy("catalog:home")
