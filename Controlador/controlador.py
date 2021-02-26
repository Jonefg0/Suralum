import pika,sys,os
import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import cx_Oracle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing, Rect, String, Group, Line
import pprint


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host ='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='estadisticos')
    
    def callback(ch,method,properties,body):
        mensaje = json.loads(body)
        print("se recibe: %r"% mensaje)
        alpdf(str(mensaje))
    
    def alpdf(mensaje):
        aux = mensaje.split('#')
        periodos = aux[0][2:-4].split(",")
        descriptores = aux [1][4:-2].split(",")
        #valor = int(descriptores[0])
        #print("valor:",valor)
        #año = int(años_final[0][1:-1])
        print("descriptores: ",descriptores)
        print("periodos ",periodos)
        doc = SimpleDocTemplate("example.pdf", pagesize=letter)
        story = []

        if (int(descriptores[0])):#VENTAS TOTALES
            print("ventas_totales")
            totales = []
            connection_ddbb = cx_Oracle.connect("nathan", "m94", "localhost")
            cursor = connection_ddbb.cursor()   
            for i in periodos:
                print()
                cursor = connection_ddbb.cursor()
                cursor.execute("SELECT id_venta, subtotal, fecha FROM ventas WHERE EXTRACT(YEAR FROM fecha) = " + i)
                total = 0
                for fname in cursor:
                    total = total+ fname[1]
                    #print ("Values:", fname[1])
                totales.append(total)
            
        
                    
        
        if (int(descriptores[1][1:])):
            print("ventas por lineas")

        if (int(descriptores[2][1:])):
            print("Ventas por familia")

        if (int(descriptores[3][1:])):
            print("Suralum")

        if (int(descriptores[4][1:])):
            print("Huracan")

        if (int(descriptores[5][1:])):
            print("Industrial")
        
        if (int(descriptores[6][1:])):
            print("mas vendido")

    
    channel.basic_consume(queue='estadisticos', on_message_callback = callback, auto_ack = True)
    print("esperando mensajes: ")
    channel.start_consuming()


    #consultas
'''
    def ventas_totales (pos,periodos):#ventas totales en cada periodo -> periodos[],totales[]
        return 0   
    def familia_más_ventas():# que familia es al qu vendió más por cada periodo -> periodos[años],familia[string],ventas[valor]
        return 0
    def Productos_más_vendido():#top 5 productos más vendidos, periodos [años],productos[largo(años)][nombre producto],totalproducto[largo(años)][valor_total]
        return 0
    def ventas_total_familia_descriptivo(pos,periodo):# periodos[años],ventas_t[len(perodos)][4]
        return 0
    def comparativo_Suralum(pos,periodo):#productos más vendidos en suralum,ventatotalproducto[largo(periodos)][7 valores]
        return 0
    def comparativo_Huracán(pos,periodo):#productos más vendidos en suralum,ventatotalproducto[largo(periodos)][? valores]
        return 0
    def Comparativo_Industrial():#productos más vendidos en suralum,ventatotalproducto[largo(periodos)][? valores]
        return 0
   
'''


if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Se interrumpe')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

