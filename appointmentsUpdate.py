#! C:/Users/HP/AppData/Local/Programs/Python/Python310/python
print("Content-Type:text/html")
print()
import cgi
form=cgi.FieldStorage()
t1=form.getvalue("t1")
t2=form.getvalue("t2")
t3=form.getvalue("t3")
t4=form.getvalue("t4")
t5=form.getvalue("t5")
t6=form.getvalue("t6")
import mysql.connector

try:
  if form.getvalue("b2")=="Update":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    cur=con.cursor()
    cur.execute("update appointments set appnum='"+t2+"',type='"+t3+"',date1='"+t4+"',descr='"+t5+"',doctor_id='"+t6+"' where id='"+t1+"'")
    con.commit()
    print("<script>alert('Record Updated....')</script>")

except Exception as e:
   print("<script>alert('Error...')</script>")