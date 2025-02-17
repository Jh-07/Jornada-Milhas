from django.db import models

class Depoimento(models.Model):
    nome = models.CharField(max_length= 50, blank=False, null=False)
    depoimento = models.TextField(max_length=200, null = False)
    foto = models.ImageField(upload_to='fotos-depoimentos', blank=True)

    def __str__(self):
        return self.nome
