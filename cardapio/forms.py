from .models import Menu, Prato, Igrediente
from django.forms import ModelForm, inlineformset_factory, BaseInlineFormSet



class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['nome']


class PratoForm(ModelForm):
    class Meta:
        model = Prato
        fields = ['menu', 'nome', 'preco']




prato_formset = inlineformset_factory(parent_model=Menu, model=Prato, fields=['nome', 'preco'], extra=5)
igrediente_formset = inlineformset_factory(parent_model=Prato, model=Igrediente, fields=['nome'], extra=5)
