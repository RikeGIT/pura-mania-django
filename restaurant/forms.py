from django import forms
from .models import Prato

class PratoForm(forms.ModelForm):
    class Meta:
        model = Prato
        fields = ['nome', 'descricao', 'preco', 'imagem', 'disponivel', 'complementos', 'tags']
        widgets = {
            'complementos': forms.CheckboxSelectMultiple,
            'tags': forms.CheckboxSelectMultiple,
        }
