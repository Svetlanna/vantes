import pandas as pd
import plotly.express as px

#les noms que je veux donner à mes colonnes.
noms_colonnes = ['date', 'produit', 'prix', 'qte', 'region']
df = pd.read_csv('ventes.csv', names=noms_colonnes, skiprows=1)

#
df['qte'] = pd.to_numeric(df['qte'], errors='coerce')
df['prix'] = pd.to_numeric(df['prix'], errors='coerce')
df['CA'] = df['prix'] * df['qte'] # Calcul du chiffre d'affaires




figure_ventes = px.bar(df,
                    x='produit',
                    y='qte',
                    title="Nombre total de ventes par produit",
                    labels={'qte': 'Quantité Totale', 'produit': 'Nom du Produit'},
                    color='produit')


figure_ca = px.pie(df,
                values='CA',
                names='produit',
                title="Répartition du Chiffre d'Affaires par produit",
                hole=0.3)


figure_region = px.pie(df,
                values='qte',
                names='region',
                title='Quantité vendue par région')


with open('analyses_ventes.html', 'w') as f:
    f.write("<h1>Rapport d'Analyse des Ventes</h1>")
    f.write(figure_ventes.to_html(full_html=False, include_plotlyjs='cdn'))



with open('analyses_ventes.html', 'a') as f:
    f.write(figure_ca.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figure_region.to_html(full_html=False, include_plotlyjs='cdn'))

print("le fichier 'analyses_ventes.html' a été vidé et mis à jour avec les 3 graphiques.")

#affichage
figure_ventes.show()
figure_ca.show()
figure_region.show()