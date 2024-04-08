from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome} {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Instituicao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituicao")
    site = models.CharField(max_length=100, verbose_name="Nome do Site")
    telefone = models.CharField(max_length=10, verbose_name="Numero de Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,verbose_name="Cidade da Instituicao")
    def __str__(self):
        return f"{self.nome}, {self.site}, {self.telefone}, {self.cidade}"
    class Meta:
        verbose_name = "Instituicao"
        verbose_name_plural = "Instituicoes"
        
class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Ocupacao")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacoes"

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Area do saber")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "AreaSaber"
        verbose_name_plural = "Areas do saber"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Pessoa")
    nome_do_pai = models.CharField(max_length=100, verbose_name="Nome do pai da Pessoa")
    nome_da_mae = models.CharField(max_length=100, verbose_name="Nome da mae da Pessoa")
    data_nasc = models.DateField(verbose_name="Data de nascimento da pessoa")
    email = models.CharField(max_length=100, verbose_name="Email da pessoa")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,verbose_name="Cidade da Pessoa")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE,verbose_name="Ocupacao da Pessoa")
    def __str__(self):
        return f"{self.nome} {self.nome_do_pai} {self.nome_da_mae} {self.data_nasc} {self.email} {self.cidade} {self.ocupacao}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
    carga_horaria_total = models.CharField(max_length=10, verbose_name="Carga horaria total")
    duracao_meses = models.CharField(max_length=10, verbose_name="Duração de meses")
    AreaSaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE,verbose_name="Area da Pessoa")
    Instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE,verbose_name="Instituição da Pessoa")
    def __str__(self):
        return f"{self.nome} {self.carga_horaria_total} {self.duracao_meses} {self.AreaSaber} {self.Instituicao} "
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class PeriodoCurso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Periodo do Curso")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Periodo Curso"
        verbose_name_plural = "Periodo Cursos"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    AreaSaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE,verbose_name="Area do saber da disciplina")
    def __str__(self):
        return f"{self.nome},{self.AreaSaber}"
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Matricula(models.Model):
    Instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE,verbose_name="Instituicao da Matricula")
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name="Curso da Matricula")
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,verbose_name="Pessoa que fez a matricula")
    data_inicio = models.DateField(verbose_name="Data de inicio")
    data_previsao_termino = models.DateField(verbose_name="Data de termino")
    
    
    def __str__(self):
        return f"{self.Instituicao} {self.Curso} {self.Pessoa} {self.data_inicio} {self.data_previsao_termino} "
    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descricao da avaliação")
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name="Avaliação do curso")
    Disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,verbose_name="Avaliação da disciplina")
    def __str__(self):
        return f"{self.descricao},{self.Curso},{self.Disciplina}"
    class Meta:
        verbose_name = "Avaliacao"
        verbose_name_plural = "Avaliacoes"

class Frequencia(models.Model):
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name="Frequencia do curso")
    Disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,verbose_name="Frequencia da disciplina")
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,verbose_name="Frequencia da pessoa")
    numero_falta = models.CharField(max_length=100,verbose_name="Numero de faltas")
    def __str__(self):
        return f"{self.Curso},{self.Disciplina},{self.Pessoa},{self.numero_falta}"
    class Meta:
        verbose_name = "Frequencia"
        verbose_name_plural = "Frequencias"

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da turma")
    turno = models.CharField(max_length=100, verbose_name="Turno")
    def __str__(self):
        return f"{self.nome} {self.turno}"
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        