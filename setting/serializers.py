from rest_framework import serializers
from .models import Setting, SiteMeta


class SiteMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteMeta
        fields = '__all__'

class SettingSerializer(serializers.ModelSerializer):
    sitemeta = SiteMetaSerializer()
    class Meta:
        model = Setting
        fields = '__all__'
        