import cx_Oracle

connection = cx_Oracle.connect("nathan", "m94", "localhost")
cursor = connection.cursor()
cursor.execute("""
        SELECT
    id_venta,
    subtotal,
    fecha
FROM
    ventas""",)

for fname in cursor:
    print ("Values:", fname)

año ="2017"

cursor.execute("""SELECT id_venta, subtotal, fecha FROM ventas WHERE EXTRACT(YEAR FROM fecha) = 2017""")

for fname in cursor:
    print ("Familia:", fname)
