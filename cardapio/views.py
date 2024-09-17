from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Menu, Prato
from .forms import MenuForm, PratoForm, prato_formset, igrediente_formset


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




class CreatePratoView(CreateView):
    model = Prato
    template_name = 'cardapio/criar_prato.html'
    form_class = PratoForm
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.request == 'POST':
            context['igrediente_formset'] = igrediente_formset(self.request.POST, instance=self.object)
        else:
            context['igrediente_formset'] = igrediente_formset(instance=self.object)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        igrediente_formset = context['igrediente_formset']

        if igrediente_formset.is_valid():
            self.object = form.save()
            igrediente_formset.save()
            
        return super().form_valid(form)

        
class ListarMenuView(ListView):
    model = Menu
    template_name = 'cardapio/listar_menu.html'
    context_object_name = 'menus'
    
    
class ListarPratosView(ListView):
    model = Prato
    template_name = 'cardapio/listar_pratos.html'
    context_object_name = 'pratos'
    

class UpdateMenuView(UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'cardapio/update_menu.html'
    
    
    def get_context_data(self, **kwargs: Any) :
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
    

class UpdatePratoView(UpdateView):
    model = Prato
    form_class = PratoForm
    template_name = 'cardapio/update_prato.html'
    
    
    def get_context_data(self, **kwargs: Any) :
        context = super().get_context_data(**kwargs)
        if self.request == 'POST':
            context['igrediente_formset'] = igrediente_formset(self.request.POST, instance=self.object)
        else:
            context['igrediente_formset'] = igrediente_formset(instance=self.object)
        
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        igrediente_formset = context['igrediente_formset']
        if igrediente_formset.is_valid():
            self.object = form.save()
            prato_formset.save()
        return super().form_valid(form)
    

