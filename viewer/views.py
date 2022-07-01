from rest_framework.generics import get_object_or_404
from viewer.models import User
from viewer.models import Pictures
from viewer.models import AccountTiers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from viewer.serialazers import UserSerializer
from viewer.serialazers import PicturesSerializer
from viewer.serialazers import AccountTierSerializer


class AccTiersViewSet(viewsets.ModelViewSet):
    '''View with every account tier'''
    queryset = AccountTiers.objects.all()
    serializer_class = AccountTierSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    '''View with every users for superusers'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class PictureViewSet(viewsets.ModelViewSet):
    """
    View with every picture
    For superuser it's showing every picture but other users only see their own pictures
    Shows fields with url depending on the built-in account tier
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PicturesSerializer
    queryset = Pictures.objects.all()

    def list(self, request, *args, **kwargs):
        """Shows fields with url depending on the built-in account tier or user satus"""
        user = self.request.user.id
        if self.request.user.is_superuser:
            pictures = Pictures.objects.all()
            serializer = PicturesSerializer(pictures, many=True, context={'request': request}).data
            return Response(serializer)
        else:
            pictures = Pictures.objects.filter(user=user)
        if self.request.user.acc_tier.name == 'BS':
            fields = ('url', 'id', 'user', 'thumbnail_200')
        elif self.request.user.acc_tier.name == 'PR':
            fields = ('url', 'id', 'user', 'thumbnail_200', 'thumbnail_400')
        elif self.request.user.acc_tier.name == 'EP':
            fields = ('url', 'id', 'user', 'thumbnail_200', 'thumbnail_400', 'picture')
        serializer = PicturesSerializer(pictures, many=True, fields=fields, context={'request': request}).data
        return Response(serializer)

    def get_object(self):
        """Cant figure it out how to restrict fields according to account tier"""
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
