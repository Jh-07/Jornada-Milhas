import random

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status, filters
from rest_framework.response import Response

from apps.jornadaMilhas.models import Depoimento, Destino
from apps.jornadaMilhas.serializers import DepoimentoSerializer, DestinoSerializer


class DepoimentoViewSet(viewsets.ModelViewSet):
    '''
    Habilita o CRUD do modelo Depoimento pelo django rest framework(DRF)
    '''
    queryset = Depoimento.objects.all().order_by('id')
    serializer_class = DepoimentoSerializer

class DepoimentoHomeViewSet(viewsets.ModelViewSet):
    '''
    Mostra 3 Depoimentos aleatórios
    '''
    queryset = Depoimento.objects.all().order_by('?')[:3] # order_by('?'): ordenação aleatória [:3]: Limita o número objetos de resposta a 3
    serializer_class = DepoimentoSerializer

class DestinoViewSet(viewsets.ModelViewSet):
    '''
    Habilita o CRUD do modelo Destino pelo django rest framework(DRF)
    '''

    serializer_class = DestinoSerializer

    def get_queryset(self): #Sobrepõe (Overrides) o método padrão de adquirir querysets
        queryset = Destino.objects.all().order_by('id')
        return queryset
    def list(self, request, *args, **kwargs): #Sobrepõe o método padrão de uma requisição GET [no DRF ao fazer uma requisição GET para uma view, o método list é chamado]
        '''
        Retorna uma resposta com a Lista de todos os Destinos , baseado num parâmetro passado na URL
        Parâmetro passado: ?nome=<nome do local>
        '''
        queryset = self.get_queryset()

        if 'nome' in request.query_params:
            nome = request.query_params['nome']
            queryset = Destino.objects.all().filter(nome__icontains = nome) #icontains procura de forma insensitiva(não importa letrs maiúsculas ou minúsculas) pelo 'nome' passado
            if not queryset.exists():
                return Response(
                    data={
                        'mensagem':'Destino não encontrado'
                    },
                    status = status.HTTP_404_NOT_FOUND
                )
        serializer = self.get_serializer(queryset,many=True)
        return Response(data = serializer.data,status=status.HTTP_200_OK)


