# coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=utf-8\n")


html = """<!DOCTYPE html>
<html>
  <head>
    <style>
      body 
      {color: yellow; 
        background-image: url('https://www.lapascalinette.fr/wp-content/uploads/2018/07/parc-aquatique-du-camping-de-la-pascalinette.jpg');
        background-repeat: no-repeat;
        background-attachment: fixed;  
        background-size: cover;
      }
    </style>
  </head>
<body>
  <center>
  <h1>camping les flots </h1> 
    <form action="connexion.py" method="post">
      <input  type="submit" value="connexion" />
    </form>
    <form action="information.py" method="post">
      <input  type="submit" value="information sur le camping" />
    </form>
      <form action="inscription.py" method="post">
      <input  type="submit" value="inscription pour etre responsable " />
    </form>
    <form action="statistique.py" method="post">
      <input  type="submit" name="valeur" value="statistique du camping  " />
    </form>
  </center> 
</body>
</html>
"""

print(html)