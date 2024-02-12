from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

from apps.models import Product


class IndexView(ListView):
    template_name = 'apps/base.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


class ProductCreateView(CreateView):
    template_name = 'apps/create_todo.html'
    model = Product
    fields = ['image', 'title', 'blocks']
    success_url = reverse_lazy('index')

class TodoUpdateView(UpdateView):
    model = Product
    fields = ['title', 'blocks']
    template_name = 'apps/update_product.html'
    success_url = reverse_lazy('index')