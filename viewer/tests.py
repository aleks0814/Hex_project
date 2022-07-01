from django.test import TestCase
from viewer.models import AccountTiers, User
from viewer.models import Pictures


class AccountTiersTests(TestCase):

    def test_acc_tier(self):
        acc_tier = AccountTiers.objects.create(name='PR')
        self.assertEqual(str(acc_tier), 'PR')


class PictureTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser = User.objects.create_user(username='testuser', password='1234')
        print(testuser.username)




    def test_pictures(self):
        pictures = Pictures.objects.create(picture='kiwi.jpg')
        self.assertEqual(str(pictures), 'kiwi.jpg')


class URLTests(TestCase):

    def test_testhomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
