from rest_framework import serializers

from fe_sms.models import Telefone


class TelefoneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = ('pais', 'ddd', 'numero')
