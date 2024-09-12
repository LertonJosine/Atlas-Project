from django.contrib import admin
from .forms import CustomUserChageForm, CustomUserCreationForm
from .models import CustomUser
# Register your models here.


class CustomAdmin(admin.ModelAdmin):
    model = CustomUser
    form = CustomUserChageForm
    add_form = CustomUserCreationForm
    list_display = ('username', 'email')
    
admin.site.register(CustomUser, CustomAdmin)

