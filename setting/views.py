
from rest_framework import viewsets
from .models import Setting
from .serializers import SettingSerializer
from drf_spectacular.utils import extend_schema



class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    
    http_method_names = ['get',]
    
    @extend_schema(
        exclude=True,  # Ignore the 'GET /{id}'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)