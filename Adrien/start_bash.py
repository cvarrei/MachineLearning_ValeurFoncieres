from dash import Dash, html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Mon Tableau de Bord Dash'),
    html.Label('Valeur 1 :'),# Titre des inputs
    dcc.Input(id='input-valeur-1', type='number', value=0),
    html.Label('Valeur 2 :'),

    dcc.Input(id='input-valeur-2', type='number', value=0),  # Champ de saisie numérique
    html.Button('Lancement de la prediction', id='mon-bouton'),
    html.Div(id='output-texte')  # Div pour afficher le résultat
])

@app.callback(
    Output('output-texte', 'children'),
    [Input('input-valeur-1', 'value'),
     Input('input-valeur-2', 'value'),
     Input('mon-bouton', 'n_clicks')]
)

def mettre_a_jour_output(valeur1,valeur2,n_clicks):
    x=0
    if(n_clicks!=x):
    # Logique pour traiter la valeur saisie (valeur_saisie) ici
        res = f"La valeur que vous avez saisie est : {valeur1+valeur2}"
        x=n_clicks
        resultat=res
    return resultat

if __name__ == '__main__':
    app.run(debug=True)


