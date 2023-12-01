from django.db import models

# Create your models here.

class Escola(models.Model):
    idEscola = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Enredo(models.Model):
    idEnredo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    enredo = models.TextField()
    carnavalesco = models.TextField()

    def __str__(self):
        return self.titulo


class LivroAbreAlas(models.Model):
    idLivro = models.AutoField(primary_key=True)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField()
    enredo = models.ForeignKey(Enredo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.escola.nome} - {self.enredo.titulo}"


class Usuario(models.Model):
    idUsr = models.AutoField(primary_key=True)
    nomeUsr = models.CharField(max_length=255)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomeUsr
    