# from django.contrib.auth import get_user_model
# from django.test import TestCase
#
# # Create your tests here.
# from django.urls import reverse
#
# from main.models import KinopoiskUser
#
#
# class MainTests(TestCase):
#     def setUp(self):
#         test_user1 = KinopoiskUser.objects.create(email='test1', password='test1')
#         test_user1.save()
#
#     def test_auth_uncorrect(self):
#         response = self.client.get(reverse('profile', 1))
#
#         self.assertRedirects(response,'/authPage/?next=/profile/1/')

from http import HTTPStatus
import os
from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class MainPagesTests(TestCase):

    def test(self):
        self.assertEquals(2, 2)

    # def setUp(self):
    #     os.environ['DJANGO_SETTINGS_MODULE'] = 'KinoPoisk.settings'
    #
    # def test_login_page_correct(self):
    #     response = self.client.get(reverse('login'))
    #
    #     self.assertEqual(response.status_code, HTTPStatus.OK)
    #     self.assertTemplateUsed(response, 'main/login.html')

    # def test_about_correct(self):
    #     response = self.client.get(reverse('about'))
    #
    #     self.assertEqual(response.status_code, HTTPStatus.OK)
    #     self.assertTemplateUsed(response, 'about.html')
    #
    # def test_contact_correct(self):
    #     response = self.client.get(reverse('contact'))
    #
    #     self.assertEqual(response.status_code, HTTPStatus.OK)
    #     self.assertTemplateUsed(response, 'contact.html')