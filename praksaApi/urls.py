from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

router = DefaultRouter()

router.register('devices', FCMDeviceAuthorizedViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('praksaApp.urls')),
]

