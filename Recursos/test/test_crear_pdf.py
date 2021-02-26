from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm



def ventas_totales (pos,periodos,ventas_totales):
    arreglo = [periodos,ventas_totales]
    table = Table(arreglo, colWidths=3* cm)
    table.setStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT')])
    for index, row in enumerate(arreglo):
        bg_color = colors.red
        ini, fin = (0, index), (len(row)-1, index)
        table.setStyle([
            ("BOX", ini, fin, 0.25, colors.black),
            ('INNERGRID', ini, fin, 0.25, colors.black),
            ('BACKGROUND', ini, fin, bg_color)
    ])
    doc.build([table])


def familia_mas_ventas_to_pdf(pos,periodo,ventas_totales):# que familia es al que vendió más por cada periodo -> periodos[años],familia[string],ventas[valor] arreglo = [periodos,ventas_totales]
    arreglo = [periodos,ventas_totales]
    table = Table(arreglo, colWidths=3* cm)
    table.setStyle([('ALIGN', (0,10), (-1,-1), 'RIGTH')])
    for index, row in enumerate(arreglo):
        bg_color = colors.blue
        ini, fin = (0, index), (len(row)-1, index)
        table.setStyle([
            ("BOX", ini, fin, 0.25, colors.black),
            ('INNERGRID', ini, fin, 0.25, colors.black),
            ('BACKGROUND', ini, fin, bg_color)
    ])
    doc.build([table])
    return 0

def Productos_más_vendido(pos,periodo):#top 5 productos más vendidos, periodos [años],productos[largo(años)][nombre producto],totalproducto[largo(años)][valor_total]
    return 0

def ventas_total_familia_descriptivo(pos,periodo):# periodos[años],ventas_t[len(perodos)][4]
    return 0

def comparativo_Suralum(pos,periodo):#productos más vendidos en suralum,ventatotalproducto[largo(periodos)][7 valores]
    return 0

def comparativo_Huracán(pos,periodo):#productos más vendidos en suralum,ventatotalproducto[largo(periodos)][? valores]
    return 0

def Comparativo_Industrial(pos,periodo):#productos más vendidos en suralum,ventatotalproducto[largo(periodos)][? valores]
    return 0

doc = SimpleDocTemplate("example.pdf", pagesize=letter)
periodos= [2017,2018,2019]
vt = [11541548,156185612,56416646]
pos= [0,0]
ventas_totales(pos,periodos,vt)
familia_mas_ventas_to_pdf(pos,periodos,vt)