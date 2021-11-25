from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Profile


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.user_obj = User.objects.create(username='testuser', password='Abc1234!')
        self.profile_obj = Profile.objects.create(user=self.user_obj, favorite_city='Paris')

        self.profiles_index_url = reverse('profiles_index')
        self.profile_url = reverse('profile', args=[self.user_obj.username])

    def test_index_GET(self):
        response = self.client.get(self.profiles_index_url)
        self.assertEquals(response.status_code, 200)

    def test_index_title(self):
        response = self.client.get(self.profiles_index_url)
        self.assertIn(b'Profiles', response.content)

    def test_index_template(self):
        response = self.client.get(self.profiles_index_url)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)

    def test_profile_title(self):
        response = self.client.get(self.profile_url)
        self.assertIn(b'testuser', response.content)

    def test_profile_template(self):
        response = self.client.get(self.profile_url)
        self.assertTemplateUsed(response, 'profiles/profile.html')
