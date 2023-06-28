from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def generate_pdf(request):
    # Obtén los datos de la orden de tu base de datos o de donde los almacenes
    order_data = {
        'order_number': 'ORD123',
        'customer_name': 'John Doe',
        'items': [
            {'name': 'Camisa', 'price': 25},
            {'name': 'Pantalón', 'price': 40},
            {'name': 'Zapatos', 'price': 60},
        ],
        'total': 125,
    }

    # Crear el objeto PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="order.pdf"'

    # Definir el tamaño y margen del PDF
    pdf = SimpleDocTemplate(response, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)

    # Contenido del PDF
    elements = []

    # Encabezado del PDF
    header_text = "Nainah Collections - Order Details"
    elements.append(header_text)

    # Estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TEXTCOLOR', (-2, -1), (-1, -1), colors.red),
        ('FONTNAME', (-2, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (-2, -1), (-1, -1), 12),
        ('ALIGN', (-2, -1), (-1, -1), 'RIGHT'),
        ('BACKGROUND', (-2, -1), (-1, -1), colors.pink),
    ])

    # Datos de la tabla
    table_data = [
        ['Order Number', 'Customer', 'Item', 'Price'],
        [order_data['order_number'], order_data['customer_name'], '', '']
    ]

    # Llenar la tabla con los elementos de la orden
    for item in order_data['items']:
        table_data.append(['', '', item['name'], str(item['price'])])

    table_data.append(['', '', 'Total', str(order_data['total'])])

    # Crear la tabla y aplicar el estilo
    table = Table(table_data)
    table.setStyle(style)

    # Agregar la tabla al contenido del PDF
    elements.append(table)

    # Generar el PDF
    pdf.build(elements)

    return response
