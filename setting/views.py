from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Setting, SiteMeta
from .serializers import SettingSerializer, SiteMetaSerializer

class SettingApiView(APIView):
    def get(self, request):
        setting = Setting.objects.all()
        serializer = SettingSerializer(setting, many=True)
        return Response(serializer.data)
    