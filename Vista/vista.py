from tkinter import *
import numpy as np
import pika
import json

#funciones

def generar_reporte():
    seleccionados = [0,0,0,0,0,0,0]
    seleccionados[0] = estadistico_1.get()
    seleccionados[1] = estadistico_2.get()
    seleccionados[2] = estadistico_3.get()
    seleccionados[3] = estadistico_4.get()
    seleccionados[4] = estadistico_5.get()
    seleccionados[5] = estadistico_6.get()
    seleccionados[6] = estadistico_7.get()
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='estadisticos')
    print("los estadisticos son: ",seleccionados)
    msg = (periodos,"#",seleccionados)
    print("mensaje que se envía es : ", msg)
    channel.basic_publish(exchange='', routing_key='estadisticos', body = json.dumps(msg))
    seleccionados = [0,0,0,0,0,0,0]
    connection.close()

def agregar_periodo():
    print(periodo.get())
    lista.insert(END,periodo.get())
    periodos.append(periodo.get())


def borrar_periodo():
    sel = lista.curselection()
    for index in sel[::-1]:
        lista.delete(index)
        periodos.pop(index)

#Ventana y variables
ventana = Tk()
ventana.geometry("900x600")
ventana.title("Estadisticas Suralum")
#frame_fechas = Frame(ventana,bg = "black").place(x = 500,y = 200)
estadistico_1 = IntVar()
estadistico_2 = IntVar()
estadistico_3 = IntVar()
estadistico_4 = IntVar()
estadistico_5 = IntVar()
estadistico_6 = IntVar()
estadistico_7 = IntVar()
periodo = StringVar()
periodos = []


#cabecera
titulo = Label(ventana,text = "Estadisticas Suralum", bg = "blue",fg = "white", font = ("Times New Roman",24)).place(x=330,y=5)
#descriptores
titulo_descriptores = Label(ventana,text = "Descriptores", font = ("Helvetica",18)).place(x = 100, y = 70)
vt_button = Checkbutton(ventana,text="Ventas Totales",onvalue = 1,offvalue = 0, variable = estadistico_1, font = ("Helvetica",18)).place(x = 100, y = 100)
vxl_button = Checkbutton(ventana,text="Ventas por línea",onvalue = 1,offvalue = 0, variable = estadistico_2, font = ("Helvetica",18)).place(x = 100, y = 130)
vxf_button = Checkbutton(ventana,text="Ventas por familia", onvalue = 1,offvalue = 0, variable = estadistico_3, font = ("Helvetica",18)).place(x = 100, y = 160)
vxs_button = Checkbutton(ventana,text="Ventas Suralum", onvalue = 1,offvalue = 0, variable = estadistico_4, font = ("Helvetica",18)).place(x = 100, y = 190)
vxh_button = Checkbutton(ventana,text="Ventas Huracán",onvalue = 1,offvalue = 0, variable = estadistico_5, font = ("Helvetica",18)).place(x = 100, y = 220)
vxi_button = Checkbutton(ventana,text="Ventas Industrial",onvalue = 1,offvalue = 0, variable = estadistico_6, font = ("Helvetica",18)).place(x = 100, y = 250)
pmv_button = Checkbutton(ventana,text="Producto más vendido",onvalue = 1,offvalue = 0, variable = estadistico_7, font = ("Helvetica",18)).place(x = 100, y = 280)


#ingreso de periodos

titulo_fechas = Label(ventana,text = "Periodos", font = ("Helvetica",18)).place(x = 500, y = 70 )
cta_fechas = Label(ventana, text = "Ingrese año: ", font = ("Helvetica",18)).place(x = 500, y = 100)
caja_año = Entry(ventana, textvar = periodo, font = ("Helvetica",18),width = "5").place(x = 650, y = 100)
f_button = Button(ventana, text ="Agregar",font = ("Helvetica",18),command = agregar_periodo).place(x = 750, y = 97)

#periodos agregados

lista = Listbox(ventana)
lista.pack()
lista.place(x = 500, y = 160)
borrar_button = Button(ventana, text = "Borrar periodo", font = ("Helvetica",18), command = borrar_periodo).place(x = 670, y = 160)



#botón generar reporte
r_button = Button(ventana, text = "Generar reporte", padx = 10, pady = 10, command = generar_reporte, font = ("Helvetica",16)).place(x = 700, y = 500 )


ventana.mainloop()