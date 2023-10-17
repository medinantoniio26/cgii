#!D:/Python/python.exe
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
    #sql = "UPDATE users SET  password=sha1('{}'), name='{}', avatar='{}', role='{}' WHERE email='{}'".format(e, p, n, a, r)
    sql = f"UPDATE users SET  password=sha1('{p}'), name='{n}', avatar='{a}', role='{r}' WHERE email='{e}'"
    cursor.execute(sql)
    con.commit()
    con.close
    print("<h1>Usuario modificado</h1>")
else:
    print("<h1>Metodo no permitido</h1>")