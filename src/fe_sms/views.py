from rest_framework.response import Response
from rest_framework.views import APIView

from fe_sms.services.sms_service_aws import SMSService


class EnviarMensagemAPIView(APIView):

    def post(self, request, format=None):
        sms_service = SMSService()

        usuario = request.user
        codigo = request.POST.get('codigo', '51')
        numero = request.POST.get('numero', '992832466')

        response = sms_service.create_message(usuario, codigo, numero)
        return Response({'OK': 'OK'})
