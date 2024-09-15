from .models import Menu, Prato, Igrediente
from django.forms import ModelForm, inlineformset_factory



class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['nome']


prato_formset = inlineformset_factory(parent_model=Menu, model=Prato, fields=['nome', 'preco'], extra=1)
igrediente_formset = inlineformset_factory(parent_model=Prato, model=Igrediente, fields=['nome'], extra=1)
