from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rental.models import Offer


class TestViews(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_offer_list(self):
        # Login
        self.client.login(username='testuser', password='password')
        url = reverse('offer-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_offer_details(self):
        # Login and create a sample offer
        self.client.login(username='testuser', password='password')
        offer = Offer.objects.create(text='Test Offer', author=self.user)
        url = reverse('offer-detail', args=[offer.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_detail(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)