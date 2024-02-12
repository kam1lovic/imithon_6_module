from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from apps.forms import CarbonadForm
from apps.models import Carbonad


class CarbonadListVeiw(ListView):
    template_name = 'index.html'
    queryset = Carbonad.objects.order_by('-id')
    context_object_name = 'carbonads'


class CarbonadUpdateView(UpdateView):
    template_name = 'update_product.html'
    form_class = CarbonadForm
    model = Carbonad
    success_url = reverse_lazy('carbonad_list')


class CarbonadDeleteView(DeleteView):
    template_name = 'delete_todo.html'
    model = Carbonad
    queryset = Carbonad.objects.all()
    success_url = reverse_lazy('carbonad_list')