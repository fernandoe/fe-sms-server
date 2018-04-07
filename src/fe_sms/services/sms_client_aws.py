import boto3


class SMSClient(object):
    def __init__(self):
        session = boto3.Session()
        self.sns = session.client('sns')

    def send_message(self):
        response = self.sns.publish(PhoneNumber='+5551992832466', Message='Teste de mensagem')
        return response
