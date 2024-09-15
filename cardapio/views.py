from django.shortcuts import render
from django.views.generic import CreateView
from .models import Menu
from .forms import MenuForm, prato_formset, igrediente_formset


class CreateMenuView(CreateView):
    model = Menu
    template_name = "cardapio/criar_cardapio.html"
    form_class = MenuForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request == 'POST':
            context['prato_formset'] = prato_formset(self.request.POST, instance=self.object)
            
        else:
            context['prato_formset'] = prato_formset(instance=self.object)
            
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        prato_formset = context['prato_formset']
        if prato_formset.is_valid():
            self.object = form.save()
        prato_formset.save()
        return super().form_valid(form)
    

