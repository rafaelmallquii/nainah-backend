from rest_framework import generics
from .models import Subscriber
from .serializers import SubscriberSerializer
from drf_spectacular.utils import extend_schema

class SubscriberCreateAPIView(generics.CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = []
    authentication_classes = []
    
    @extend_schema(
        description='Create a new subscriber',
        responses={201: SubscriberSerializer}
    )
    def perform_create(self, serializer):
        serializer.save()