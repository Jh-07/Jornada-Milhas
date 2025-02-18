import os.path

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from apps.jornadaMilhas.serializers import DepoimentoSerializer
from django.urls import reverse
from rest_framework import status

from apps.jornadaMilhas.models import Depoimento
from rest_framework.test import APITestCase


#TODO Resolver criação de múltiplas imagens de teste

class DepoimentosTestCase(APITestCase):
    """
    Teste de API para o modelo de Depoimento
    """
    def setUp(self):

            self.usuario =  User.objects.create_superuser(username='admin',password='admin') #Cria um superusuario de teste com login e senha 'admin'
            self.url = reverse('Depoimentos-list') #Declara a Url que será usada apartir de sua basename em 'setup/urls.py'
            self.client.force_authenticate(user = self.usuario)


            #Depoimento de teste 1
            self.depoimento_1 = Depoimento.objects.create(
                nome = 'Teste um',
                depoimento = 'Depoimento teste',

                 foto = SimpleUploadedFile( #Como as fotos são ImageFields, é necessário usar essa classe para criar uma imagem de teste
                    name='foto_de_teste_1.jpg',
                    content=open('Foto depoimento/download.jpg','rb').read(),
                    content_type = 'image/jpg'
                )


            #Depoimento de teste 2
            )
            self.depoimento_2 = Depoimento.objects.create(
                nome ='Teste dois',
                depoimento='Depoimento teste 2',

                 foto = SimpleUploadedFile(
                    name='foto_de_teste_2.jpg',
                    content=open('Foto depoimento/download.jpg','rb').read(),
                    content_type = 'image/jpg'
                )



            )

    def test_requisicao_get_lista_depoimentos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_requisicao_get_depoimentos_por_id(self):
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        dados = Depoimento.objects.get(pk = 1) #ao usar 'objects.get()'se usa o argumento pk (primary key) e não Id
        dados_serializados = DepoimentoSerializer(instance=dados).data
        dados_serializados['foto'] = 'http://testserver' + dados_serializados['foto'] #A serialização retorna no campo 'foto' a url de hospedagem(absoluta) enquanto 'objects.get' retorna apenas o caminho relativo
        self.assertEqual(response.data,dados_serializados)


    def test_requisicao_delete_depoimentos(self):
        response = self.client.delete(self.url+'2/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_depoimentos(self):
        dados = {
            'nome': 'Testando denovo',
            'depoimento': 'Testando depoimento 2',
             'foto': SimpleUploadedFile(
                name='foto_de_teste_3.jpg',
                content=open('Foto depoimento/download.jpg','rb').read(),
                content_type = 'image/jpg'
            )

        }
        response = self.client.put(self.url+'1/', dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_requisicao_post_depoimentos(self):
        dados = {
            'nome': 'Testando',
            'depoimento': 'Testando depoimento',
             'foto' : SimpleUploadedFile(
                name='foto_de_teste_4.jpg',
                content=open('Foto depoimento/download.jpg','rb').read(),
                content_type = 'image/jpg'
            )
        }
        response = self.client.post(self.url,data = dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


