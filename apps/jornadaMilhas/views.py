import random

from rest_framework import viewsets
from apps.jornadaMilhas.models import Depoimento
from apps.jornadaMilhas.serializers import DepoimentoSerializer

class DepoimentoViewSet(viewsets.ModelViewSet):
    '''
    Habilita o CRUD do modelo Depoimento pelo django rest framework(DRF)
    '''
    queryset = Depoimento.objects.all().order_by('id')
    serializer_class = DepoimentoSerializer
    http_method_names = ['get','post','put','delete',]

class DepoimentoHomeViewSet(viewsets.ModelViewSet):
    '''
    Mostra 3 Depoimentos aleatórios
    '''
    queryset = Depoimento.objects.all().order_by('?')[:3] # order_by('?'): ordenação aleatória [:3]: Limita o número objetos de resposta a 3
    serializer_class = DepoimentoSerializer

