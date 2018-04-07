import boto3


class SMSClient(object):
    def __init__(self):
        pass

    def send_message(self):
        session = boto3.Session()
        sns = session.client('sns')
        response = sns.publish(PhoneNumber='+5551992832466', Message='Teste de mensagem')
        print(response)
