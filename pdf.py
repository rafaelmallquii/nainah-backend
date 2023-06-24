from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

def generar_factura():
    # Crear un nuevo archivo PDF
    doc = SimpleDocTemplate("factura.pdf", pagesize=letter)
    elements = []

    # Configurar el estilo de la fuente
    styles = getSampleStyleSheet()
    header_style = styles["Heading1"]
    normal_style = styles["Normal"]

    # Dibujar el encabezado
    elements.append(Paragraph("Nainah Collection", header_style))
    elements.append(Paragraph("54 Allen St, Springfield, MA 01108 USA", normal_style))
    elements.append(Paragraph("+1 413-273- 9878", normal_style))
    elements.append(Paragraph("infonainah@nainahcollection.com", normal_style))
    elements.append(Spacer(1, 12))

    # Dibujar el número de factura
    elements.append(Paragraph("Factura #001", header_style))
    elements.append(Spacer(1, 12))

    # Dibujar la tabla de productos
    data = [['Producto', 'Cantidad', 'Precio unitario', 'Total'],
            ['Producto 1', '2', '$10', '$20'],
            ['Producto 2', '1', '$15', '$15'],
            ['Producto 3', '3', '$5', '$15'],
            ['Total', '', '', '$50']]
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e83e8c')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#e83e8c')),
        ('TEXTCOLOR', (0, -1), (-1, -1), colors.whitesmoke),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, -1), (-1, -1), 14),
        ('TOPPADDING', (0, -1), (-1, -1), 12)
    ])
    table = Table(data, colWidths=[120, 60, 80, 80])

    table.setStyle(table_style)
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Dibujar el pie de página
    elements.append(Paragraph("Gracias por su compra", normal_style))

    # Guardar el archivo PDF generado
    doc.build(elements)

generar_factura()
