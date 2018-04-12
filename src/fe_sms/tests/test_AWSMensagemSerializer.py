from django.test import TestCase

from fe_sms.serializers import AWSMensagemSerializer


class TestAWSMensagemSerializer(TestCase):

    def setUp(self):
        self.DATA1 = {'mensagem': 'Mensagem de teste (unit-test).'}
        self.DATA_INVALID1 = {}
        self.DATA_INVALID2 = {'mensagem': 'Mensagem de teste (unit-test).'}

    def test_is_valid(self):
        assert AWSMensagemSerializer(data=self.DATA1).is_valid()
        assert not AWSMensagemSerializer(data=self.DATA_INVALID1).is_valid()

