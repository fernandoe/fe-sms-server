from rest_framework.response import Response
from rest_framework.views import APIView

from fe_sms.services.sms_service_aws import SMSService


class EnviarMensagemAPIView(APIView):

    def post(self, request, format=None):
        response = SMSService.create_message()
        return Response({'OK': 'OK'})
