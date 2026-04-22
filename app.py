import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.bar(données, x = "produit", y = "qte")

figure.write_html('ventes-par-produit.html')

print('ventes-par-produit.html généré avec succès !')

# Pas reussis exercice 6.b -> fais avec l'aide de claude pour comprendre 

données['CA'] = données['prix'] * données['qte']
figure = px.bar(
    données, 
    x='produit',                   
    y='CA',                         
    title='Chiffre d\'affaires par produit',
    labels={'CA': 'CA (€)', 'produit': 'Produit'},
    color='CA')    
    
figure.write_html('ca-par-produit.html')
print('ca-par-produit.html généré avec succès !')



données_grouped = données.groupby('produit')['CA'].sum().reset_index()
figure = px.pie(données_grouped, values='CA', names='produit', 
                title='Répartition du CA par produit')

figure.write_html('ca-pie-chart.html')