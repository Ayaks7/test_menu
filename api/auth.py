from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions


class SingleTokenAuthentication(BaseAuthentication):
    """Аутентификация пользователя по токену."""
    def authenticate(self, request):
        user_token = request.META.get(
            'HTTP_AUTHORIZATION'
        )

        if user_token is not None and \
                user_token.replace('Token ', '') == settings.API_TOKEN:
            user, created = User.objects.get_or_create(
                username='add_test'
            )
            return (user, None)
        raise exceptions.AuthenticationFailed('Invalid Token')
