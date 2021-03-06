# Generated by Django 4.0.4 on 2022-05-16 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_delete_educacao_alter_publicacao_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formacao', models.CharField(max_length=40)),
                ('curso', models.CharField(max_length=40)),
                ('local', models.CharField(max_length=20)),
                ('periodo', models.CharField(max_length=30)),
                ('logotipo', models.ImageField(upload_to='static/portfolio/images')),
            ],
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='imagem',
            field=models.ImageField(upload_to='static/portfolio/images'),
        ),
    ]
