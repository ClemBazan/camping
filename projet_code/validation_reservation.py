# 3 eme page de reservation 
# reste test de 2 location je pense crée un espace compte 
# il y a aussi acompte a faire 

#noublie pas de changer les codes de connection et surement la table avec 


# coding: utf-8
import psycopg2
#-----------------------------
import cgi 
import cgitb
#------------------------------recuperation des variable 
cgitb.enable()
form=cgi.FieldStorage()
nom_groupe=form.getvalue('nom_groupe')
demi_pension =form.getvalue('demi_pension')
dated= form.getvalue('dated')
datef=form.getvalue('datef')
#responsable
prenomr=form.getvalue('prenomr')
nomr=form.getvalue('nomr')
telr=form.getvalue('telr')
e_mailr=form.getvalue('e_mailr')
adresser=form.getvalue('adresser')
#acompagnant1
prenom1=form.getvalue('prenom1')
nom1=form.getvalue('nom1')
tel1=form.getvalue('tel1')
e_mail1=form.getvalue('e_mail1')
adresse1=form.getvalue('adresse1')
#acompagnant2
prenom2=form.getvalue('prenom2')
nom2=form.getvalue('nom2')
tel2=form.getvalue('tel2')
e_mail2=form.getvalue('e_mail2')
adresse2=form.getvalue('adresse2')
#acompagnant3
prenom3=form.getvalue('prenom3')
nom3=form.getvalue('nom3')
tel3=form.getvalue('tel3')
e_mail3=form.getvalue('e_mail3')
adresse3=form.getvalue('adresse3')
#acompagnant4
prenom4=form.getvalue('prenom4')
nom4=form.getvalue('nom4')
tel4=form.getvalue('tel4')
e_mail4=form.getvalue('e_mail4')
adresse4=form.getvalue('adresse4')
#acompagnant5
prenom5=form.getvalue('prenom5')
nom5=form.getvalue('nom5')
tel5=form.getvalue('tel5')
e_mail5=form.getvalue('e_mail5')
adresse5=form.getvalue('adresse5')
#acompagnant6
prenom6=form.getvalue('prenom6')
nom6=form.getvalue('nom6')
tel6=form.getvalue('tel6')
e_mail6=form.getvalue('e_mail6')
adresse6=form.getvalue('adresse6')
#acompagnant7
prenom7=form.getvalue('prenom7')
nom7=form.getvalue('nom7')
tel7=form.getvalue('tel7')
e_mail7=form.getvalue('e_mail7')
adresse7=form.getvalue('adresse7')

nbr_perso=int(form.getvalue('nbr_perso'))

#-----------------espace html -----------------
print("Content-type: text/html; charset=utf-8\n")


htmld= """<!DOCTYPE html>
<html>
<body>"""

htmlf="""
</body>
</html>
"""
#------------------connection----------
hostname = 'localhost'  
username = 'postgres'
password = '@toto83DBZ'
database = 'postgres'
TableTest1 = "projet.client"
TableTest2 = "projet.reservation"

myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()
#--------------------------- enregistrement-------
#---------------------nom de la famillle existe 

#----------------------------------------------
#---------------------ajouter 
# Requete SQL
sqlreservation = """INSERT INTO projet.reservation (id_reservation,datef,nom_groupe,present,dated,demi_pension,id_client)
VALUES (%s,%s,%s,%s,%s,%s,%s)"""
sqlclient = """INSERT INTO projet.client (id_client, nom, prenom,tel,mail,adresse,responsable,nom_groupe)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

i=1

#---------------------------------------
while(i<=nbr_perso):
# Requete SQL
    reqmaxid_client = ('SELECT max(id_client) from {}'.format(TableTest1))

# Exécution de la requête
    cursor.execute(reqmaxid_client)
# Sortie à l'écran
    data = cursor.fetchall()    
    maxi=data[0][0]+1

# on met dans la base de donnée les personne en fonction de i qui va de 1 a max personne 
    if i==1:
        value = (maxi, nomr,prenomr,telr,e_mailr,adresser,1,nom_groupe)
        #--------insertiond dans la table reservation 
        reqmaxid_reservation = ('SELECT max(id_reservation) from {}'.format(TableTest2))
        cursor.execute(reqmaxid_reservation)
        datar = cursor.fetchall()    
        maxir=datar[0][0]+1
        value1 = (maxir,datef,nom_groupe, 0,dated,demi_pension,maxi)
        cursor .execute(sqlreservation,value1)
        myConnection .commit()
        count = cursor .rowcount
    if i==2:
        value = (maxi, nom1,prenom1,tel1,e_mail1,adresse1,0,nom_groupe)
    if i==3:
        value = (maxi, nom2,prenom2,tel2,e_mail2,adresse2,0,nom_groupe)
    if i==4:
        value = (maxi, nom3,prenom3,tel3,e_mail3,adresse3,0,nom_groupe)
    if i==5:
        value = (maxi, nom4,prenom4,tel4,e_mail4,adresse4,0,nom_groupe)
    if i==6:
        value = (maxi, nom5,prenom5,tel5,e_mail5,adresse5,0,nom_groupe)
    if i==7:
        value = (maxi, nom6,prenom6,tel6,e_mail6,adresse6,0,nom_groupe)
    if i==8:
        value = (maxi, nom7,prenom7,tel7,e_mail7,adresse7,0,nom_groupe)
    i=i+1
# Exécution de la requête
    cursor .execute(sqlclient, value)
# validé la modification
myConnection .commit()
count = cursor .rowcount
print(htmld)
print("""votre reservation est faite""")
print(htmlf)
#------------------------programme principal ---------



