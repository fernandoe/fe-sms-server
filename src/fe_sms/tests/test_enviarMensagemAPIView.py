from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings
from fe_core.factories import UserFactory, EntityFactory

from fe_sms.models import Telefone, Mensagem, AWSMensagem

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


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

    def test_response_200(self):
        response = self.client.post(reverse('enviar-mensagem'), {
            'codigo': '51',
            'numero': '992832466',
        })
        assert status.HTTP_200_OK == response.status_code
        # self.assertEqual(response.status_code, )
        # endereco = Endereco.objects.get(uuid=response.data['uuid'])
        # self.assertIsNone(endereco.entidade)
        # self.assertEqual(endereco.usuario, self.user)

    def test_create_model(self):
        assert 0 == Telefone.objects.all().count()
        assert 0 == Mensagem.objects.all().count()
        assert 0 == AWSMensagem.objects.all().count()
        self.client.post(reverse('enviar-mensagem'), {
            'codigo': '51',
            'numero': '992832466',
        })
        assert 1 == Telefone.objects.all().count()
        assert 1 == Mensagem.objects.all().count()
        assert 1 == AWSMensagem.objects.all().count()

