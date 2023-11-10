from django.db import models
from django.contrib.auth.models import User

class Topico(models.Model):
    texto = models.CharField(max_length=100)
    data_edicao = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto
    

class Entrada(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    texto = models.TextField()
    data_edicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto[:50]+"..."