from rest_framework import serializers

from .models import Telefone, AWSMensagem


class TelefoneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = ('pais', 'ddd', 'numero')


class AWSMensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AWSMensagem
        fields = ('telefone', 'mensagem')
