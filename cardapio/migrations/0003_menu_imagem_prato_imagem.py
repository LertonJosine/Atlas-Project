# Generated by Django 5.1.1 on 2024-09-18 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0002_rename_categoria_menu_rename_categoria_prato_menu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='menu/'),
        ),
        migrations.AddField(
            model_name='prato',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='pratos/'),
        ),
    ]
