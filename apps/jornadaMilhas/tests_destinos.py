from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from apps.jornadaMilhas.serializers import DestinoSerializer
from django.urls import reverse
from rest_framework import status

from apps.jornadaMilhas.models import Destino
from rest_framework.test import APITestCase


#TODO Resolver criação de múltiplas imagens de teste

class DestinosTestCase(APITestCase):
    """
    Teste de API para o modelo de Destino
    """
    def setUp(self):

            self.usuario =  User.objects.create_superuser(username='admin',password='admin') #Cria um superusuario de teste com login e senha 'admin'
            self.url = reverse('Destinos-list') #Declara a Url que será usada apartir de sua basename em 'setup/urls.py'
            self.client.force_authenticate(user = self.usuario)


            #Destino de teste 1
            self.Destino_1 = Destino.objects.create(
                nome = 'Teste um',
                preco = 1500.00,
                meta = 'Meta texto da imagem 1',
                texto_descritivo = 'Descrição da viagem destino 1',

                foto_1 = SimpleUploadedFile( #Como as fotos são ImageFields, é necessário usar essa classe para criar uma imagem de teste
                    name='foto_de_teste_destino_1_1.jpg',
                    content=open('Foto depoimento/paris.jpg','rb').read(),
                    content_type = 'image/jpg'
                ),
                foto_2 = SimpleUploadedFile( #Como as fotos são ImageFields, é necessário usar essa classe para criar uma imagem de teste
                    name='foto_de_teste_destino_1_2.jpg',
                    content=open('Foto depoimento/paris.jpg','rb').read(),
                    content_type = 'image/jpg'
                )


            #Destino de teste 2
            )
            self.Destino_2 = Destino.objects.create(
                nome ='Teste dois',
                preco= 2500.00,
                meta='Meta texto da imagem 2',
                texto_descritivo='Descrição da viagem destino 2', #substituir por api chatgpt

                 foto_1 = SimpleUploadedFile(
                    name='foto_de_teste_destino_2_1.jpg',
                    content=open('Foto depoimento/download.jpg','rb').read(),
                    content_type = 'image/jpg'
                ),
                foto_2 = SimpleUploadedFile(
                    # Como as fotos são ImageFields, é necessário usar essa classe para criar uma imagem de teste
                    name='foto_de_teste_destino_2_2.jpg',
                    content=open('Foto depoimento/paris.jpg', 'rb').read(),
                    content_type='image/jpg'
                )



            )

    def test_requisicao_get_lista_Destinos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_requisicao_get_Destinos_por_id(self):
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        dados = Destino.objects.get(pk = 1) #ao usar 'objects.get()'se usa o argumento pk (primary key) e não Id
        dados_serializados = DestinoSerializer(instance=dados).data
        dados_serializados['foto_1'] = 'http://testserver' + dados_serializados['foto_1'] #A serialização retorna no campo 'foto' a url de hospedagem(absoluta) enquanto 'objects.get' retorna apenas o caminho relativo
        dados_serializados['foto_2'] = 'http://testserver' + dados_serializados['foto_2'] #A serialização retorna no campo 'foto' a url de hospedagem(absoluta) enquanto 'objects.get' retorna apenas o caminho relativo
        self.assertEqual(response.data,dados_serializados)


    def test_requisicao_delete_Destinos(self):
        response = self.client.delete(self.url+'2/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_Destinos(self):
        dados = {
            'nome': 'Testando denovo',
            'preco': '1500.00',
            'meta' : 'Meta texto da imagem de teste',
            'texto_descritivo' : 'Descrição da viagem destino teste',
            'foto_1': SimpleUploadedFile(
                name='foto_de_teste_destino_3_1.jpg',
                content=open('Foto depoimento/paris.jpg','rb').read(),
                content_type = 'image/jpg'
            ),
            'foto_2': SimpleUploadedFile(
                name='foto_de_teste_destino_3_2.jpg',
                content=open('Foto depoimento/paris.jpg','rb').read(),
                content_type = 'image/jpg'
            )

        }
        response = self.client.put(self.url+'1/', dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_requisicao_post_Destinos(self):
        dados = {
            'nome': 'Testando',
            'preco': '2500.00',
            'meta': 'Meta texto da imagem de teste',
            'texto_descritivo': 'Descrição da viagem destino teste',
            'foto_1' : SimpleUploadedFile(
                name='foto_de_teste_destino_4_1.jpg',
                content=open('Foto depoimento/paris.jpg','rb').read(),
                content_type = 'image/jpg'
            ),
            'foto_2' : SimpleUploadedFile(
                name='foto_de_teste_destino_4_2.jpg',
                content=open('Foto depoimento/paris.jpg','rb').read(),
                content_type = 'image/jpg'
            )
        }
        response = self.client.post(self.url,data = dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)