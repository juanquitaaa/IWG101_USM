# Generated by Django 5.1.1 on 2024-11-27 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_UDI', '0002_mensaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aviso', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('ubicacion', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_UDI.usuario')),
            ],
        ),
    ]