from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from fe_sms.models import AWSMensagem
from fe_sms.serializers import TelefoneModelSerializer


class EnviarMensagemAPIView(APIView):

    def post(self, request, format=None):
        usuario = request.user,
        entidade = request.user.entity,
        serializer = TelefoneModelSerializer(data=request.data)
        if serializer.is_valid():
            telefone = serializer.save(usuario=usuario, entidade=entidade)
            message = AWSMensagem.objects.create(
                usuario=request.user,
                entidade=request.user.entity,
                telefone=telefone
            )
            data = {'uuid': str(message.uuid)}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
