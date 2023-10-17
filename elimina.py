#!C:/Python311/python.exe
import mysql.connector
import os
import cgi
import cgitb
cgitb.enable()
print("Content-type: text/html\n")
print()

metodo = os.environ["REQUEST_METHOD"]

if metodo == "POST":
    dato = cgi.FieldStorage()
    e = dato.getvalue("email")
    con= mysql.connector.connect(user='root', password='', host='127.0.0.1', database='foro')
    cursor = con.cursor()
    #sql = "UPDATE users SET  password=sha1('{}'), name='{}', avatar='{}', role='{}' WHERE email='{}'".format(e, p, n, a, r)
    sql = f"DELETE FROM users WHERE email='{e}'"
    cursor.execute(sql)
    con.commit()
    con.close
    print("<h1>Usuario Eliminado</h1>")
else:
    print("<h1>Metodo no permitido</h1>")