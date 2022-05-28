from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('sobremim', views.sobremim_view, name='sobremim'),


    path('projetos', views.projetos_view, name='projetos'),

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