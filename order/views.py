from rest_framework import views
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderView(views.APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)