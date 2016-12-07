from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from ...accounts.tests.factory_models import UserFactory


class BaseApiTest(TestCase):
    def setUp(self):
        super().setUp()

        User = get_user_model()
        self.user = UserFactory.create(username='test')
        self.token = Token.objects.create(user=self.user)
        self.api_client = APIClient()
        self.api_client.credentials(
            HTTP_AUTHORIZATION='Token {0}'.format(self.token.key))
