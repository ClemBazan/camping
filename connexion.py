# coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=utf-8\n")


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
<body>
  <center>
  <h1>connexion camping les flots </h1> 
    <form action="compte.py" method="post">
    connexion:   <input type="texte" name="id_client" value="" /><br>
     code:    <input type="password" name="code" value="" /><br>
     <input  type="submit" value="valider " />
    </form>
    <form action="index.py" method="post">
<input  type="submit" value="retour" />
</form>
  </center> 
</body>
</html>
"""

print(html)