import cx_Oracle

connection = cx_Oracle.connect("nathan", "m94", "localhost")
cursor = connection.cursor()

año ='2019'

#cursor.execute("""SELECT
 #                   productos.descripcion,
  #                  SUM(venta_productos.cantidad) as v,
   #                 SUM(venta_productos.cantidad * venta_productos.precio) as c,
    #                productos.id_familia
       #         FROM
        #            venta_productos JOIN productos ON venta_productos.id_producto = productos.id_producto JOIN ventas ON venta_productos.id_venta=ventas.id_venta
         #       WHERE EXTRACT(YEAR FROM ventas.fecha) = """+año+"""
          #      GROUP BY 
           #         productos.descripcion
            #    ORDER BY
             #       v ASC"""
#nombreusuario_verify= 'brain'
#contrasenausuario_verify='brain'
#cursor.execute("SELECT total,opeid FROM ventas WHERE EXTRACT(YEAR FROM fecha) = 2017")
#descontar = 0
#for valor in cursor:
 #   print ("opeid:", valor[1],"total:",valor[0])
    
    #else:
     # total = total +valor[0]
#print("desc:",descontar)
#print("total:",total)    


#cursor.execute("SELECT SUM(total) FROM ventas WHERE (EXTRACT(YEAR FROM fecha) = 2017 AND opeid NOT IN (50, 52, 55, 56, 60, 61))")
#descontar = 0
#total = 0
#for valor in cursor:
 #     total = total +valor[0]
#print("desc:",descontar)
#print("total:",total)    


cursor.execute("SELECT subtotal,opeid FROM ventas WHERE EXTRACT(YEAR FROM fecha) = 2017")
descontar = 0
total = 0
for valor in cursor:
    print ("opeid:", valor[1],"total:",valor[0])
    if (valor[1]!=52 and valor[1]!=50):
      if ((valor[1]==61)):#descuentos
        descontar = descontar +valor[0]
      if(valor[1]==33 or valor[1]==56 or valor[1]==30):#totales
        total = total + valor[0]



print("desc:",descontar)
print("total:",total)   
print("total real :", total-descontar) 






#if cursor.fetchall():
   # print("INICIO CORRECTO")
#else:
#    print("NACA LA PIRINACA")

#cursor.execute("SELECT id_venta, subtotal, fecha FROM ventas WHERE EXTRACT(YEAR FROM fecha) = " + año)

#consulta total venta familia por periodo
#cursor.execute("""SELECT
#    SUM(ventas.subtotal) as c
#FROM
#    ventas
#WHERE EXTRACT(YEAR FROM ventas.fecha) = 2017
#""")
#total = 0
#for valor in cursor:
#    print ("Values:", valor)
  
  #  total = total + valor[1]

#print("#############################",total*0.81,"####################################")

#total familias
#cursor.execute("""SELECT
 #   productos.id_familia,
  #  SUM(venta_productos.cantidad) as c,
   # SUM(venta_productos.precio)
    
#FROM
#    venta_productos INNER JOIN productos ON venta_productos.id_producto = productos.id_producto JOIN ventas ON venta_productos.id_venta=ventas.id_venta
#WHERE EXTRACT(YEAR FROM ventas.fecha) = """+año+"""AND(productos.id_familia=1 OR productos.id_familia=2 OR productos.id_familia=3)
#GROUP BY
#    productos.id_familia
#ORDER BY
#     ASC
#""")

#cursor.execute("""SELECT
#    SUM(venta_productos.cantidad) as c,
#    SUM(ventas.subtotal) as v
#FROM
#    venta_productos JOIN productos ON venta_productos.id_producto = productos.id_producto JOIN ventas ON venta_productos.id_venta=ventas.id_venta
#WHERE EXTRACT(YEAR FROM ventas.fecha) = 2017 AND productos.id_familia=1#GROUP BY
#   productos.id_familia
#ORDER BY
#    v DESC""")


#total = 0
#vt = []
#for valor in cursor:
#    print ("Values:", valor)
#    vt.append(valor[2])
#print(vt)

#for fname in cursor:
#    print ("Familia:", fname)


  
