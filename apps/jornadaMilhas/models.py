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

class Destino(models.Model):
    '''
    Classe de modelo de destinos
    '''

    nome = models.CharField(max_length=50, blank=False,null=False)
    preco = models.DecimalField(max_digits=10,decimal_places=2,null=False)
    meta = models.TextField(max_length=160, blank=True,null=False)
    texto_descritivo = models.CharField(max_length=300, null=True)
    foto_1 = models.ImageField(upload_to='fotos-destinos-1',blank=True,null=True)
    foto_2 = models.ImageField(upload_to='fotos-destinos-2',blank=True, null=True)

    def __str__(self):
        return self.nome