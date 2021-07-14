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
        self.snack =Snack.objects.create(   name = 'goacamole',
                        purchaser = self.user,
                        description = 'awesome food'
                    )
        
    
    def test_status_codes(self):
        self.assertEqual(self.client.get(reverse('home')).status_code, 200)
        self.assertEqual(self.client.get(reverse('new')).status_code, 200)

    def test_create_view(self):
        responses = self.client.post(reverse('new'),{"name" : 'goacamole',"purchaser" : self.user,"description" : 'awesome food'})
        # responses = self.client.post(reverse('new'),self.snack)
        self.assertEqual(responses.status_code,200)
        self.assertContains(responses, 'goacamole')

    def test_new_object_creation(self):
        self.assertEqual(str(self.snack),'goacamole')

    def test_home_lists(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'goacamole')
    def test_details_view(self):
        response = self.client.get(reverse('details', args = '1'))
        self.assertContains(response,'awesome')
        self.assertTemplateUsed(response, 'details.html')
    def test_update_view(self):
        response = self.client.post(reverse('update',args='1'),{"name" : 'shawerma',"purchaser" : self.user,"description" : 'awesome food'})
        self.assertContains(response, 'shawerma')
        self.assertEqual(response.status_code,200)
    def test_delete_view(self):
        response = self.client.post(reverse('delete',args='1'))
        print(response.items)
        # check if it redirects properly
        self.assertEqual(response.status_code,302)