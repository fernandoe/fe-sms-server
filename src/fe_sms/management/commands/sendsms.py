from django.core.management.base import BaseCommand

from fe_sms.models import AWSMensagem


class Command(BaseCommand):

    def handle(self, *args, **options):
        mensagens = AWSMensagem.objects.filter(status=AWSMensagem.STATUS_CRIADO)

        if mensagens.count() == 0:
            self.stdout.write(self.style.SUCCESS('Não existem SMSs para serem enviadas nesse momento!'))

        for m in mensagens:
            m.enviar_mensagem()
            self.stdout.write(self.style.SUCCESS(f'Enviando SMS UUID={m.uuid}'))
