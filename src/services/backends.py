import os

import requests
from django.contrib.auth import get_user_model
from fe_core.models import Entity
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework_jwt.settings import api_settings

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
User = get_user_model()

host = os.environ.get('CONTA_SERVICE_HOST', 'conta')
port = os.environ.get('CONTA_SERVICE_PORT', '8000')


class FEMicroservicesBackend(BaseAuthentication):
    def authenticate(self, request, token=None):
        auth = get_authorization_header(request).split()
        if auth and auth[0].lower() == b'bearer':

            if len(auth) == 1:
                msg = 'Invalid token header. No credentials provided.'
                raise exceptions.AuthenticationFailed(msg)
            elif len(auth) > 2:
                msg = 'Invalid token header. Token string should not contain spaces.'
                raise exceptions.AuthenticationFailed(msg)

            try:
                token = auth[1].decode()

                url = 'http://{HOST}:{PORT}/verify/'.format(HOST=host, PORT=port)
                response = requests.post(url, data={
                    'token': token
                })

                if response.status_code == 400:
                    print(response.content)
                    raise exceptions.AuthenticationFailed('Invalid credentials')
                elif response.status_code == 404:
                    print(response.content)
                    raise exceptions.AuthenticationFailed('Conta service not found')

                info = jwt_decode_handler(token)
                try:
                    user = User.objects.get(pk=info['user_id'])
                except User.DoesNotExist:
                    entity = None
                    if 'entity' in info:
                        try:
                            entity = Entity.objects.get(pk=info['entity'])
                        except Entity.DoesNotExist:
                            entity = Entity.objects.create(
                                pk=info['entity']
                            )
                    user = User.objects.create(
                        pk=info['user_id'],
                        email=info['email'],
                        entity=entity
                    )
                return user, token
            except UnicodeError:
                msg = 'Invalid token header. Token string should not contain invalid characters.'
                raise exceptions.AuthenticationFailed(msg)
        else:
            return None


class FEMicroservicesBackendTesting(BaseAuthentication):
    def authenticate(self, request, token=None):
        auth = get_authorization_header(request).split()
        if auth and auth[0].lower() == b'bearer':

            if len(auth) == 1:
                msg = 'Invalid token header. No credentials provided.'
                raise exceptions.AuthenticationFailed(msg)
            elif len(auth) > 2:
                msg = 'Invalid token header. Token string should not contain spaces.'
                raise exceptions.AuthenticationFailed(msg)

            try:
                token = auth[1].decode()
                info = jwt_decode_handler(token)
                try:
                    user = User.objects.get(pk=info['user_id'])
                except User.DoesNotExist:
                    user = User.objects.create(
                        pk=info['user_id'],
                        email=info['email']
                    )
                return user, token
            except UnicodeError:
                msg = 'Invalid token header. Token string should not contain invalid characters.'
                raise exceptions.AuthenticationFailed(msg)
        else:
            return None
