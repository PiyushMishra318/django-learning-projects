from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import Post, UserProfile


class AccountsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="demo",
            email="demo@example.com",
            password="demo-pass-123",
        )
        self.profile = UserProfile.objects.get(user=self.user)

    def test_home_requires_login(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 302)

    def test_register_creates_user(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newbie",
                "first_name": "New",
                "last_name": "User",
                "email": "new@example.com",
                "password1": "ComplexPass123!",
                "password2": "ComplexPass123!",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newbie").exists())

    def test_authenticated_user_can_create_post(self):
        self.client.login(username="demo", password="demo-pass-123")
        response = self.client.post(reverse("update"), {"body": "Hello world"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 1)

    def test_profile_search_finds_user(self):
        self.client.login(username="demo", password="demo-pass-123")
        response = self.client.post(reverse("search_profile"), {"username": "demo"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "demo")
