from django.urls import path
from .views import PratoCreateView, PratoUpdateView, PratoDeleteView
from .views import IndexView, CartaoPagina1View, CartaoPagina2View, CartaoPagina3View
urlpatterns = [
    path('puramania/', IndexView.as_view(), name='home'),
    path('puramania/cartao1/', CartaoPagina1View.as_view(), name='cartaopagina1'),
    path('puramania/cartao1/cartao2/', CartaoPagina2View.as_view(), name='cartaopagina2'),
    path('puramania/cartao1/cartao2/cartao3/', CartaoPagina3View.as_view(), name='cartaopagina3'),
    # Crud
    path('pratos/', PratoCreateView.as_view(), name='prato-crud'),
    path('pratos/editar/<int:pk>/', PratoUpdateView.as_view(), name='prato-editar'),
    path('pratos/excluir/<int:pk>/', PratoDeleteView.as_view(), name='prato-excluir'),
]