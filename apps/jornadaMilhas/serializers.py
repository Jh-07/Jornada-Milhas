from rest_framework import serializers

from apps.jornadaMilhas.models import Depoimento, Destino
from apps.jornadaMilhas.validators import *


class DepoimentoSerializer(serializers.ModelSerializer):
    '''
    Serializador da classe de depoimento
    '''
    class Meta:
        model = Depoimento
        fields = '__all__' #Todos os campos da classe serão serializados

class DestinoSerializer(serializers.ModelSerializer):
    '''
    Serializador da classe de destino
    '''
    class Meta:
        model = Destino
        fields = '__all__'

    #Verifica se o 'nome' é nulo, caso seja, completar com o texto do ChatGPT
    def validate(self, data):
        if not data['texto_descritivo']:
           data['texto_descritivo'] = get_texto_descritivo_chatGPT(data['nome'])
        print(data)
        return data