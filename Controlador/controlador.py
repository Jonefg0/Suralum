import pika,sys,os
import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import cx_Oracle


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
        print ("años: ", aux[0])
        print("descriptores: ",aux [1])
        w, h = A4
        c = canvas.Canvas("Suralam.pdf", pagesize=A4)
        c.drawString(50, h - 50, mensaje)
        c.showPage()
        c.save()

    
    channel.basic_consume(queue='estadisticos', on_message_callback = callback, auto_ack = True)
    print("esperando mensajes: ")
    channel.start_consuming()


    #consultas

    def ventas_totales (pos,periodos):#ventas totales en cada periodo -> periodos[],totales[]
        for i in periodos:
            connection = cx_Oracle.connect("nathan", "m94", "localhost")
            cursor = connection.cursor()
            cursor.execute("""
            SELECT
            id_venta,
            subtotal,
            fecha
            FROM
            ventas""")
            
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
   



if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Se interrumpe')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

