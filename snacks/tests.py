from django.http import response
from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth import get_user_model
# Create your tests here.

class test_for_all(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "ahmad",
            email = 'ahmad@yahoo.com',
            password = 'AaAa123456'
        )
        self.snack = {  "name" : 'goacamole',
                        "purchaser" : self.user,
                        "description" : 'awesome food'
                    }
        
    
    def test_status_codes(self):
        self.assertEqual(self.client.get(reverse('home')).status_code, 200)
        self.assertEqual(self.client.get(reverse('new')).status_code, 200)

    def test_contains(self):
        # responses = self.client.post(reverse('new'),{"name" : 'goacamole',"purchaser" : self.user,"description" : 'awesome food'})
        responses = self.client.post(reverse('new'),self.snack)
        self.assertEqual(responses.status_code,200)
        self.assertContains(responses, 'goacamole')