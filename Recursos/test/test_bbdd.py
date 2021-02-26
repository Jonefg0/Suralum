import cx_Oracle

connection = cx_Oracle.connect("nathan", "m94", "localhost")
cursor = connection.cursor()



año ='2017'
cursor.execute("SELECT id_venta, subtotal, fecha FROM ventas WHERE EXTRACT(YEAR FROM fecha) = " + año)
total = 0
for fname in cursor:
    total = total+ fname[1]
    print ("Values:", fname[1])
print (total)




#for fname in cursor:
#    print ("Familia:", fname)


    
