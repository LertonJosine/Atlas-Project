# Generated by Django 5.1.1 on 2024-09-15 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Menu',
        ),
        migrations.RenameField(
            model_name='prato',
            old_name='categoria',
            new_name='menu',
        ),
        migrations.RemoveField(
            model_name='igrediente',
            name='prato',
        ),
        migrations.AddField(
            model_name='igrediente',
            name='prato',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cardapio.prato'),
            preserve_default=False,
        ),
    ]
