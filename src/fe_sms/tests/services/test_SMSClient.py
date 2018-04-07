from unittest import TestCase

from fe_sms.services.sms_client_aws import SMSClient


class TestSMSClient(TestCase):
    def test___init__(self):
        self.fail()

    def test_send_message(self):
        client = SMSClient()
        client.send_message()
