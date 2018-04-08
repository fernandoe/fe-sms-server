import boto3

from fe_sms.models import AWSMensagem


class SMSService(object):
    def __init__(self):
        session = boto3.Session()
        self.sns = session.client('sns')

    def create_message(self):
        AWSMensagem.objects.create(

        )

    def send_message(self):
        response = self.sns.publish(PhoneNumber='+5551992832466', Message='Teste de mensagem')
        return response
