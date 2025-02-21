from rest_framework import viewsets, generics, status
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
    queryset = Destino.objects.all().order_by('id')
    serializer_class = DestinoSerializer
    #filterset_fields = ['nome',] #Filtra usando o parametro 'nome' na URL, porém retorna apenas o nome EXATO, caso queira fazer uma filtragem melhor, criar uma classe de filtro ou usar o método abaixo

    #Filtra usando o parametro 'nome' na URL, usando operador ILIKE do SQL
    def list(self, request, *args, **kwargs):#Sobrepõe o método padrão de uma requisição GET [no DRF ao fazer uma requisição GET para uma view, o método list é chamado]
        '''
        Retorna uma resposta com a Lista de todos os Destinos , baseado num parâmetro passado na URL
        Parâmetro passado: ?nome=<nome do local>
        '''
        queryset = self.get_queryset()
        nome = self.request.query_params.get('nome')
        if nome :
            queryset = Destino.objects.all().filter(nome__icontains=nome)

            #Função no pacote generics que faz o mesmo que o get_object_or_404() do Django padrão, mas levantando exceção
            generics.get_object_or_404(queryset) #Faz a mesma coisa que o código abaixo, sem a flexibilidade de escolher a mensagem enviada

        # if not queryset.exists():
        #     return Response(
        #         data={
        #             "Mensagem": "Destino nãp encontrado."
        #         },
        #         status=status.HTTP_404_NOT_FOUND
        #     )
        serializer = self.get_serializer(queryset,many=True)
        return Response(data = serializer.data,status=status.HTTP_200_OK)