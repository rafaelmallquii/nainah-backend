from django.urls import path, include
from rest_framework import routers
from .views import SettingViewSet

router = routers.DefaultRouter()

router.register(r'setting', SettingViewSet, basename='setting')

urlpatterns = [
    path('', include(router.urls), name='setting'),
]
