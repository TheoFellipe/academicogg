from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages         



class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass
class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})
class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        Instituicoes = Instituicao.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': Instituicao})
class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        Ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes':Ocupacao})
class AreasdosaberView(View):
    def get(self, request, *args, **kwargs):
        Areasdosaber = AreaSaber.objects.all()
        return render(request, 'areasaber.html', {'areasdosaber':AreaSaber})
class Pessoas(View):
    def get(self, request, *args, **kwargs):
        Pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': Pessoa})
    

