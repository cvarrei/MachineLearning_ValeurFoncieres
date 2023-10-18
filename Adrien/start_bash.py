from dash import Dash, html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from Prediction import preproc, pred

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Mon Tableau de Bord Dash'),
    html.Label('Nombre de lot'),# Titre des inputs
    dcc.Input(id='nlot', type='number', value=0),
    html.Label('Type local :'),
    dcc.Input(id='tl', type='text', value="maison" , placeholder='Entrez votre texte ici...'),# Champ de saisie numérique
    html.Label('surface reele bati'),
    dcc.Input(id='sr', type='number', value=0),
    html.Label('Nombre de pieces principales :'),
    dcc.Input(id='nbpp', type='number', value=0),
    html.Label('Surface terrain :'),
    dcc.Input(id='st', type='number', value=0),
    html.Label("Presence d'un terrain exterieur (y/n) :"),
    dcc.Input(id='te', type='text', value="n" , placeholder='Entrez votre texte ici...'),# Champ de saisie numérique
    html.Label('Années :'),
    dcc.Input(id='year', type='number', value=0),
    html.Label('Mois :'),
    dcc.Input(id='month', type='number', value=0),
    html.Label("Nom de la region :"),
    dcc.Input(id='nom_region', type='text', value="n" , placeholder='Entrez votre texte ici...'),# Champ de saisie numérique
    html.Button('Lancement de la prediction', id='mon-bouton'),
    html.Div(id='output-texte')  # Div pour afficher le résultat
])

@app.callback(
    Output('output-texte', 'children'),
    [Input('nlot', 'value'),
     Input('tl', 'value'),
     Input('sr', 'value'),
     Input('nbpp', 'value'),
     Input('st', 'value'),
     Input('te', 'value'),
     Input('year', 'value'),
     Input('month', 'value'),
     Input('nom_region', 'value')]
)

def mettre_a_jour_output(nlot,tl,sr,nbpp,st,te,year,month,nom_region):
    x=0

    res = f"Le cout du bien sera de:  {r} euros"
    return resultat

if __name__ == '__main__':
    app.run(debug=True)


