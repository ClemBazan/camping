
# coding: utf-8
# 2eme page inscription 
# inscription des personnne dans la location


#---------------------------initialise les variables-----------------
import cgi 
import cgitb

cgitb.enable()
form=cgi.FieldStorage()
nbr_perso=int(form.getvalue('nbr_personne'))
typee=form.getvalue("type")
duree=int(form.getvalue('duree'))
dated=form.getvalue('dated')
datef =form.getvalue('datef')
nom_groupe=form.getvalue('nom_groupe')
demi_pension =form.getvalue('demi_pension')
print("Content-type: text/html; charset=utf-8\n")
#------------------------------------------------------------
# ---------------------------variable pour html -----------------

htmld = """<!DOCTYPE html>
<html>
<body>
<form action="validation_reservation.py" method="post">


"""
htmlf="""
<input type="submit" value="valider" />
</form>
<form action="reservation.py" method="post">
 <input type="submit" value="retour" />
</form>
</body>
</html>
"""
responsable=""" 
    <tr> 
    <th> responsable  </th>
   <th> <input type="text" name="nomr">   </th>
    <th><input type="text" name="prenomr">   </th>
   <th> <input type="text" name="telr">  </th>
   <th> <input type="text" name="e_mailr">  </th>
   <th>  <input type="text" name="adresser">   </th>
    </tr>
"""
inscription1=""" 
    <tr>
    <th> acompagnant 1  </th>
     <th><input type="text" name="nom1">   </th>
   <th> <input type="text" name="prenom1">   </th>
   <th>  <input type="text" name="tel1">   </th>
   <th> <input type="text" name="e_mail1">   </th>
   <th> <input type="text" name="adresse1">  </th>
    </tr>
"""
inscription2=""" 
    <tr>
    <th>acompagnant 2 </th>
    <th><input type="text" name="nom2">  </th>
   <th> <input type="text" name="prenom2"> </th>
    <th> <input type="text" name="tel2">   </th>
   <th> <input type="text" name="e_mail2">   </th>
    <th> <input type="text" name="adresse2">  </th>
    </tr>
"""
inscription3=""" 
    <tr>
    <th> acompagnant 3  </th>
  <th> <input type="text" name="nom3">   </th>
   <th> <input type="text" name="prenom3">  </th>
  <th> <input type="text" name="tel3"> </th>
  <th>  <input type="text" name="e_mail3">   </th>
   <th>  <input type="text" name="adresse3"> </th>
    </tr>
"""
inscription4=""" 
    <tr>
    <th>acompagnant 4 </th>
    <th> <input type="text" name="nom4">  </th>
 <th>  <input type="text" name="prenom4">   </th>
   <th>  <input type="text" name="tel4">   </th>
    <th> <input type="text" name="e_mail4">  </th>
  <th>  <input type="text" name="adresse4">  </th>
    </tr>
"""
inscription5=""" 
   <tr>
   <th> acompagnant 5  </th>
   <th>  <input type="text" name="nom5"> </th>
  <th> <input type="text" name="prenom5">   </th>
  <th> <input type="text" name="tel5">   </th>
   <th> <input type="text" name="e_mail5">   </th>
  <th>  <input type="text" name="adresse5">   </th>
    </tr>
"""
inscription6=""" 
   <tr>
   <th> acompagnant 6 </th>
   <th> <input type="text" name="nom6">  </th>
    <th> <input type="text" name="prenom6">  </th>
  <th>  <input type="text" name="tel6"> </th>
   <th>  <input type="text" name="e_mail6">   </th>
   <th>  <input type="text" name="adresse6"> </th>
    </tr>
"""
inscription7=""" 
    <tr>
    <th> acompagnant 7</th>
   <th> <input type="text" name="nom7">   </th>
  <th>  <input type="text" name="prenom7">   </th>
  <th>  <input type="text" name="tel7">   </th>
   <th>  <input type="text" name="e_mail7">   </th>
  <th>  <input type="text" name="adresse7"></th>   </th>
    </tr>
"""
table="""<table> 
   <tr>
        <th>titre</th>
       <th>Nom</th>
       <th>prenom</th>
       <th>tel</th>
        <th>e-mail</th>
         <th>adresse</th>
   </tr>"""
fintable="""</table> """
#-----------------------------------------------------------------
#--------------programme principal --------------------
print(htmld)
print(f""" nombre de personne dans la location :{nbr_perso}<br>""")
print(f"""<input  name="nbr_perso" type="hidden" value="{nbr_perso}">""") #je te expliquerai plus tard s

print(f"""type de la location : {typee} <br>""")
print(f"""<input  name="typee" type="hidden" value="{typee}">""")#je te expliquerai plus tard s

print(f""" nom du groupe :{nom_groupe}<br>""")
print(f"""<input  name="nom_groupe" type="hidden" value="{nom_groupe}">""") #je te expliquerai plus tard s

print(f"""duree du sejour: {duree} <br>""")

print(f"""date du debut: {dated} <br>""")
print(f"""<input  name="dated" type="hidden" value="{dated}">""")#je te expliquerai plus tard s
print(f"""date de fin  : {datef} <br>""")
print(f"""<input  name="datef" type="hidden" value="{datef}">""")#je te expliquerai plus tard s

print(f"""demi pension : {demi_pension} <br>""")
print(f"""<input  name="demi_pension" type="hidden" value="{demi_pension}">""")#je te expliquerai plus tard s
i=1
while(i<=nbr_perso):# creation du tableau 
    if i==1:
        table=table+responsable
    if i==2:
        table=table+inscription1
    if i==3:
        table=table+inscription2
    if i==4:
        table=table+inscription3
    if i==5:
        table=table+inscription4
    if i==6:
        table=table+inscription5
    if i==7:
        table=table+inscription6
    if i==8:
        table=table+inscription7
    i=i+1
table=table+fintable

print(table)
print(htmlf)


