from django.contrib.auth import get_user_model
from django.db import models
from fe_core.models import UUIDModel, Entity

User = get_user_model()


class Telefone(UUIDModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    entidade = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    pais = models.CharField(max_length=10, default="+55")
    codigo = models.SmallIntegerField()
    numero = models.CharField(max_length=10)


class Mensagem(UUIDModel):
    STATUS_CRIADO = "criado"
    STATUS_CHOICES = (
        (STATUS_CRIADO, "Criado"),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    entidade = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)
    mensagem = models.CharField(max_length=160)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_CRIADO)


class AWSMensagem(Mensagem):
    message_identifier = models.UUIDField(blank=True, null=True)
    request_identifier = models.UUIDField(blank=True, null=True)
    http_status_code = models.SmallIntegerField(blank=True, null=True)
    retry_attempts = models.SmallIntegerField(blank=True, null=True)
