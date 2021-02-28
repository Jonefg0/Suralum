import cx_Oracle

connection = cx_Oracle.connect("nathan", "m94", "localhost")
cursor = connection.cursor()



año ='2019'

cursor.execute("""SELECT
                    productos.descripcion,
                    SUM(venta_productos.cantidad) as v,
                    SUM(venta_productos.cantidad * venta_productos.precio) as c
                FROM
                    venta_productos JOIN productos ON venta_productos.id_producto = productos.id_producto JOIN ventas ON venta_productos.id_venta=ventas.id_venta
                WHERE EXTRACT(YEAR FROM ventas.fecha) = """+año+"""AND productos.id_familia=2
                GROUP BY
                    productos.descripcion
                ORDER BY
                    v ASC"""
                )
for valor in cursor:
    print ("Values:", valor)

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


  
