from django.urls import path
from .views import SettingApiView

urlpatterns = [
    path('setting/', SettingApiView.as_view()),
]