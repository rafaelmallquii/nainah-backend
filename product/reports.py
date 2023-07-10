from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, Image
from io import BytesIO
from PIL import Image as PilImage
from .models import Product

def generate_product_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="product_report.pdf"'

    products = Product.objects.all()
    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()

    elements = []
    
    # Encabezado
    header = Paragraph("Nainah Collection - Product Inventory", styles['Heading1'])
    # background pink
    
    header.style.backColor = '#FFC0CB'
    
    elements.append(header)
    elements.append(Spacer(1, 12))

    for product in products:
        # Cargar y redimensionar la imagen del producto
        image_path = product.image.path
        pil_image = PilImage.open(image_path)
        max_width = 50
        max_height = 50
        pil_image.thumbnail((max_width, max_height), PilImage.ANTIALIAS)
        image_data = BytesIO()
        pil_image.save(image_data, format='PNG')

        img = Image(image_data)

        elements.append(Paragraph(f'ID: {product.product_id()} - {product.title}', styles['Heading3']))
        elements.append(img)
        elements.append(Spacer(1, 12))

        data = [['Variant', 'Color', 'Size', 'Stock', 'Price', 'Sale Price', 'Image']]  # Añade 'Image' a la lista

        for variant in product.variants():
            variant_data = [
                variant.title,
                variant.color,
                variant.size,
                variant.stock,
                variant.price,
                variant.sale_price,
                Image(variant.image.path, width=20, height=20)  # Agrega la imagen de la variante
            ]
            data.append(variant_data)

        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), styles['Heading4'].backColor),
            ('TEXTCOLOR', (0, 0), (-1, 0), styles['Heading4'].textColor),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), styles['Heading4'].fontName),
            ('FONTSIZE', (0, 0), (-1, 0), styles['Heading4'].fontSize),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), styles['Normal'].backColor),
            ('GRID', (0, 0), (-1, -1), 1, styles['Normal'].textColor),
        ]))

        elements.append(table)
        elements.append(Spacer(1, 12))

    doc.build(elements)

    return response
