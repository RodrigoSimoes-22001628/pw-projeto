from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('sobremim', views.sobremim_view, name='sobremim'),
    path('cadeira_nova',views.cadeira_nova_view, name='cadeira_nova'),
    path('cadeira_edita/<int:cadeira_id>', views.cadeira_edita_view, name='cadeira_edita'),
    path('cadeira_apaga/<int:cadeira_id>', views.cadeira_apaga_view, name='cadeira_apaga'),


    path('projetos', views.projetos_view, name='projetos'),
    path('projetos_nova',views.projetos_nova_view, name='projetos_nova'),
    path('projetos_edita/<int:projeto_id>', views.projetos_edita_view, name='projetos_edita'),
    path('projetos_apaga/<int:projeto_id>', views.projetos_apaga_view, name='projetos_apaga'),

    path('programacaoweb', views.programacaoweb_view, name='programacaoweb'),
    path('blog', views.blog_view, name='blog'),
    path('blog_nova',views.blog_nova_view, name='blog_nova'),
    path('blog_edita/<int:blog_id>', views.blog_edita_view, name='blog_edita'),
    path('blog_apaga/<int:blog_id>', views.blog_apaga_view, name='blog_apaga'),
    path('quizz', views.quizz, name='quizz'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('contacto', views.contacto_view, name='contacto'),
]