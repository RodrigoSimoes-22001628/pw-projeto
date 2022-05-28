from django import forms
from django.forms import ModelForm
from .models import *


class PublicacaoForm(ModelForm):
    class Meta:
        model = Publicacao
        fields = '__all__'

    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor'}),
            'data': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Select a date','type': 'date'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'titulo'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'link'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descricao'}),
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'autor': 'Autor',
            'data': 'Data',
            'titulo': 'Título',
            'link': 'Link',
            'descricao': 'Descrição',
        }


class ProjetosForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control','placeholder': 'descricao'}),
            'anoRealizacao': forms.TextInput(attrs={'class': 'form-control','placeholder': 'anoRealizacao'} ),
            'participantes' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'participantes'} ),
            'linkGitHub': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'linkGitHub'}),
            'linkYt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'linkYt'}),
            'tecnologias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tecnologias'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'anoRealizacao': 'Ano Realização',
            'participantes': 'Participantes',
            'linkGitHub': 'Link GitHub',
            'linkYt': 'Link Youtube',
            'tecnologias': 'Tecnologias',
        }


class CadeirasForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nome'}),
            'ano': forms.TextInput(attrs={'class': 'form-control','placeholder': 'ano'}),
            'semestre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'semestre'} ),
            'ects' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'ects'} ),
            'ano_letivo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ano_letivo'}),
            'topicos_abordados': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'topicos_abordados'}),
            'ranking': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ranking'}),
            'docente_teorica': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'docente_teorica'}),
            'docente_praticas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'docente_praticas'}),
            'link_cadeira': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'link_cadeira'}),
            'linguagens' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'linguagens'}),
            'projetos' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'projetos'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome',
            'ano': 'Ano',
            'semestre': 'Semestre',
            'ects' : 'ECTS',
            'ano_letivo': 'Ano Letivo',
            'topicos_abordados': 'Tópicos Abordados',
            'ranking': 'Ranking',
            'docente_teorica':  'Docente Teórica',
            'docente_praticas':  'Docentes Práticas',
            'link_cadeira':  'Link Cadeira',
            'linguagens' : 'Linguagens',
            'projetos' :  'Projetos',
        }