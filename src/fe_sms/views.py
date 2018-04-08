# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class EnviarMensagemAPIView(APIView):

    def post(self, request, format=None):
        # usernames = [user.username for user in User.objects.all()]
        return Response({'OK': 'OK'})
