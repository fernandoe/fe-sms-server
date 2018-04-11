import boto3


class SMSService(object):
    def __init__(self):
        session = boto3.Session()
        self.sns = session.client('sns')

    def send_message(self, phone, message):
        response = self.sns.publish(PhoneNumber=phone, Message=message)
        return response
