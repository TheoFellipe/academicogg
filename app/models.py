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