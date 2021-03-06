from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TelefoneModelSerializer, AWSMensagemSerializer


class EnviarMensagemAPIView(APIView):

    def post(self, request, format=None):
        usuario = request.user
        entidade = request.user.entity
        telefone_serializer = TelefoneModelSerializer(data=request.data)
        mensagem_serializer = AWSMensagemSerializer(data=request.data)
        if telefone_serializer.is_valid() and mensagem_serializer.is_valid():
            telefone = telefone_serializer.save(usuario=usuario, entidade=entidade)
            mensagem = mensagem_serializer.save(telefone=telefone, usuario=usuario, entidade=entidade)
            data = {'uuid': str(mensagem.uuid)}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            errors = dict(mensagem_serializer.errors, **mensagem_serializer.errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
