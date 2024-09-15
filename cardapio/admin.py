from django.contrib import admin
from .models import Menu, Prato, Igrediente


class PratoInline(admin.TabularInline):
    model = Prato
    

class MenuAdmin(admin.ModelAdmin):
    inlines = [PratoInline]
    list_display = [
        'nome',
    ]


class IgredienteInline(admin.TabularInline):
    model = Igrediente


class PratoAdmin(admin.ModelAdmin):
    inlines = [
        IgredienteInline,
    ]
    list_display = [
        'nome', 'menu'
    ]


# Register your models here.
admin.site.register(Menu, MenuAdmin)
admin.site.register(Prato, PratoAdmin)
