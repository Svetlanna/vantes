import pandas as pd
import plotly.express as px#dessiner les graphiques
data = {
    'produit': ['Produit A', 'Produit B', 'Produit C'],
    'quantite_vendue': [325, 125, 80],
    'chiffre_affaires': [3250, 1875, 1600]
}

df = pd.DataFrame(data)
figure_ventes = px.bar(df,
                    x='produit',
                    y='quantite_vendue',
                    title="Nombre total de ventes par produit",
                    labels={'quantite_vendue': 'Quantité Totale', 'produit': 'Nom du Produit'},
                    color='produit')


figure_ca = px.pie(df,
                values='chiffre_affaires',
                names='produit',
                title="Répartition du Chiffre d'Affaires par produit",
                hole=0.3)


figure_ventes.show()
figure_ca.show()