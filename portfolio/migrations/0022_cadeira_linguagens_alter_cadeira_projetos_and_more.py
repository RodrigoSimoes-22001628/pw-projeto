# Generated by Django 4.0.4 on 2022-05-23 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_alter_professor_link_lusofona_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadeira',
            name='linguagens',
            field=models.ManyToManyField(blank=True, to='portfolio.tecnologia'),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='projetos',
            field=models.ManyToManyField(blank=True, to='portfolio.projeto'),
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='participantes',
        ),
        migrations.AddField(
            model_name='projeto',
            name='participantes',
            field=models.ManyToManyField(to='portfolio.pessoa'),
        ),
    ]
