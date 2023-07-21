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

from djoser.views import UserViewSet
from djoser import utils
from djoser.compat import get_user_email

class CustomUserViewSet(UserViewSet):
    def resend_activation(self, request):
        user = Customer.objects.filter(email=request.data.get('email')).first()

        if user:
            if user.is_active:
                return Response({"message": "This user is already active, please Login."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "No user found with this email."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().resend_activation(request)
