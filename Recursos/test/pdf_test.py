from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm


doc = SimpleDocTemplate("example.pdf", pagesize=letter)

answers = [['00', '01'],
           ['02', '03', '04', '05'],
           ['06', '07', '08'],
           ['09', '10', '11', '12', '13'],
           ['14', '15', '16'],
           ['17', '18'],
           ['19', '20', '21', '22']
           ]

table = Table(answers, colWidths=1 * cm)
table.setStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT')])

for index, row in enumerate(answers):
    bg_color = colors.white if index % 2 else colors.lightgrey
    ini, fin = (0, index), (len(row)-1, index)
    table.setStyle([
        ("BOX", ini, fin, 0.25, colors.black),
        ('INNERGRID', ini, fin, 0.25, colors.black),
        ('BACKGROUND', ini, fin, bg_color)
    ])

doc.build([table])