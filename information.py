#coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=unicode\n")


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


<body>

<center> 
    information:<br>
    bonjour,a tout nos futur client <br>
    dans notre camping nous possedons plusieur type emplacement qui sont :<br>
    -emplacement tante jusqua 6 place<br>
    -emplacement caravane/campingcar  6 place <br>
    -emplacement de mobile home de 6 et 8 place <br>
    des chalet vont bientot voir le jour dans notre camping soyez patient!!!!! <br>

    prix par  emplcament pour les location:<br>
    <table>
    <tr>
    <th>EMPLACEMENT</th>
    <th>jour</th>
    <th>semaine</th>
    <th>mois</th>
    </tr>  
    <tr>
    <th>tante</th>
    <th>10</th>
    <th>60</th>
    <th>100</th>
    </tr>  
    <tr>
    <th>caravane/campingcar</th>
    <th>20</th>
    <th>120</th>
    <th>450</th>
    </tr>  
    <th>mobile home 6 personne </th>
    <th>50</th>
    <th>300</th>
    <th>800</th>
    </tr>  
    <th>mobilehome 8 personne</th>
    <th>75</th>
    <th>500</th>
    <th>1800</th>
    </tr>  
    </table><p>
    une option demi-pension est disponbile!<br>
    cela vous offre un repas chaque soir au restaurant <br>

    si vous reservé a la semaine il y aura 10 pourcent de remise <br>
    et si vous prenez le mois 20 pourcent de remise <br> 
    une offre a pas manque<br>

    si vous apporté des voiture il y a un prix de 20 euro par voiture <br>
    les vélo quand a eux sont gratuit <br></p>  
<form action="index.py" method="post">
<input  type="submit" value="retour" />
</form>
</center> 
</body>
</html>
"""

print(html)