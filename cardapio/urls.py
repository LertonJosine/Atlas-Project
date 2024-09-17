from django.urls import path
from .views import CreateMenuView, CreatePratoView, UpdateMenuView, UpdatePratoView, ListarMenuView, ListarPratosView

urlpatterns = [
    path('criarmenu/', CreateMenuView.as_view(), name='criar_menu'),
    path('criar_prato/', CreatePratoView.as_view(), name='criar_prato'),
    path('actualizar/menu/<int:pk>/', UpdateMenuView.as_view(), name='update_menu'),
    path('actualizar/prato/<int:pk>/', UpdatePratoView.as_view(), name='actualizar_prato'),
    path('actualizar/menu/', ListarMenuView.as_view(), name='listar_menu'),
    path('atualizar/prato/', ListarPratosView.as_view(), name='listar_pratos'),

]
