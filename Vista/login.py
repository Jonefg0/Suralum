from tkinter import *


ventana = Tk()
ventana.geometry("600x400")
ventana.title("Login")
user = StringVar()
passw = StringVar()



usuario = Label(ventana,text = "Usuario", font = ("Helvetica",15))
caja_usuario = Entry(ventana, textvar = user, font = ("Helvetica",18),width = "14")
caja_password =Entry(ventana, textvar = passw, font = ("Helvetica",18),width = "14")
password = Label(ventana,text = "Contraseña", font = ("Helvetica",15))
login_button = Button(ventana,text = "Ingresar",font = ("Helvetica",15))



usuario.pack()
usuario.place(x = 100, y = 100)
caja_usuario.pack()
caja_usuario.place(x=250, y = 95)
password.pack()
password.place(x = 100, y = 150)
caja_password.pack()
caja_password.place(x = 250, y = 145)
login_button.pack()
login_button.place(x = 300,y = 300)




ventana.mainloop()