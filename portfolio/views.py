from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import matplotlib 
from matplotlib import pyplot as plt
from .models import *
from .forms import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view (request):
    if request.method == "Post":
        username = request.Post['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)

        if user is not None :
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio : home'))
        else :
            return render(request, 'portfolio/login.html', {
                'menssage': "Invalid credentials"
            })
    return render (request,'portfolio/login.html' )

def logout_view(request):
    logout(request)
    return render(request, 'portfolio/login.html',{'message': "Logged Out"})

def layout_view(request):
    return render(request, 'portfolio/layout.html')

def home_view(request):
    return render(request, 'portfolio/home.html')

def sobremim_view(request):
    context = {'educacaos': Educacao.objects.all(),
               'cadeiras': Cadeira.objects.all(),
               'competencias' : Competencia.objects.all(),
               'linguas' : Lingua.objects.all(),
               'interesses' : Interesse.objects.all(),
               }
    return render(request, 'portfolio/sobremim.html', context)

def cadeira_nova_view(request):
    form = CadeirasForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:sobremim'))

    context = {'form': form}
    return render(request, 'portfolio/cadeira_nova.html', context)

def cadeira_edita_view(request, cadeira_id):
    cadeira = Cadeira.objects.get(id=cadeira_id)
    form = CadeirasForm(request.POST or None, request.FILES, instance=cadeira)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:sobremim'))

    context = {'form': form, 
                'cadeira_id': cadeira_id,
              }
    return render(request, 'portfolio/cadeira_edita.html', context)

def cadeira_apaga_view(request, cadeira_id):
    Cadeira.objects.get(id=cadeira_id).delete()
    return HttpResponseRedirect(reverse('portfolio:sobremim'))



#----------------------------------------------------------



def projetos_view(request):
    context = {'projetos': Projeto.objects.all(),
                'tfcs': TFC.objects.all(),
                }
    return render(request, 'portfolio/projetos.html', context)

def projetos_nova_view(request):
    form = ProjetosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}
    return render(request, 'portfolio/projetos_nova.html', context)

def projetos_edita_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    form = ProjetosForm(request.POST or None, instance=projeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio: projetos'))

    context = {'form': form, 
                'projeto_id': projeto_id,
              }
    return render(request, 'portfolio/projetos_edita.html', context)

def projetos_apaga_view(request, projeto_id):
    Projeto.objects.get(id=projeto_id).delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))

#----------------------------------------------------------------------------------------

def programacaoweb_view(request):
    context = {
                'tecnologias': Tecnologia.objects.all(),
                'laboratorios' : Laboratorio.objects.all(),
                'noticias' : Noticia.objects.all(),
                'tecnologiawebsites': Tecnologiawebsite.objects.all(),}
    return render(request, 'portfolio/programacaoweb.html', context)


#----------------------------------------------------------------------------

def blog_view(request):
    context = {'publicacaos': Publicacao.objects.all()}
    return render(request, 'portfolio/blog.html', context)

def blog_nova_view(request):
    form = PublicacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}
    return render(request, 'portfolio/blog_nova.html', context)

def blog_edita_view(request, blog_id):
    blog = Publicacao.objects.get(id=blog_id)
    form = PublicacaoForm(request.POST or None, instance=blog)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 
                'blog_id': blog_id,
              }
    return render(request, 'portfolio/blog_edita.html', context)


def blog_apaga_view(request, blog_id):
    Publicacao.objects.get(id=blog_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))

#------------------------------------------------------------------------

def contacto_view(request):
    return render(request, 'portfolio/contacto.html')

#-------------------------------------------------------------------------
def resultados_quizz(request):
    pontos = 0
    nome = request.POST['nome']
    apelido = request.POST['apelido']
    html = request.POST['Html']
    css = request.POST['Css']
    estilos = request.POST['estilos']
    django = request.POST['Django']

    if html == "1991" :
        pontos += 25

    if css == "World Wide Web Consortium" or css == "W3C" :
        pontos += 25

    if estilos == "css" or estilos == "CSS" :
        pontos += 25 
    
    if django == "django" or  django == "Django" :
        pontos += 25

    return pontos

def desenha_grafico_resultados():
    participantes = sorted(PontuacaoQuizz.objects.all(), key=lambda t: t.pontuacao, reverse=True)     
    nomes = []     
    pontuacoes = []     
    for pt in participantes:         
        nomes.append(pt.nome +" "+pt.apelido)         
        pontuacoes.append(pt.pontuacao)     
        plt.barh(nomes, pontuacoes)     
        plt.savefig("portfolio/static/portfolio/images/grafico.png", bbox_inches='tight')

def quizz(request):
    if request.method == 'POST':
        n = request.POST['nome']
        a = request.POST['apelido']
        p = resultados_quizz(request)
        r = PontuacaoQuizz(nome=n, apelido=a, pontuacao=p)
        r.save()
    context = {
        'pontuacao': p
    }
    desenha_grafico_resultados()
    return render(request,'portfolio/programacaoweb.html',context)