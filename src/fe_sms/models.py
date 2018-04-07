from django.db import models
from fe_core.models import UUIDModel, Entity, User


class Telefone(UUIDModel):
    usuario = models.ForeignKey(User)
    entidade = models.ForeignKey(Entity, null=True, blank=True)
    pais = models.CharField(max_length=10, default="+55")
    codigo = models.SmallIntegerField()
    numero = models.CharField(max_length=10)


class Mensagem(UUIDModel):
    STATUS_CRIADO = "criado"
    STATUS_CHOICES = (
        (STATUS_CRIADO, "Criado"),
    )
    usuario = models.ForeignKey(User)
    entidade = models.ForeignKey(Entity, null=True, blank=True)
    telefone = models.ForeignKey(Telefone)
    mensagem = models.CharField(max_length=160)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_CRIADO)


class AWSMensagem(Mensagem):
    message_id = models.UUIDField(blank=False, null=False)
    request_id = models.UUIDField(blank=False, null=False)
    http_status_code = models.SmallIntegerField()
    retry_attempts = models.SmallIntegerField()
