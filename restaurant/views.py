from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from .models import Prato, Tag
from .forms import PratoForm


class PratoCreateView(LoginRequiredMixin, CreateView):
    model = Prato
    form_class = PratoForm
    template_name = 'restaurant/pages/pratosCrud.html'
    success_url = reverse_lazy('prato-crud')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pratos'] = Prato.objects.all()
        return context


class PratoUpdateView(LoginRequiredMixin, UpdateView):
    model = Prato
    form_class = PratoForm
    template_name = 'restaurant/pages/pratosCrud.html'
    success_url = reverse_lazy('prato-crud')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pratos'] = Prato.objects.all()
        context['editando'] = self.object.pk
        return context


class PratoDeleteView(LoginRequiredMixin, DeleteView):
    model = Prato
    template_name = 'restaurant/pages/pratosCrud.html'  # Usar o mesmo template para exibir confirmação, ou crie outro se quiser
    success_url = reverse_lazy('prato-crud')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pratos'] = Prato.objects.all()
        context['excluir'] = self.object.pk
        return context

    # Opcional: para redirecionar direto sem página de confirmação, sobrescreva o método post:
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.delete()
    #     return redirect(self.success_url)


class IndexView(ListView):
    model = Prato
    template_name = 'restaurant/pages/home.html'
    context_object_name = 'pratos'

    def get_queryset(self):
        queryset = super().get_queryset().filter(disponivel=True)
        tag_nome = self.request.GET.get('tag')
        if tag_nome:
            queryset = queryset.filter(tags__nome__iexact=tag_nome)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['tag_selecionada'] = self.request.GET.get('tag')
        return context


class CartaoPagina1View(TemplateView):
    template_name = 'restaurant/pages/cartaopagina1.html'


class CartaoPagina2View(TemplateView):
    template_name = 'restaurant/pages/cartaopagina2.html'


class CartaoPagina3View(TemplateView):
    template_name = 'restaurant/pages/cartaopagina3.html'
