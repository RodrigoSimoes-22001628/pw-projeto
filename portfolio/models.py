from django.db import models

# Create your models here.
class Publicacao (models.Model):
   imagem = models.ImageField(upload_to= 'static/portfolio/images', blank=True)
   autor = models.CharField(max_length = 25)
   data = models.DateTimeField()
   titulo = models.CharField(max_length = 100)
   descricao = models.CharField(max_length = 2000)
   link = models.CharField(max_length = 1000 ,  null=True, blank=True)
   
   def __str__(self):
         return self.titulo[:50]
     
class Educacao (models.Model):
   formacao = models.CharField(max_length = 40)
   curso = models.CharField(max_length = 40)
   local = models.CharField(max_length = 20)
   periodo = models.CharField(max_length = 30)
   logotipo = models.ImageField(upload_to= 'static/portfolio/images')
   
   def __str__(self):
         return self.formacao[:50]

class Tecnologia (models.Model):
   nome = models.CharField(max_length = 80)
   acronimo = models.CharField (max_length = 10, blank=True)
   anoCriacao = models.IntegerField()
   criador = models.CharField(max_length = 80)
   logotipo = models.ImageField(upload_to= 'static/portfolio/images')
   link = models.CharField(max_length = 1000, null=True, blank=True) 
   descricao = models.TextField(max_length = 1000)

   def __str__(self):
      return self.nome[:50]

class Pessoa (models.Model):
   nome = models.CharField(max_length = 40)
   link_lusofona = models.CharField(max_length = 1000, null=True, blank=True)
   link_linkedin = models.CharField(max_length = 1000,  null=True, blank=True)
   
   def __str__(self):
     return self.nome[:50]

class Projeto (models.Model):
   titulo = models.CharField(max_length = 80)
   descricao = models.CharField(max_length = 500)
   imagem = models.ImageField(upload_to= 'static/portfolio/images', blank=True) 
   anoRealizacao = models.IntegerField()
   participantes = models.ManyToManyField(Pessoa, blank = True)
   linkGitHub = models.CharField(max_length = 1000, null=True, blank=True) 
   linkYt = models.CharField(max_length = 1000, null=True, blank=True) 
   tecnologias = models.ManyToManyField(Tecnologia, blank = True)

   def __str__(self):
     return self.titulo[:50] 

class TFC (models.Model):
    titulo = models.CharField(max_length = 80)
    autor = models.ManyToManyField(Pessoa ,  related_name= 'autor')
    orientador = models.ManyToManyField(Pessoa , related_name= 'orientador')
    imagem = models.ImageField(upload_to= 'static/portfolio/images', blank=True) 
    anoRealizacao = models.IntegerField()
    sumario = models.CharField(max_length = 500)
    link_relatorio = models.CharField(max_length = 1000)
    linkGitHub = models.CharField(max_length = 1000, null=True, blank=True)
    linkYt = models.CharField(max_length = 1000, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Cadeira(models.Model):
   nome = models.CharField(max_length = 40)
   ano = models.IntegerField()
   semestre = models.CharField(max_length = 2)
   ects = models.IntegerField()
   ano_letivo = models.CharField(max_length = 20)
   topicos_abordados = models.TextField()
   ranking = models.IntegerField()
   docente_teorica = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
   docentes_praticas = models.ManyToManyField(Pessoa, related_name= 'professor_pratica')
   link_cadeira = models.CharField(max_length = 1000)
   linguagens = models.ManyToManyField(Tecnologia,blank = True)
   projetos = models.ManyToManyField(Projeto, blank = True)
   
   def __str__(self):
      return self.nome[:50]

class Competencia (models.Model):
   titulo = models.CharField(max_length = 20)
   descricao = models.TextField(max_length = 1000)
   projetos = models.ManyToManyField(Projeto ,blank = True) 
   cadeira = models.ManyToManyField(Cadeira ,blank = True)    

   def __str__(self):
      return self.titulo[:50]

class Interesse (models.Model):
   titulo = models.CharField(max_length = 40)
   descricao = models.TextField(max_length = 1000)
   imagem = models.ImageField(upload_to= 'static/portfolio/images')
   link = models.CharField(max_length = 1000, null=True, blank=True)    

   def __str__(self):
      return self.titulo[:50]


# PROGRAMAÇÃO WEB
class Laboratorio (models.Model):
   titulo = models.CharField(max_length = 80)
   descricao = models.TextField(max_length = 1000)
   link = models.CharField(max_length = 1000, null=True, blank=True) 
   
   def __str__(self):
      return self.titulo[:50]

class Noticia (models.Model) :
   titulo = models.CharField(max_length = 80)
   descricao = models.TextField(max_length = 1000) 
   imagem = models.ImageField(upload_to= 'static/portfolio/images')
   link = models.CharField(max_length = 1000, null=True, blank=True) 

   def __str__(self):
      return self.titulo[:50]

# PROGRAMAÇÃO WEB

# SOBRE ESTE WEBSITE
class Tecnologiawebsite (models.Model):
   nome = models.CharField(max_length = 80)
   acronimo = models.CharField (max_length = 10, blank=True)
   anoCriacao = models.IntegerField()
   criador = models.CharField(max_length = 80)
   logotipo = models.ImageField(upload_to= 'static/portfolio/images')
   codigo = models.ImageField(upload_to= 'static/portfolio/images')
   link = models.CharField(max_length = 1000, null=True, blank=True) 
   descricao = models.TextField(max_length = 1000)

   def __str__(self):
      return self.nome[:50]

# SOBRE ESTE WEBSITE

class Lingua (models.Model) : 
   nome = models.CharField(max_length = 30)
   nivel = models.CharField(max_length = 30)

   def __str__(self):
      return self.nome[:50]

class PontuacaoQuizz(models.Model):     
   nome = models.CharField(max_length=30)    
   apelido = models.CharField(max_length=30)     
   pontuacao = models.IntegerField()

   def __str__(self):
      return self.nome[:50]