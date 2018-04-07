from unittest import TestCase

from botocore.stub import Stubber

from fe_sms.services.sms_client_aws import SMSClient
from fe_sms.tests.responses import RESPONSE1


class TestSMSClient(TestCase):

    def test_send_message(self):
        client = SMSClient()
        stubber = Stubber(client.sns)
        stubber.add_response("publish", RESPONSE1)
        with stubber:
            response = client.send_message()

        assert "MessageId" in response
        assert "ResponseMetadata" in response
        assert "RequestId" in response["ResponseMetadata"]
        assert "HTTPStatusCode" in response["ResponseMetadata"]
        assert "RetryAttempts" in response["ResponseMetadata"]
