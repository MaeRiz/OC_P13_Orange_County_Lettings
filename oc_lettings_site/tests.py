from django.test import Client, TestCase
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')

    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)

    def test_index_title(self):
        response = self.client.get(self.index_url)
        self.assertIn(b'Holiday Homes', response.content)

    def test_index_template(self):
        response = self.client.get(self.index_url)
        self.assertTemplateUsed(response, 'index.html')
