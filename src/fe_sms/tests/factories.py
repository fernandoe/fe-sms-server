import factory
from django.contrib.auth import get_user_model
from fe_core.factories import UserFactory, EntityFactory

from fe_sms.models import Telefone

User = get_user_model()


class TelefoneFactory(factory.django.DjangoModelFactory):
    usuario = factory.SubFactory(UserFactory)
    entidade = factory.SubFactory(EntityFactory)
    ddd = '51'
    numero = '992832466'

    class Meta:
        model = Telefone
