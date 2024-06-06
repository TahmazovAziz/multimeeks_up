from django.test import TestCase
from users.models import *
from users.forms import *
from django.urls import reverse
from django.contrib.auth.validators import UnicodeUsernameValidator

class TestUsers(TestCase):

    def test_form_validity(self):
        form = UserCreationForm(data={'username': 'testuser',  'password1': 'testpassword', 'password2': 'testpassword'})
        self.assertTrue(form.is_valid())


    def test_invalid_form(self):
        form = UserCreationForm(data={'username': 'testusername', 'password1': '' , 'password2':''})
        self.assertFalse(form.is_valid())