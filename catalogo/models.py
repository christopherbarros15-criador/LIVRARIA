from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(blank=True, null=True)
    nacionalidade = models.CharField(max_length=100, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Editora(models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, related_name='livros')
    editora = models.ForeignKey(Editora, on_delete=models.SET_NULL, null=True, related_name='livros')
    ano_publicacao = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.titulo