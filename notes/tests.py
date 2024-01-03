import json

from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from notes.models import Note

client = Client()
User = get_user_model()


class NotesTest(TestCase):
    def setUp(self) -> None:
        self.user = User(username="johndoe")
        self.user.set_password("johndoepassword")
        self.user.save()

        self.token = Token.objects.create(user=self.user)

        self.note = Note.objects.create(user=self.user, text="lorem ipsum")

    def test_get_notes(self):
        """
        Get a list of notes.
        """
        url = reverse("notes:views")
        response = client.get(
            url,
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(200, response.status_code)

    def test_single_get_note(self):
        """
        Get a single note.
        """
        url = reverse("notes:detail-view", kwargs={"id": self.note.id})
        response = client.get(
            url,
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(200, response.status_code)

    def test_post_note(self):
        """
        Post a new note.
        """
        url = reverse("notes:views")
        response = client.post(
            url,
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
            data=json.dumps({"text": "lorem ipsum"}),
        )

        self.assertEqual(response.status_code, 201)

    def test_put_note(self):
        """
        Update an existing note.
        """
        url = reverse("notes:detail-view", kwargs={"id": self.note.id})

        response = client.put(
            url,
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
            data=json.dumps({"text": "lorem ipsum"}),
        )

        self.assertEqual(response.status_code, 201)

    def test_delete_note(self):
        """
        Delete an existing note.
        """
        url = reverse("notes:detail-view", kwargs={"id": self.note.id})

        response = client.delete(
            url,
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)

    def test_share_note(self):
        """
        Share a note.
        """
        url = reverse("notes:share", kwargs={"id": self.note.id})

        response = client.post(
            url,
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content).get("text"), self.note.text)

    def test_search_note(self):
        """
        Search a query in notes.
        """
        url = reverse("notes:search") + f"?q=ipsum"
        response = client.get(
            url,
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Token {self.token.key}",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)[0].get("text"), self.note.text)
