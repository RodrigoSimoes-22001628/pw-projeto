# Generated by Django 4.0.4 on 2022-05-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_educacao_alter_publicacao_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('link_linkedin', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cadeira',
        ),
        migrations.DeleteModel(
            name='Linguagem',
        ),
        migrations.AddField(
            model_name='professor',
            name='link_linkedin',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='link_lusofona',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='link',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
