from django.test import TestCase

from fe_sms.serializers import AWSMensagemSerializer
from fe_sms.tests.factories import TelefoneFactory


class TestAWSMensagemSerializer(TestCase):

    def setUp(self):
        telefone = TelefoneFactory()
        self.DATA1 = {'telefone': str(telefone.uuid), 'mensagem': 'Mensagem de teste (unit-test).'}
        self.DATA_INVALID1 = {'telefone': str(telefone.uuid)}
        self.DATA_INVALID2 = {'mensagem': 'Mensagem de teste (unit-test).'}

    def test_is_valid(self):
        assert AWSMensagemSerializer(data=self.DATA1).is_valid()
        assert not AWSMensagemSerializer(data=self.DATA_INVALID1).is_valid()
        assert not AWSMensagemSerializer(data=self.DATA_INVALID2).is_valid()
