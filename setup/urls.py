"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.jornadaMilhas.views import DepoimentoViewSet, DepoimentoHomeViewSet, DestinoViewSet

router = routers.DefaultRouter() #Criação de um router para melhorar a visibilidade do código

#Registrando rotas no router
router.register('depoimentos',DepoimentoViewSet, basename='Depoimentos')
router.register('depoimentos-home',DepoimentoHomeViewSet,basename='Depoimentos Home')
router.register('destinos', DestinoViewSet, basename='Destinos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), #Inclui as rotas do router
]
