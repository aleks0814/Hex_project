from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.core.validators import FileExtensionValidator
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail


class AccountTiers(models.Model):
    tiers = [
        ('BS', 'Basic'),
        ('PR', 'Premium'),
        ('EP', 'Enterprise')
    ]
    name = models.CharField(max_length=100, choices=tiers, default='BS', unique=True)

    def __str__(self):
        return f'{self.name}'


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.acc_tier = AccountTiers.name.default
        user.save()
        return user


class User(AbstractUser):
    objects = UserManager()
    acc_tier = models.ForeignKey(AccountTiers, on_delete=models.SET_NULL, null=True, default=1)


class Pictures(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True)
    picture = models.ImageField(default=False, upload_to='viewer/pictures',
                                validators=[FileExtensionValidator(allowed_extensions=['JPG', 'PNG'])])
    thumbnail_200 = ImageSpecField(source='picture', processors=[Thumbnail(height=200)])
    thumbnail_400 = ImageSpecField(source='picture', processors=[Thumbnail(height=400)])

    def __str__(self):
        return f'{self.picture}'