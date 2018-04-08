from django.urls import path

from .views import EnviarMensagemAPIView

urlpatterns = [
    path('enviar-mensagem', EnviarMensagemAPIView.as_view(), name='enviar-mensagem')
]
