from django.test import TestCase
from django.urls import reverse 

class TestClientViews(TestCase):

    def test_home_view(self):
        """Test the response of the home view"""
        response = self.client.get(reverse('core:list_clients'))
        self.assertEqual(response.status_code, 200)

    def test_create_view(self):
        """Test the response of the client create view"""
        response = self.client.get(reverse('core:new_client'))
        self.assertEqual(response.status_code, 302)

    def test_update_view(self):
        """Test the response of the client update view"""
        response = self.client.get(reverse('core:update_client', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_delete_view(self):
        """Test the response of the client delete view"""
        response = self.client.get(reverse('core:delete_client', args=[1]))
        self.assertEqual(response.status_code, 302)

