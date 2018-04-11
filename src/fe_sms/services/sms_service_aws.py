import boto3

from fe_sms.models import AWSMensagem


class SMSService(object):
    def __init__(self):
        session = boto3.Session()
        self.sns = session.client('sns')

    @staticmethod
    def create_message(usuario, telefone):
        return AWSMensagem.objects.create(usuario=usuario, entidade=usuario.entity, telefone=telefone)

    def send_message(self, phone, message):
        response = self.sns.publish(PhoneNumber=phone, Message=message)
        return response
