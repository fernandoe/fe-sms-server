from django.contrib import admin

from fe_sms.models import Telefone, Mensagem, AWSMensagem


@admin.register(Telefone)
class TelefoneModelAdmin(admin.ModelAdmin):
    list_display = ('get_uuid', 'usuario', 'entidade', 'pais', 'ddd', 'numero')


@admin.register(Mensagem)
class MensagemModelAdmin(admin.ModelAdmin):
    list_display = ('get_uuid', 'usuario', 'telefone', 'mensagem', 'status')


@admin.register(AWSMensagem)
class AWSMensagemModelAdmin(admin.ModelAdmin):
    list_display = ('get_uuid', 'message_identifier', 'request_identifier', 'http_status_code', 'retry_attempts')
