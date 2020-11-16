# coding: utf-8
#1 er page de reservation 
# les date ne sont pas configure pour le moment 
print("Content-type: text/html; charset=utf-8\n")


html = """<!DOCTYPE html>
<html>
<body>

<form action="reservation2.py" method="post">
    nombre de personne dans la location : <input type="text" name="nbr_personne"value="1"/><br>
    type de la location :
    <select name="type">
        <option value="tante">tante</option>
        <option value="caravane">caravane</option>
        <option value="mobilehom6">mobilehome 6 personne</option>
        <option value="mobilehome8">mobilehome 8 personne</option>
    </select><br>
    duree du sejour  : <input type="text" name="duree"value="1"/> <br>
    date de debut: <input type="date"  name="dated"><br>
    date de fin:
    <input type="date"  name="datef"><br>

    nom du groupe (ayez de imagination): <input type="text" name="nom_groupe"value="spiderman"/><br>
    demi pension? <input type="text" name="demi_pension"value="oui"/><br>   
            <input type="submit" value="valider" />
</form>"""
html1="""
    <form action="information.py" method="post">
      <input  type="submit" value="information sur le camping" />
    </form>
</body>
</html>
"""

print(html)
print(html1)

