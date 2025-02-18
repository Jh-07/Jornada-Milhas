from django.contrib import admin
from apps.jornadaMilhas.models import Depoimento


class Depoimentos(admin.ModelAdmin):
    """
    Classe que disponibiliza o gerenciamento das instâncias de depoimento no admin Django
    """
    list_display = ('id','nome') # Campos serão exibidos na tela
    list_display_links = ('id','nome') # Quais campos são clicáveis para ir na tela de edição
    list_per_page = 10 # Número de objetos por página
    search_fields = ('nome',) # Qual campo será usado na barra de pesquisa do admin

admin.site.register(Depoimento,Depoimentos) #Faz com que o gerenciamento apareça na tela de admin
