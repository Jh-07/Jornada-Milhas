from rest_framework import serializers

from apps.jornadaMilhas.models import Depoimento


class DepoimentoSerializer(serializers.ModelSerializer):
    '''
    Serializador da classe de depoimento
    '''
    class Meta:
        model = Depoimento
        fields = '__all__' #Todos os campos da classe serão serializados