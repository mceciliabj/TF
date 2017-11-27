from django.shortcuts import render
from django.http import request
from django.views.decorators.csrf import ensure_csrf_cookie
from core.forms import ContatoForm

def index (requisito):
    return render(requisito,'index.html')
def contato(requisito):
    if requisito.POST:   
        form = ContatoForm(requisito.POST)
        if form.is_valid():
            form.envia_email()
    else:
        form = ContatoForm()
    texto ={
        "form":form
    }
    return render(requisito,'contato.html',texto)   
def cursos (requisito):
    return render(requisito,'cursos.html')
def contato(requisito):
    return render(requisito,'contato.html')
def contatos_profs (requisito):
    return render(requisito,'contatos_profs.html')
def adm (requisito):
    return render(requisito,'adm.html')
def bancodedados (requisito):
    return render(requisito,'bancodedados.html')
def jogosdigitais (requisito):
    return render (requisito,'jogosdigitais.html')
def si (requisito):
    return render(requisito,'si.html')
def ti (requisito):
    return render(requisito,'ti.html')
def noticias (requisito):
    return render(requisito,'noticias.html')
def formulario_matricula (requisito):
    return render(requisito,'formulario_matricula.html')
def aluno (requisito):
    return render(requisito,'aluno.html')
def professor (requisito):
    return render(requisito,'Professor.html')
def meusdadosaluno (requisito):
    return render (requisito,'meus_dados_aluno.html')
def notas (requisito):
    return render (requisito,'notas.html')
def notasprof (requisito):
    return render (requisito,'notas_prof.html')
def meusdadosprof (requisito):
    return render (requisito,'meus_dados_professor.html')

