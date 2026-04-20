<<<<<<< HEAD
import pandas as pd
import plotly.express as px#dessiner les graphiques
data = {
    'produit': ['Produit A', 'Produit B', 'Produit C'],
    'quantite_vendue': [325, 125, 80],
    'chiffre_affaires': [3250, 1875, 1600]
}

df = pd.DataFrame(data)
figure_ventes = px.bar(df,
=======
import pandas as pd #Pandas pour  manipuler les données comme dans un tableau Excel
import plotly.express as px #Plotly pour  dessiner les graphiques.

#Ce sont les résultats que j'ai récupérés grâce à mes requêtes SQL
data = {
    'produit': ['Produit A', 'Produit B', 'Produit C'],
    'quantite_vendue': [325, 125, 80],  # Chiffres exemples (à vérifier avec  SQL)
    'chiffre_affaires': [3250, 1875, 1600] # Calcul : Prix * Quantité
}

#La commande pd.DataFrame transforme ces chiffres en un tableau
# que Python peut analyser
df = pd.DataFrame(data) #pour transformer ces données en un tableau structuré pour Python

#Tâche 6.a /Graphique 1 (Ventes par produit)
# px.bar pour créer un diagramme en barres.
#Cela permet de comparer visuellement les quantités vendues pour chaque produit.
fig_ventes = px.bar(df,
>>>>>>> 52000c87373d44f8dac0b52d6115fdfa9b9349af
                    x='produit',
                    y='quantite_vendue',
                    title="Nombre total de ventes par produit",
                    labels={'quantite_vendue': 'Quantité Totale', 'produit': 'Nom du Produit'},
                    color='produit')

<<<<<<< HEAD

figure_ca = px.pie(df,
                values='chiffre_affaires',
                names='produit',
                title="Répartition du Chiffre d'Affaires par produit",
                hole=0.3)


figure_ventes.show()
figure_ca.show()
=======
#Tâche 6.b / Graphique 2 (CA par produit)
#px.pie (un graphique en secteurs). Cela permet de voir la part
# de chaque produit dans le Chiffre d'Affaires total.
# C'est très utile pour voir quel produit rapporte le plus d'argent.
fig_ca = px.pie(df,
                values='chiffre_affaires',
                names='produit',
                title="Répartition du Chiffre d'Affaires par produit",
                hole=0.3) # Pour faire un graphique en "Donut" (plus moderne)

# Affichage
#la commande .show() permet d'ouvrir mon navigateur pour afficher
# les graphiques de manière interactive
fig_ventes.show()
fig_ca.show()
>>>>>>> 52000c87373d44f8dac0b52d6115fdfa9b9349af
