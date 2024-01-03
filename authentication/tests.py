import json
from django.urls import reverse
from django.test import TestCase, Client

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Create your tests here.


client = Client()
User = get_user_model()


class UserRegistration(TestCase):
    def setUp(self):
        self.valid_payload = {"username": "johndoe5", "password": "johndoepass"}

    def test_status_code(self):
        response = client.post(
            reverse("authentication:register"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)


class UserLogin(TestCase):
    def setUp(self) -> None:
        user1 = User(username="johndoe2")
        user1.set_password("johndoepass")
        user1.save()

        self.token = Token.objects.create(user=user1)

        self.valid_payload = {"username": "johndoe2", "password": "johndoepass"}

    def test_token(self):
        response = client.post(
            reverse("authentication:login"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        resp_data = json.loads(response.content)
        self.assertEqual(resp_data.get("token"), self.token.key)
