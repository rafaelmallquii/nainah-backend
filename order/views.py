from rest_framework import views
from rest_framework.response import Response
from order.models import Order
from order.serializers import OrderSerializer
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class OrderView(views.APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
def order_pdf(request, pk):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="order.pdf"'
    # response['Content-Disposition'] = 'attachment; filename="order.pdf"' # attachment for download

    # Create the PDF object, using the response object as its "file."
    p = SimpleDocTemplate(response, pagesize=letter)

    
    order = Order.objects.get(pk=pk)
    data = [
        ['Item', 'Quantity', 'Price', 'Total'],
    ]
    for i in order.orderitem_set.all():
        data.append([i.title, i.quantity, i.price, i.total_price])
    
    # Create the table style
    style = TableStyle([
        ('BACKGROUND', (0,0), (3,0), colors.pink),
        ('TEXTCOLOR', (0,0), (-1,0), colors.black),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 14),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.white),
    ])
    
    # Create the table object
    t = Table(data)

    # Add style to the table
    t.setStyle(style)

    # Add borders to the table
    ts = TableStyle(
        [
            ('BOX',(0,0),(-1,-1),2,colors.black),
            ('LINEBEFORE',(2,1),(2,-1),2,colors.pink),
            ('LINEABOVE',(0,2),(-1,2),2,colors.pink),
            ('GRID',(0,1),(-1,-1),2,colors.black),
        ]
    )
    t.setStyle(ts)

    # Send the data and build the file
    elements = []
    elements.append(t)
    p.build(elements)
    return response