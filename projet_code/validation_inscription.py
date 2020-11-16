#coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=utf-8\n")
# coding: utf-8
import psycopg2
#-----------------------------
import cgi 
import cgitb

cgitb.enable()
form=cgi.FieldStorage()

prenom=form.getvalue('prenom')
nom=form.getvalue('nom')
tel=form.getvalue('tel')
e_mail=form.getvalue('e_mail')
adresse=form.getvalue('adresse')
age=int(form.getvalue('age'))
code=form.getvalue('code')

# faire par rapport a la saison 
html = """<!DOCTYPE html>
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


<body>""" 
htmlf="""
<form action="index.py" method="post">
<input  type="submit" value="retour" />
</form>
<center> 

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


if(age<18):# le text du majeur jai pas fais deux location encore 
    print(html)
    print("""le responsable doit etre etre majeur """)
    print(htmlf)
else:
    # Requete SQL
    reqmaxid_client = ('SELECT max(id_responsable) from {}'.format(TableTest1))
    # Exécution de la requête
    cursor.execute(reqmaxid_client)
    # Sortie à l'écran
    data = cursor.fetchall()    
    maxi=data[0][0]+1
    sql = """INSERT INTO projet.responsable(id_responsable, nom, prenom,tel,e_mail,adresse,code)
    VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    value = (maxi, nom,prenom,tel,e_mail,adresse,code)
    cursor .execute(sql, value)
    # validé la modification
    myConnection .commit()
    count = cursor .rowcount
    print(html)
    print("""votre inscription est parfaite!!! """)
    print(f"""identifiant est :{maxi} <br>
    et votre code :{code}""")
    print(htmlf)
