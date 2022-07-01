from viewer.models import User
from viewer.models import Pictures
from viewer.models import AccountTiers
from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        """

        :rtype: object
        """
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class AccountTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTiers
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    acc_tier = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'acc_tier']


class PicturesSerializer(DynamicFieldsModelSerializer):
    thumbnail_200 = serializers.ImageField(read_only=True)
    thumbnail_400 = serializers.ImageField(read_only=True)

    class Meta:
        model = Pictures
        fields = ['url', 'id', 'user', 'thumbnail_200', 'thumbnail_400', 'picture']



