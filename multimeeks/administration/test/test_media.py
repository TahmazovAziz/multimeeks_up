from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from cinema.models import *

class MediaTest(TestCase):
    def setUp(self):
        self.c = self.category = Category.objects.create(name='testname', slug='testname')
        self.media =  Media.objects.create(name='testname', year='Year 2020', discription='testdiscription' , direct_by='test_direct_by', country='kz', poster='test/poster.png', slug='testname', category=self.c)

    def test_list_view(self):
        url = reverse('home_page')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
    
    def test_media_view(self):
        res = self.client.get('http://127.0.0.1:8000/player/1-testname/1')
        self.assertEqual(res.status_code, 200)

    def test_create_view(self):
        url = reverse('administration_create_media')
        media = Media(
            name='newname', 
            year='Year 2025', 
            discription='newdiscription', 
            direct_by='new_direct_by',
            country='kz', 
            poster='administration/test/poster.png', 
            slug='newname', 
            category=self.c
        )
        media.save()
        resp = self.client.post(url, data={
            'name': media.name,
            'year': media.year,
            'discription': media.discription,
            'direct_by': media.direct_by,
            'country': media.country,
            'poster': media.poster,
            'slug': media.slug,
            'category': media.category,
        })
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(media.name, "newname")
    
    def test_update_view(self):
        updated_media = Media(
            name='updatename', 
            year='Year 2025', 
            discription='updatediscription', 
            direct_by='update_direct_by',
            country='kz', 
            poster='administration/test/poster.png', 
            slug='update', 
            category=self.c
        )
        updated_media.save()
        self.assertEqual(updated_media.name,'updatename')
        self.media.refresh_from_db()
        self.assertEqual(updated_media.name,'updatename')
