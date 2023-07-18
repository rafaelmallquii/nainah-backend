from rest_framework import generics
from .models import Catalog
from .serializers import CatalogSerializer

class CatalogAll(generics.ListAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    