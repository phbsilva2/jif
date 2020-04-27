from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from django.shortcuts import HttpResponse
import io


def inscricao_pdf(unidade_organizacional, modalidade, incricoes):

    dados = []

    cabecalho = ['Nome do Atleta', 'Data Nasc.', 'RG', 'Matrícula']

    dados.append(cabecalho)

    for inscricao in incricoes:
        dados.append(inscricao)

    pdf_buffer = io.BytesIO()

    pdf = SimpleDocTemplate(pdf_buffer, pagesize=A4)

    table = Table(dados)

    # Adicionar estilo
    style = TableStyle([
        ('BACKGROUND', (0, 0), (3, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

        ('FONTNAME', (0, 0), (-1, 0), 'Courier'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),

        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),

        # ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])
    table.setStyle(style)

    # Alternar a cor do fundo
    rowNumb = len(dados)
    for i in range(1, rowNumb):
        if i % 2 == 0:
            bc = colors.white
        else:
            bc = colors.lightgrey

        ts = TableStyle(
            [('BACKGROUND', (0, i), (-1, i), bc)]
        )
        table.setStyle(ts)

    # Adicionar bordas
    ts = TableStyle(
        [
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('GRID', (0, 1), (-1, -1), 1, colors.black),
        ]
    )
    table.setStyle(ts)

    styles = getSampleStyleSheet()
    normal = styles['Normal']

    elems = []
    elems.append(Paragraph("<h1><b>IFB - Instituto Federal de Brasília</b></h1>", normal))
    elems.append(Spacer(1, 0.2 * inch))
    elems.append(Paragraph("<h2>Unidade Organizacional: <b>%s</b></h2>" % (unidade_organizacional), normal))
    elems.append(Paragraph("<h2>Modalidade: <b>%s</b></h2>" % (modalidade), normal))
    elems.append(Spacer(1, 0.2 * inch))
    elems.append(table)

    pdf.build(elems)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=pdfTable2.pdf'
    response.write(pdf_buffer.getvalue())
    pdf_buffer.close()

    return response
