from botocore.stub import Stubber
from django.test import TestCase

from fe_sms.services.sms_service_aws import SMSService
from fe_sms.tests.factories import TelefoneFactory
from fe_sms.tests.responses import RESPONSE1, RESPONSE_INVALID

MESSAGE = 'Test message (Unit Test).'


class TestSMSService(TestCase):

    def test_send_message(self):
        telefone = TelefoneFactory()
        client = SMSService()
        stubber = Stubber(client.sns)
        stubber.add_response("publish", RESPONSE1)
        with stubber:
            response = client.send_message(telefone.get_telefone(), MESSAGE)

        assert "MessageId" in response
        assert "ResponseMetadata" in response
        assert "RequestId" in response["ResponseMetadata"]
        assert "HTTPStatusCode" in response["ResponseMetadata"]
        assert "RetryAttempts" in response["ResponseMetadata"]


    def test_send_message_with_invalid_number(self):
        telefone = TelefoneFactory(numero='999999')
        client = SMSService()
        stubber = Stubber(client.sns)
        stubber.add_response("publish", RESPONSE_INVALID)
        with stubber:
            response = client.send_message(telefone.get_telefone(), MESSAGE)

        assert "MessageId" in response
        assert "ResponseMetadata" in response
        assert "RequestId" in response["ResponseMetadata"]
        assert "HTTPStatusCode" in response["ResponseMetadata"]
        assert "RetryAttempts" in response["ResponseMetadata"]
