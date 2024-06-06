from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import *

class MediaTestApi(APITestCase):
    def setUp(self):
        c = self.category = Category.objects.create(name='testname', slug='testname')
        self.media =  Media.objects.create(name='testname', year='Year 2020', discription='testdiscription' , direct_by='test_direct_by', country='kz', poster='test/poster.png', slug='testname', category=c)

    def test_list_view(self):
        url = reverse('home_page')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
    
    def test_media_view(self):
        res = self.client.get('http://127.0.0.1:8000/player/1-testname/1')
        self.assertEqual(res.status_code, 200)
