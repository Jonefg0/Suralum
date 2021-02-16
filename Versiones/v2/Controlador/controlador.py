import pika,sys,os
import json


def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host ='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='estadisticos')


    def callback(ch,method,properties,body):
        print("se recibe: %r"% json.loads(body))
    
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

