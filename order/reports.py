import os
from django.conf import settings
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.platypus import Table
from django.conf import settings
from setting.models import Setting
from order.models import Order
from reportlab.lib.utils import ImageReader
from PIL import Image
from django.contrib.admin.views.decorators import staff_member_required

def draw_header(canvas, site_logo):
    png = Image.open(os.path.join(str(settings.BASE_DIR) + site_logo.url))
    png.load() # required for png.split()
    background = Image.new("RGB", png.size, (255, 255, 255))
    background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
    background.save('logo.jpg', 'JPEG', quality=80)
    
    canvas.setFillColorRGB(0.2, 0.2, 0.2)
    canvas.setFont('Helvetica', 16)
    canvas.drawString(18 * cm, -1 * cm, 'Invoice')
    canvas.drawInlineImage(background, 1 * cm, -1.1 * cm, 40, 25)
    canvas.setLineWidth(4)
    canvas.setStrokeColorRGB(1, 0.8, 0.8)
    canvas.line(0, -1.25 * cm, 21.7 * cm, -1.25 * cm)

def draw_address(canvas, business_details):
    """ Draws the business address """
    canvas.setFont('Helvetica', 9)
    textobject = canvas.beginText(13 * cm, -2.5 * cm)
    for line in business_details:
        textobject.textLine(line)
    canvas.drawText(textobject)

def draw_footer(canvas, note):
    """ Draws the invoice footer """
    textobject = canvas.beginText(1 * cm, -27 * cm)
    for line in note:
        textobject.textLine(line)
    textobject.textLine('Thank you for your business.')
    canvas.drawText(textobject)

@staff_member_required
def order_pdf(request, pk):
    """ Draws the invoice """
    order = Order.objects.get(pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
    # change title of html head 
    response['Content-Title'] = 'Invoice'

    s = Setting.objects.first()

    pdf_canvas = canvas.Canvas(response, pagesize=A4)
    pdf_canvas.translate(0, 29.7 * cm)
    pdf_canvas.setFont('Helvetica', 10)

    pdf_canvas.saveState()
    draw_header(pdf_canvas, s.site_logo)
    pdf_canvas.restoreState()

    pdf_canvas.saveState()
    draw_footer(pdf_canvas, [
        'Bank Details: Street address, Town, County, POSTCODE',
        'Sort Code: 00-00-00 Account No: 00000000 (Quote invoice number).',
        'Please pay via bank transfer or cheque. All payments should be made in CURRENCY.',
        'Make cheques payable to Company Name Ltd.',
    ])
    pdf_canvas.restoreState()

    pdf_canvas.saveState()
    address = s.site_address.split(', ')
    
    address = [_.upper() for _ in address]
    
    info =  [
        s.site_name.upper(),
        *address,
        f'Phone: {s.site_phone}',
        f'Email: {s.site_email}',
        f'Website: {s.site_website}',
        f'Reg No: {s.site_reg_no}'
    ]
    draw_address(pdf_canvas, info)
    pdf_canvas.restoreState()

    # Client address
    textobject = pdf_canvas.beginText(1.5 * cm, -2.5 * cm)
    textobject.textLine(f'{order.first_name} {order.last_name}')
    textobject.textLine(f'{order.email}')
    textobject.textLine(f'{order.address_line_1}')
    textobject.textLine(f'{order.address_line_2}')
    textobject.textLine(f'{order.city}')
    textobject.textLine(f'{order.state}')
    textobject.textLine(f'{order.postcode}')
    textobject.textLine(f'{order.country}')
    pdf_canvas.drawText(textobject)

    # Info
    textobject = pdf_canvas.beginText(1.5 * cm, -6.75 * cm)
    textobject.textLine(f'Invoice ID: {order.order_id()}')
    textobject.textLine(f'Invoice Date: {order.created.strftime("%d %b %Y %H:%M %p")}')
    try:
        textobject.textLine(f'Client: {order.customer.email}')
    except:
        pass
    pdf_canvas.drawText(textobject)

    # Items
    data = [['Quantity', 'Description', 'Unit Price', 'Amount']]

    for item in order.orderitem_set.all():
        data.append([item.quantity, f'{item.title}', item.price, item.total_price])

    data.append(['', '', 'Sub Total:', f'{order.sub_total}'])
    data.append(['', '', 'Shipping:', f'{order.shipping_charge}'])
    data.append(['', '', 'Tax:', "{:.2f}".format(order.tax)])
    data.append(['', '', 'Discount:', '0'])
    data.append(['', '', 'Total:', f'USD$ {order.total}'])
    
    table = Table(data, colWidths=[2 * cm, 11 * cm, 3 * cm, 3 * cm])
    table.setStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, -1), (0.2, 0.2, 0.2)),
        ('GRID', (0, 0), (-1, -6), 1, (0.7, 0.7, 0.7)),
        ('GRID', (-2, -1), (-1, -1), 1, (0.7, 0.7, 0.7)),
        ('ALIGN', (-2, 0), (-1, -1), 'RIGHT'),
        ('BACKGROUND', (0, 0), (-1, 0), (1, 0.8, 0.8)),
        ('FONT', (2, -5), (2, -4), 'Helvetica-Bold'),
        ('FONT', (2, -4), (2, -4), 'Helvetica-Bold'),
        ('FONT', (2, -3), (2, -3), 'Helvetica-Bold'), 
        ('FONT', (2, -2), (2, -2), 'Helvetica-Bold'),
        ('FONT', (2, -1), (2, -1), 'Helvetica-Bold'), 
        ('FONT', (3, -1), (3, -1), 'Helvetica-Bold'),
        ('BACKGROUND', (2, -1), (2, -1), (1, 0.8, 0.8)),
        ('BACKGROUND', (3, -1), (3, -1), (1, 0.8, 0.8)),
    ])
    tw, th = table.wrapOn(pdf_canvas, 15 * cm, 19 * cm)
    table.drawOn(pdf_canvas, 1 * cm, -8 * cm - th)

    pdf_canvas.showPage()
    pdf_canvas.save()

    return response
