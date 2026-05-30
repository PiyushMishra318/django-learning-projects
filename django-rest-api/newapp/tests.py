from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from newapp.models import Snippet


class SnippetApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="demo",
            email="demo@example.com",
            password="demo-pass-123",
        )
        self.snippet_payload = {
            "title": "Hello",
            "code": "print('hello')",
            "linenos": False,
            "language": "python",
            "style": "friendly",
        }

    def test_list_snippets_is_public(self):
        response = self.client.get("/snippets/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_snippet_requires_authentication(self):
        response = self.client.post("/snippets/", self.snippet_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_snippet(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/snippets/", self.snippet_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Snippet.objects.count(), 1)
        self.assertEqual(Snippet.objects.get().owner, self.user)

    def test_highlight_action_returns_html(self):
        snippet = Snippet.objects.create(owner=self.user, **self.snippet_payload)
        response = self.client.get(f"/snippets/{snippet.pk}/highlight/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(b"highlight", response.content.lower())

    def test_jwt_token_endpoint(self):
        response = self.client.post(
            "/api/token/",
            {"username": "demo", "password": "demo-pass-123"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_feed_page_renders(self):
        response = self.client.get("/feed/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Snippet Feed")
