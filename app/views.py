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
        return render(request, 'instituicao.html', {'instituicoes': Instituicoes})
class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        Ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes':Ocupacoes})
class AreasdosaberView(View):
    def get(self, request, *args, **kwargs):
        Areasdosaber = AreaSaber.objects.all()
        return render(request, 'area.html', {'Areasdosaber': Areasdosaber})
class PessoasView(View):
    def get(self, request, *args, **kwargs):
        Pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': Pessoas})
class CursosView(View):
    def get(self, request, *args, **kwargs):
        Cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': Cursos})
class PeriodosCursosView(View):
    def get(self, request, *args, **kwargs):
        PeriodosCursos = PeriodoCurso.objects.all()
        return render(request, 'periodo.html', {'periodocursos': PeriodosCursos})
class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        Disciplinas = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplinas': Disciplinas})
class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        Matriculas = Matricula.objects.all()
        return render(request, 'matricula.html', {'matriculas': Matriculas})
class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        Avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacoes': Avaliacoes})
class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        Frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias': Frequencias})
class TurmasView(View):
    def get(self, request, *args, **kwargs):
        Turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': Turmas})
class TiavaliacoesView(View):
    def get(self, request, *args, **kwargs):
        Tiavaliacoes = Tiavaliacao.objects.all()
        return render(request, 'tiposavaliacao.html', {'tiavaliacoes': Tiavaliacoes})
class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        Ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencias.html', {'Ocorrencias': Ocorrencias})
