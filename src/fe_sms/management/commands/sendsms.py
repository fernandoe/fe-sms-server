from django.core.management.base import BaseCommand

from fe_sms.models import Mensagem


class Command(BaseCommand):

    def handle(self, *args, **options):
        mensagens = Mensagem.objects.filter(status=Mensagem.STATUS_CRIADO)
        for m in mensagens:
            self.stdout.write(self.style.SUCCESS(f'Enviando SMS UUID={m.uuid}'))

