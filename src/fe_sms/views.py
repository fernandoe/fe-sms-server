from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from fe_sms.serializers import TelefoneModelSerializer
from fe_sms.services.sms_service_aws import SMSService


class EnviarMensagemAPIView(APIView):

    def post(self, request, format=None):
        serializer = TelefoneModelSerializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user
            entity = user.entity
            telefone = serializer.save(usuario=user, entidade=entity)
            message = SMSService.create_message(user,  telefone)
            data = {
                'uuid': str(message.uuid)
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
