from tkinter import *
import pika
import json
import cx_Oracle


def menu_pantalla():
    global ventanamain
    ventanamain = Tk()
    ventanamain.geometry("500x400")
    ventanamain.title("Bienvenido al Sistema Suralum")

    Label(ventanamain,text ="Acceso al sistema",bg="royal blue",fg="white",width="300",font=("Helvetica",15)).pack()
    Label(ventanamain,text ="").pack()
    global imagen
    imagen = PhotoImage(file="bg.gif")


    Button(ventanamain,text = "Iniciar sesión",height="3",width="30",bg = "blue",command = inicio_sesion).pack()
    Button(ventanamain,text = "Registro(Under construction)",height="3",width="30").pack()


    ventanamain.mainloop()

def validaciondatos():
        connection_ddbb = cx_Oracle.connect('nathan','m94', "localhost")
        cursor = connection_ddbb.cursor()
    
        print(nombreusuario_verify)
        user = str(nombreusuario_verify)
        print(user,"dif/n")
        cursor.execute("SELECT password FROM  users WHERE username='"+nombreusuario_verify.get()+"' and password='"+contrasenausuario_verify.get()+"'")
        if (cursor.fetchall()):
            print("INICIO CORRECTO")
            ventana_principal()
        else:
            print("ERROR DE CONTRASEÑA")


        

def inicio_sesion():
    ventanamain.withdraw()

    global ventana_sesion
    ventana_sesion = Toplevel(ventanamain)
    ventana_sesion.geometry("500x300")
    ventana_sesion.title("Inicio de sesion")

    Label(ventana_sesion,text = "Ingrese su Usuario y  Contraseña").pack()
    Label(ventana_sesion,text = "").pack()

    global nombreusuario_verify 
    global contrasenausuario_verify

    nombreusuario_verify = StringVar()
    contrasenausuario_verify=StringVar()

    global nombreusuario_entry 
    global constrasenausuario_entry

    Label(ventana_sesion,text = "Usuario").pack()
    nombreusuario_entry = Entry(ventana_sesion,textvariable = nombreusuario_verify)
    nombreusuario_entry.pack()
    Label(ventana_sesion).pack()

    Label(ventana_sesion,text = "Contraseña").pack()
    constrasenausuario_entry = Entry(ventana_sesion,textvariable = contrasenausuario_verify)
    constrasenausuario_entry.pack()
    Label(ventana_sesion).pack()
    Button(ventana_sesion,text ="A darle átomos",command = validaciondatos).pack()




def ventana_principal():
    ventana_sesion.withdraw()
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
    ventana = Toplevel(ventanamain)
    ventana.geometry("800x600")
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
    #imagen = PhotoImage(file = "bg.png")
    #Label(ventana,image=imagen).place(x=0,y=0)
    
    Label(ventana,image=imagen).place(x=0,y=0)


    #cabeceratitulo = Label(ventana,text = "Estadisticas Suralum", bg = '#FFF9C2',fg = '#274a99', font = ("Helvetica",24,"bold")).place(x=230,y=80)
    titulo = Label(ventana,text = "Estadisticas Suralum", bg = '#FFF9C2',fg = '#274a99', font = ("Helvetica",24,"bold")).place(x=230,y=80)
    #descriptores
    titulo_descriptores = Label(ventana,text = "Descriptores", font = ("Helvetica",18,"bold"),bg = '#FFF9C2').place(x = 450, y = 140)

    vt_button = Checkbutton(ventana,text="Ventas Totales",onvalue = 1,offvalue = 0, variable = estadistico_1, font = ("Helvetica",14),bg = '#FFF9C2').place(x = 450, y = 180)
    vxl_button = Checkbutton(ventana,text="Ventas por línea",onvalue = 1,offvalue = 0, variable = estadistico_2, font = ("Helvetica",14),bg = '#FFF9C2').place(x = 450, y = 210)
    vxf_button = Checkbutton(ventana,text="Ventas por familia", onvalue = 1,offvalue = 0, variable = estadistico_3, font = ("Helvetica",14),bg = '#FFF9C2').place(x = 450, y = 240)
    vxs_button = Checkbutton(ventana,text="Ventas Suralum", onvalue = 1,offvalue = 0, variable = estadistico_4, font = ("Helvetica",14),bg = '#FFF9C2').place(x = 450, y = 270)
    vxh_button = Checkbutton(ventana,text="Ventas Huracán",onvalue = 1,offvalue = 0, variable = estadistico_5, font = ("Helvetica",14),bg = '#FFF9C2').place(x = 450, y = 300)
    vxi_button = Checkbutton(ventana,text="Ventas Industrial",onvalue = 1,offvalue = 0, variable = estadistico_6, font = ("Helvetica",14),bg = '#FFF9C2').place(x = 450, y = 330)
    pmv_button = Checkbutton(ventana,text="Producto más vendido",onvalue = 1,offvalue = 0, variable = estadistico_7, font = ("Helvetica",14),bg = '#FFF9C2').place(x = 450, y = 360)


    #ingreso de periodos
    titulo_fechas = Label(ventana,text = "Periodos", font = ("Helvetica",18,"bold"),bg = '#FFF9C2').place(x = 20, y = 140 )
    cta_fechas = Label(ventana, text = "Ingrese año: ", font = ("Helvetica",14),bg = '#FFF9C2').place(x = 20, y = 180)
    caja_año = Entry(ventana, textvar = periodo, font = ("Helvetica",14),bg = "white",width = "6").place(x = 140, y = 180)
    f_button = Button(ventana, text ="Agregar",font = ("Helvetica",12),bg = '#274a99', fg="white", command = agregar_periodo).place(x = 220, y = 178)

    lista = Listbox(ventana, width=46)
    lista.pack() 
    lista.place(x = 20, y = 240)
        
    borrar_button = Button(ventana, text = "Borrar periodo", font = ("Helvetica",12),bg = '#274a99', fg="white", width=30, command = borrar_periodo).place(x = 20, y = 420)

    #botón generar reporte
    r_button = Button(ventana, text = "Generar reporte", padx = 10, pady = 10, bg = '#274a99', fg="white", width=13, command = generar_reporte, font = ("Helvetica",14)).place(x = 600, y = 520 )

    #botón cerrar sesión
    c_button = Button(ventana, text ="Cerrar Sesión",font = ("Helvetica",12),bg = '#274a99', fg="white", command=ventana.destroy).place(x = 600, y = 25)


menu_pantalla()




