from django.contrib.auth import get_user_model
from django.test import TestCase

from fe_sms.models import Telefone


User = get_user_model()

class TestTelefone(TestCase):

    def test___str__(self):
        user = User.objects.create(email='fer.esp@gmail.com')
        telefone = Telefone.objects.create(usuario=user, ddd='51', numero='992832466')
        assert '+55 (51) 992832466' == str(telefone)
