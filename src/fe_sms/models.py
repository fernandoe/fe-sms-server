from django.contrib.auth import get_user_model
from django.db import models
from fe_core.models import UUIDModel, Entity



User = get_user_model()


class Telefone(UUIDModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    entidade = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    pais = models.CharField(max_length=10, default="+55")
    ddd = models.SmallIntegerField()
    numero = models.CharField(max_length=10)

    def __str__(self):
        return "%s (%s) %s" % (self.pais, self.ddd, self.numero)


class Mensagem(UUIDModel):
    STATUS_CRIADO = "criado"
    STATUS_ENVIADO = "enviado"
    STATUS_CHOICES = (
        (STATUS_CRIADO, "Criado"),
        (STATUS_ENVIADO, "Enviado"),
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
    response = models.TextField(blank=True, null=True)

    def enviar_mensagem(self):
        from fe_sms.services.sms_service_aws import SMSService
        if self.status != self.STATUS_CRIADO:
            print(f'Mensagem não enviada devido ao seus status={self.status}')
        service = SMSService()
        response = service.send_message(self.telefone.__str__(), self.mensagem)
        self.response = response
        self.message_identifier = response["MessageId"]
        self.request_identifier = response["ResponseMetadata"]["RequestId"]
        self.http_status_code = response["ResponseMetadata"]["HTTPStatusCode"]
        self.retry_attempts = response["ResponseMetadata"]["RetryAttempts"]
        self.status = self.STATUS_ENVIADO
        self.save()
