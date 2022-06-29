from viewer.models import User
from viewer.models import Pictures
from viewer.models import AccountTiers
from rest_framework import serializers


class AccountTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTiers
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    acc_tier = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'acc_tier']


class PicturesSerializer(serializers.HyperlinkedModelSerializer):
    thumbnail_200 = serializers.ImageField(read_only=True)
    thumbnail_400 = serializers.ImageField(read_only=True)

    class Meta:
        model = Pictures
        fields = '__all__'
