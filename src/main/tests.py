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
