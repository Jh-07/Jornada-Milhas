from django.db import models

class Depoimento(models.Model):
    '''
    Classe de modelo de Depoimentos
    '''
    nome = models.CharField(max_length= 50, blank=False, null=False)
    depoimento = models.TextField(max_length=200, null = False)
    foto = models.ImageField(upload_to='fotos-depoimentos' , blank=True) #upload_to : Informa qual pasta as imagens serão encaminhadas

    def __str__(self):
        return self.nome
