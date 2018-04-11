from django.core.management.base import BaseCommand

from fe_sms.models import Mensagem


class Command(BaseCommand):

    def handle(self, *args, **options):
        mensagens = Mensagem.objects.filter(status=Mensagem.STATUS_CRIADO)
        if mensagens.count() == 0:
            self.stdout.write(self.style.SUCCESS('Não existem mensagens para serem enviadas.'))
        else:
            for m in mensagens:
                self.stdout.write(self.style.SUCCESS(f'Enviando SMS UUID={m.uuid}'))
