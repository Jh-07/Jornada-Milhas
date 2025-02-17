from django.contrib import admin
from apps.jornadaMilhas.models import Depoimento


class Depoimentos(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')
    list_per_page = 10
    search_fields = ('nome',)

admin.site.register(Depoimento,Depoimentos)
