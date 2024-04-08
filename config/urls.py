from django.contrib import admin
from django.urls import include, path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),

    path('ocupacao.html',OcupacoesView.as_view(), name='ocupacao'),
    path('avaliacao.html',AvaliacoesView.as_view(), name='avaliacao'),
    path('area.html', AreasdosaberView.as_view(), name='area'),
    path('periodo.html', PeriodosCursosView.as_view(), name='periodo'),
    path('turma.html', TurmasView.as_view(), name='turma'),
    path('cidade.html', CidadesView.as_view(), name='cidade'),
    path('tipos_avaliacao.html', AvaliacoesView.as_view(), name='tipos_avalicao'),
    path('pessoa.html', PessoasView.as_view(), name='pessoa'),
    path('instituicao.html', InstituicoesView.as_view(), name='instituicao'),
    path('curso.html', CursosView.as_view(), name='curso'),
    path('disciplina.html', DisciplinasView.as_view(), name='disciplinas'),
    path('matricula.html', MatriculasView.as_view(), name='matricula'),
    path('frequencia.html', FrequenciasView.as_view(), name='frequencia'),
    path('disciplinacurso.html', DisciplinasView.as_view(), name='disciplina_curso'),
]