from django.contrib.auth import get_user_model
from django.test import TestCase
from fe_core.factories import UserFactory

from fe_sms.models import Telefone
from fe_sms.tests.factories import TelefoneFactory

User = get_user_model()

DDD = '51'
NUMERO = '992832466'


class TestTelefone(TestCase):

    def test_entity(self):
        telefone = TelefoneFactory(ddd=DDD, numero=NUMERO)
        assert telefone.entidade

    def test_none_entity(self):
        telefone = TelefoneFactory(ddd=DDD, numero=NUMERO, entidade=None)
        assert telefone.entidade is None

    def test___str__(self):
        telefone = TelefoneFactory(ddd=DDD, numero=NUMERO)
        assert '+55 (51) 992832466' == str(telefone)

    def test_get_telefone(self):
        telefone = TelefoneFactory(ddd=DDD, numero=NUMERO)
        assert '+5551992832466' == telefone.get_telefone()

    def test_entidade_on_delete(self):
        usuario = UserFactory()
        telefone = TelefoneFactory(ddd=DDD, numero=NUMERO, usuario=usuario)
        assert 1 == Telefone.objects.filter(pk=telefone.uuid).count()
        User.objects.get(pk=usuario.pk).delete()
        assert 0 == Telefone.objects.filter(pk=telefone.uuid).count()
