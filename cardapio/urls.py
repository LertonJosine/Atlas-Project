from django.urls import path
from .views import CreateMenuView

urlpatterns = [
    path('criarmenu/', CreateMenuView.as_view(), name='criar_menu'),
]
