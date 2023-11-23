from django.db import models

# Create your models here.

class Example(models.Model):
    ID = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=50)
    Idade = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")


    
    def __str__(self):
        return self.field1
    