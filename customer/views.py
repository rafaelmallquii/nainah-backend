from rest_framework import generics, status
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Customer
from order.models import Order
from drf_spectacular.utils import extend_schema


def get_order_history(request, customer_id):
    orders = Order.objects.filter(customer_id=customer_id)
    
    data = []
    
    for order in orders:
        data.append({
            'id': order.id,
        })
        
    return JsonResponse(data, safe=False)


# check status active or not active customer

class CustomerActive(generics.ListAPIView):
    @extend_schema(
        description='Check status active or not active customer',
        responses={200: None}
    )
    def get(self, request, email):
        try:
            customer = Customer.objects.get(email=email)
            if customer.is_active:
                return Response({'email': customer.email, 'is_active': customer.is_active}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'No active'},status=status.HTTP_404_NOT_FOUND)
        except Customer.DoesNotExist:
            return Response({'message': 'Email not register'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)