from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView

from catalog.models import Product


class HomeView(TemplateView):
    """Класс для вывода главной страницы"""
    model = Product
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        return context_data

# def home(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list
#     }
#     return render(request, 'catalog/home.html', context)


class ContactsView(TemplateView):
    """Класс для вывода страницы с контактами"""
    template_name = 'catalog/contacts.html'

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Вы отправили новое сообщение от name(phone): message')
        return render(request, 'catalog/contact.html')

    def get(self, request):
        return render(request, 'catalog/contact.html')


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name}, ({phone}): {message}')
#     return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    """Класс для вывода страницы с деталями товара"""
    model = Product
    context_object_name = 'products'


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': product,
#     }
#     return render(request, 'catalog/product_detail.html', context)
