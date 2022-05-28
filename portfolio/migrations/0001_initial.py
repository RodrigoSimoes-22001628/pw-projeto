# Generated by Django 4.0.4 on 2022-05-12 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='')),
                ('autor', models.CharField(max_length=25)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=25)),
                ('descricao', models.CharField(max_length=2000)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
    ]
