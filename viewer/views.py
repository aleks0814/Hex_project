from django.shortcuts import render
from viewer.models import User
from viewer.models import Pictures
from viewer.models import AccountTiers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from viewer.serialazers import UserSerializer
from viewer.serialazers import PicturesSerializer
from viewer.serialazers import AccountTierSerializer
from rest_framework import generics


class AccTiersViewSet(viewsets.ModelViewSet):
    queryset = AccountTiers.objects.all()
    serializer_class = AccountTierSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class PictureViewSet(viewsets.ModelViewSet):
    serializer_class = PicturesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id
        if self.request.user.is_superuser:
            return Pictures.objects.all()
        pictures = Pictures.objects.filter(user=user)
        return pictures

