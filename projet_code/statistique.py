# coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=utf-8\n")
import cgi 
import cgitb
import psycopg2

cgitb.enable()
form=cgi.FieldStorage()

valeur=form.getvalue('valeur')

htmld = """<!DOCTYPE html>
<html>
<head>
  <head>
    <style>
      body {
      -webkit-animation: colorchange 20s infinite;
      animation: colorchange 20s infinite;
      }
      @-webkit-keyframes colorchange {
      0%  {background: #ff0000;}
      5%  {background: #fff300;}
      10%  {background: #0cff00;}
      15%  {background: #00ffec;}
      20% {background: #ff00d8;}
      25%  {background: #f3ff00;}
      30%  {background: #0027ff;}
      35%  {background: #ffbdf5;}
      40% {background: #2ddf6e;}
      45%  {background: #df2db7}
      50%  {background: #ff0000;}
      55%  {background: #ff0000;}
      60%  {background: #fff300;}
      65%  {background: #0cff00;}
      70%  {background: #00ffec;}
      75% {background: #ff00d8;}
      80%  {background: #f3ff00;}
      85%  {background: #0027ff;}
      90%  {background: #ffbdf5;}
      95% {background: #2ddf6e;}
      100%  {background: #ff0000;}
      }

    </style>
  </head>
<body>
    <form action="statistique.py" method="post">
        <input  type="submit" name="valeur" value="tout les client" />
    </form>
    <form action="statistique.py" method="post">
        <input  type="submit" name="valeur" value="le nombre de client qui sont venue dans notre camping" />
    </form>
    <form action="statistique.py" method="post">
        <input  type="submit" name="valeur" value="le nombre de compte?" />
    </form>
    <form action="index.py" method="post">
        <input  type="submit" value="retour" />
    </form>
</body>
</html>
"""
table="""<table> 
   <tr>
        <th>id_client</th>
       <th>Nom</th>
       <th>prenom</th>
       <th>tel</th>
        <th>e-mail</th>
         <th>adresse</th>
         <th>groupe </th>
   </tr>"""
#------------------connection----------
hostname = 'localhost'  
username = 'postgres'
password = '@toto83DBZ'
database = 'postgres'
TableTest1 = "projet.client"
TableTest2 = "projet.responsable"

myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()


if(valeur=="tout les client"):
    req = ('SELECT * from {}'.format(TableTest1))
    cursor.execute(req)
    data = cursor.fetchall()  
    i=0
    n=len(data)
    print(htmld)
    while(i<n):
        print(f"{data[i]}")
        print(""" <br>""")
        i=i+1
elif (valeur=="le nombre de client qui sont venue dans notre camping"):
    req = ('SELECT max(id_client) from {}'.format(TableTest1))
    cursor.execute(req)
    data = cursor.fetchall()  
    print(htmld)
    print(f" le nombre de client depuis sont ouverture est :{data[0][0]}")
elif (valeur=="le nombre de compte?"):
    req = ('SELECT max(id_responsable) from {}'.format(TableTest2))
    cursor.execute(req)
    data = cursor.fetchall()  
    print(htmld)
    print(f" le nombre de compte cree depuis sont ouverture est :{data[0][0]}")
else:
    print(htmld)