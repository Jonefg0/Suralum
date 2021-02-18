import pika,sys,os
import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host ='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='estadisticos')


    def callback(ch,method,properties,body):
        mensaje = json.loads(body)
        print("se recibe: %r"% mensaje)
        alpdf(str(mensaje))
    
    def alpdf(mensaje):
        w, h = A4
        c = canvas.Canvas("hola-mundo.pdf", pagesize=A4)
        c.drawString(50, h - 50, mensaje)
        c.showPage()
        c.save()

    
    channel.basic_consume(queue='estadisticos', on_message_callback = callback, auto_ack = True)
    print("esperando mensajes: ")
    channel.start_consuming()



if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Se interrumpe')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

