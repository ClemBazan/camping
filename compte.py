# coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=utf-8\n")
import psycopg2
#-----------------------------
import cgi 
import cgitb

cgitb.enable()
form=cgi.FieldStorage()

id_client=int(form.getvalue('id_client'))
code=form.getvalue('code')

html = """<!DOCTYPE html>
<html>
<body>
  <center>
  <h1>camping les flots </h1> 
    <form action="index.py" method="post">
      <input  type="submit" value="deconnexion" />
    </form>
    <form action="information.py" method="post">
      <input  type="submit" value="information sur le camping" />
    </form>
      <form action="reservation.py" method="post">
      <input  type="submit" value="reservation " />
    </form>
  </center> 
</body>
</html>
"""

html2="""
<!DOCTYPE html>
<html>
<body>
  <center>
      <form action="connexion.py" method="post">
      votre identifiant ou code est faux !veulliez reessaye
      <input  type="submit" value="retour" />
    </form>
      </center>
</body>
</html>
     """
#------------------connection----------
hostname = 'localhost'  
username = 'postgres'
password = '@toto83DBZ'
database = 'postgres'
TableTest1 = "projet.responsable"

myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()
 # Requete SQL
req = ('SELECT id_responsable,code from {}'.format(TableTest1))
cursor.execute(req)
data = cursor.fetchall() 

req = ('SELECT max(id_responsable) from {}'.format(TableTest1))
cursor.execute(req)
maxi = cursor.fetchall()    
maxir=maxi[0][0]
i=0
var=0
while(i<=maxir):
    if (id_client==data[i][0]and code==data[i][1]):
        var=1
    i=i+1
if (var==1):
    print(html)
else:
    print(html2)