"""ProjetoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import index, contatos_profs, cursos, adm, bancodedados, jogosdigitais, si, ti, noticias, formulario_matricula, aluno, professor, meusdadosaluno, notas, notasprof, meusdadosprof, contato
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index ),
    url(r'^contatoProf/',contatos_profs ),
    url(r'^cursos/',cursos),
    url(r'^cursoadministracao/',adm),
    url(r'^cursobancodedados/', bancodedados),
    url(r'^cursojogosdigitais/', jogosdigitais),
    url(r'^cursosi/', si),
    url(r'^cursoti/', ti),
    url(r'^noticias/', noticias),
    url(r'^matricula/', formulario_matricula),
    url(r'^areaAluno/', aluno),
    url(r'^areaProfessor/', professor),
    url(r'^dadosAlunos/', meusdadosaluno),
    url(r'^notasaluno/', notas),
    url(r'^notasprof/', notasprof),
    url(r'^dadosprof/', meusdadosprof),
    url(r'^contato/', contato),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
]

