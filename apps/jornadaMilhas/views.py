from rest_framework import viewsets
from apps.jornadaMilhas.models import Depoimento
from apps.jornadaMilhas.serializers import DepoimentoSerializer

class DepoimentoViewSet(viewsets.ModelViewSet):
    queryset = Depoimento.objects.all().order_by('id')
    serializer_class = DepoimentoSerializer

