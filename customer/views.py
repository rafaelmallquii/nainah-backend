from django.http import JsonResponse

from order.models import Order

def get_order_history(request, customer_id):
    orders = Order.objects.filter(customer_id=customer_id)
    
    data = []
    
    for order in orders:
        data.append({
            'id': order.id,
        })
        
    return JsonResponse(data, safe=False)