"""upload_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from viewer.views import UserViewSet
from viewer.views import PictureViewSet
from viewer.views import AccTiersViewSet
from django.conf.urls.static import static
from django.conf import settings

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'tiers', AccTiersViewSet, basename='accounttiers')
router.register(r'users', UserViewSet, basename='user')
router.register(r'pictures', PictureViewSet, basename='pictures')
# router.register(r'sdsad', pictures_list, basename='pictures_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('pic', include(pictures_list)),
    path('', include(router.urls)),
    path('viewer-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)