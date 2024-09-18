from django.db import models
from django.urls import reverse
# Create your models here.


class Menu(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='menu/', blank=True)    
    def get_absolute_url(self):
        return reverse("landing")
    
    
    def __str__(self) -> str:
        return self.nome[:50]


class Prato(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    imagem = models.ImageField(upload_to='pratos/', blank=True)
    
    def get_absolute_url(self):
        return reverse("landing")
    
    def __str__(self) -> str:
        return self.nome[:50]
    
class Igrediente(models.Model):
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def get_absolute_url(self):
            return reverse("landing")

    def __str__(self) -> str:
        return self.nome[:50]
