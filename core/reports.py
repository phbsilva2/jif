from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from django.shortcuts import HttpResponse
from django.conf import settings
import io


def inscricao_pdf(unidade_organizacional_nome, modalidade_nome, inscricoes=[]):

    cabecalho = ['Nome do Atleta', 'Data Nasc.', 'RG', 'Matrícula']

    qtd_atletas = len(inscricoes)
    inscricoes.sort()

    inscricoes.insert(0, cabecalho)

    pdf_buffer = io.BytesIO()

    pdf = SimpleDocTemplate(pdf_buffer, pagesize=A4)

    table = Table(inscricoes)

    # Adicionar estilo
    style = TableStyle([
        ('BACKGROUND', (0, 0), (3, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        # ('FONTNAME', (0, 0), (-1, 0), 'Courier'),
        # ('FONTSIZE', (0, 0), (-1, 0), 11),
        # ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ])
    table.setStyle(style)

    # Alternar a cor do fundo
    rowNumb = len(inscricoes)
    for i in range(1, rowNumb):
        if i % 2 == 0:
            bc = colors.lightgrey
        else:
            bc = colors.white

        ts = TableStyle(
            [('BACKGROUND', (0, i), (-1, i), bc),
             ('ALIGN', (0, 1), (-1, -1), 'LEFT')]
        )
        table.setStyle(ts)

    # Adicionar bordas
    ts = TableStyle(
        [
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]
    )
    table.setStyle(ts)

    styles = getSampleStyleSheet()
    normal = styles['Normal']

    static_files_path = getattr(settings, 'STATIC_ROOT', None)
    logo_dir = static_files_path + '\imagens\logo_IFB.png'
    imagem = Image(logo_dir, 1.2 * inch, 1 * inch)

    elems = []
    elems.append(imagem)
    elems.append(Spacer(1, 0.3 * inch))
    elems.append(Paragraph("<para alignment='center'><h1><b>JOGOS DO INSTITUTO FEDERAL</b></h1></para>", styles["Normal"]))
    elems.append(Spacer(1, 0.3 * inch))
    elems.append(Paragraph('IFB - Instituto Federal de Educação, Ciência e Tecnologia de Brasília', styles["Normal"]))
    elems.append(Spacer(1, 0.2 * inch))
    elems.append(Paragraph("<h2>Unidade Organizacional: <b>%s</b></h2>" % (unidade_organizacional_nome), normal))
    elems.append(Paragraph("<h2>Modalidade: <b>%s</b></h2>" % (modalidade_nome), normal))
    elems.append(Spacer(1, 0.2 * inch))
    elems.append(table)

    elems.append(Spacer(1, 0.2 * inch))
    elems.append(Paragraph(f'Número Total de Atletas: {qtd_atletas}', styles["Normal"]))

    texto = '<p align=”justify”><font size="10">Declaro que os atletas aqui relacionados estão ' \
            'regularmente matriculados e frequentando aulas em nossa instituição de ensino:</font></p>'

    elems.append(Spacer(1, 0.2 * inch))
    elems.append(Paragraph(texto, styles["Normal"]))

    elems.append(Spacer(1, 0.5 * inch))
    elems.append(Paragraph('<para alignment="center">________________________________________</para>', styles["Normal"]))
    elems.append(Paragraph('<para alignment="center">Secretaria de Registro Escolar</para>', styles["Normal"]))
    elems.append(Paragraph('<para alignment="center">Carimbo e Assinatura</para>', styles["Normal"]))

    elems.append(Spacer(1, 0.5 * inch))
    elems.append(Paragraph('<para alignment="center">________________________________________</para>', styles["Normal"]))
    elems.append(Paragraph('<para alignment="center">Professor de Educação Física</para>', styles["Normal"]))
    elems.append(Paragraph('<para alignment="center">Assinatura</para>', styles["Normal"]))

    elems.append(Spacer(1, 0.5 * inch))
    elems.append(Paragraph('<para alignment="center">________________________________________</para>', styles["Normal"]))
    elems.append(Paragraph('<para alignment="center">Diretor Geral do Campus</para>', styles["Normal"]))
    elems.append(Paragraph('<para alignment="center">Assinatura</para>', styles["Normal"]))

    pdf.build(elems)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Ficha_Inscricao_JIF.pdf'
    response.write(pdf_buffer.getvalue())
    pdf_buffer.close()

    return response
