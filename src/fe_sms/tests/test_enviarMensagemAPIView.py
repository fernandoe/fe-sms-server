from django.urls import reverse
from fe_core.factories import UserFactory, EntityFactory
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from fe_sms.models import Telefone, Mensagem, AWSMensagem

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


example_data_1 = {
    'ddd': '51',
    'numero': '992832466',
}


class TestEnviarMensagemAPIView(APITestCase):

    def setUp(self):
        self.user = UserFactory(entity=None)
        payload = jwt_payload_handler(self.user)
        user_token = jwt_encode_handler(payload)

        self.entity = EntityFactory()
        self.user_with_entity = UserFactory(entity=self.entity)
        payload = jwt_payload_handler(self.user_with_entity)
        self.user_with_entity_token = jwt_encode_handler(payload)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token)

    def test_response_201(self):
        response = self.client.post(reverse('enviar-mensagem'), example_data_1)
        assert status.HTTP_201_CREATED == response.status_code

    def test_create_model(self):
        assert 0 == Telefone.objects.all().count()
        assert 0 == Mensagem.objects.all().count()
        assert 0 == AWSMensagem.objects.all().count()
        self.client.post(reverse('enviar-mensagem'), example_data_1)
        assert 1 == Telefone.objects.all().count()
        assert 1 == Mensagem.objects.all().count()
        assert 1 == AWSMensagem.objects.all().count()

    def test_response(self):
        response = self.client.post(reverse('enviar-mensagem'), example_data_1)
        m = Mensagem.objects.first()
        assert response.data['uuid'] == str(m.uuid)

    def test_create_message_and_awsmessage(self):
        response = self.client.post(reverse('enviar-mensagem'), example_data_1)
        uuid = response.data['uuid']
        assert Mensagem.objects.get(pk=uuid)
        assert AWSMensagem.objects.get(pk=uuid)

    def test_user_and_entity_into_objects(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user_with_entity_token)
        response = self.client.post(reverse('enviar-mensagem'), example_data_1)

        obj = Mensagem.objects.get(pk=response.data['uuid'])
        assert self.entity == obj.entidade
        assert self.user_with_entity == obj.usuario

        obj = AWSMensagem.objects.get(pk=response.data['uuid'])
        assert self.entity == obj.entidade
        assert self.user_with_entity == obj.usuario

        obj = Telefone.objects.first()
        assert self.entity == obj.entidade
        assert self.user_with_entity == obj.usuario

    def test_only_user_into_objects(self):
        response = self.client.post(reverse('enviar-mensagem'), example_data_1)

        obj = Mensagem.objects.get(pk=response.data['uuid'])
        assert not obj.entidade
        assert self.user == obj.usuario

        obj = AWSMensagem.objects.get(pk=response.data['uuid'])
        assert not obj.entidade
        assert self.user == obj.usuario

        obj = Telefone.objects.first()
        assert not obj.entidade
        assert self.user == obj.usuario
