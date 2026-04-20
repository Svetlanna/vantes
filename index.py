import pandas as pd
import plotly.express as px  # dessiner les graphiques

#DONNÉES avec les Régions
data = {
    'produit': ['Produit A', 'Produit B', 'Produit C'],
    'quantite_vendue': [325, 125, 80],
    'chiffre_affaires': [3250, 1875, 1600],

    'region': ['Nord', 'Sud', 'Est'],
    'ca_region': [2100, 2800, 1825]  # Chiffre d'Affaires par région
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
                   hole=0.3)  # Mode "Donut"

figure_region = px.bar(df,
                       x='region',
                       y='ca_region',
                       title="Chiffre d'Affaires par Région (€)",
                       labels={'ca_region': 'Chiffre d\'Affaires (€)', 'region': 'Région'},
                       color='region',
                       template='plotly_dark')


with open('analyses_ventes.html', 'a') as f:
    f.write(figure_ventes.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figure_ca.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figure_region.to_html(full_html=False, include_plotlyjs='cdn'))

print('analyses_ventes.html généré avec succès !')



# affichage
figure_ventes.show()
figure_ca.show()
figure_region.show()
