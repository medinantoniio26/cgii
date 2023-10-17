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
    p = dato.getvalue("password")
    n = dato.getvalue("name")
    a = dato.getvalue("avatar")
    r = dato.getvalue("role")
    con= mysql.connector.connect(user='root', password='', host='127.0.0.1', database='foro')
    cursor = con.cursor()
    sql = "INSERT INTO users VALUES ('{}', sha1('{}'), '{}', '{}', '{}')".format(e, p, n, a, r)
    cursor.execute(sql)
    con.commit()
    con.close
    print("<h1>Usuario agregado</h1>")
else:
    print("<h1>Metodo no permitido</h1>")