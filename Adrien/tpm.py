import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Ma Liste Déroulante Dash'),
    dcc.Dropdown(
        id='ma-liste-deroulante',
        options=[
            {'label': 'Option 1', 'value': 'opt1'},
            {'label': 'Option 2', 'value': 'opt2'},
            {'label': 'Option 3', 'value': 'opt3'}
        ],
        value='None'  # Valeur par défaut sélectionnée dans la liste déroulante
    ),
    html.Div(id='output-liste-deroulante')  # Div pour afficher le résultat
])


@app.callback(
    Output('output-liste-deroulante', 'children'),
    [Input('ma-liste-deroulante', 'value')]
)
def mettre_a_jour_output(valeur_selectionnee):
    return f"Vous avez sélectionné l'option : {valeur_selectionnee}"



if __name__ == '__main__':
    app.run_server(debug=True)