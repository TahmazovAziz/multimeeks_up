from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Users

class UsersApiTest(APITestCase):
    
    def setUp(self):
        self.user1 = Users.objects.create(username='username1')
        self.user2 = Users.objects.create(username='username2')
    
    def test_users_list(self):
        url = reverse('users-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 2)

    def test_retrieve_user(self):
        url = reverse('users-detail', kwargs={'pk':self.user1.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['username'], self.user1.username)

    def test_update_users(self):
        url = reverse('users-detail', kwargs={'pk':self.user1.pk})
        data = {'username': 'upusername' ,'password':'asdda'}
        resp = self.client.put(url, data, format='json')
        self.assertEqual(resp.status_code, 200)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.username, 'upusername')
    
    def test_create_user(self):
        url = reverse('users-list')
        data = {'username': 'newuser', 'password': 'aesfdfd'}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Users.objects.count(), 3)
        
    def test_delete_user(self):
        url = reverse('users-detail',kwargs={'pk':self.user1.pk})
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code,204)
        self.assertEqual(Users.objects.count(), 1)