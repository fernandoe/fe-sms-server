from django.test import TestCase
from fe_core.factories import UserFactory, EntityFactory

from fe_sms.serializers import TelefoneModelSerializer

DATA1 = {'pais': '+55', 'ddd': '51', 'numero': '992832466'}
DATA2 = {'ddd': '51', 'numero': '992832466'}
DATA_INVALID1 = {'ddd': '51'}
DATA_INVALID2 = {'numero': '992832466'}


class TestTelefoneModelSerializer(TestCase):

    def test_is_valid(self):
        assert TelefoneModelSerializer(data=DATA1).is_valid()
        assert TelefoneModelSerializer(data=DATA2).is_valid()
        assert not TelefoneModelSerializer(data=DATA_INVALID1).is_valid()
        assert not TelefoneModelSerializer(data=DATA_INVALID2).is_valid()

    def test_save_with_usuario_and_entidy(self):
        entidade = EntityFactory()
        usuario = UserFactory(entity=entidade)
        serializer = TelefoneModelSerializer(data=DATA1)
        serializer.is_valid()
        assert serializer.save(usuario=usuario, entidade=entidade)
