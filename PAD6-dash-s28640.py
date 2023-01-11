from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly_express as px
from dash.exceptions import PreventUpdate

app = Dash(__name__)


df = pd.read_csv("/Users/maciejbunkowski/Library/CloudStorage/OneDrive-Polsko-JapońskaAkademiaTechnikKomputerowych/STUDIA/PJATK/I SEMESTR/Programowanie dla Analityki Danych/winequelity.csv").drop(['Unnamed: 0'],axis=1)

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


all_options = {
    'Regresja Liniowa': list(df.columns),
    'Klasyfikacja': list(df.columns)
}

@app.callback(
    Output('my-graph', 'figure'),
    Input('type-radio', 'value'),
    Input('variable-radio', 'value'))
def set_display_children(selected_type, selected_variable):
    if selected_variable is None:
        raise PreventUpdate()
    elif selected_type == "Regresja Liniowa":
        return px.scatter(df, x=df[f"{selected_variable}"], y="pH", title=f"pH in relation to {selected_variable}")
    else:
        return px.box(df, x="target", y=df[f"{selected_variable}"], color="target", title=f"Type of wine in relation to {selected_variable}", 
        color_discrete_map={"red": "red", "white": "green"},)

app.layout = html.Div(children=[ 
    html.H4(
    children='Wine Quality Data'),
    generate_table(df),

    dcc.RadioItems(list(all_options.keys()),
        id='type-radio',
    ),

    dcc.RadioItems(list(all_options.values())[0],
        id='variable-radio'),
        
    html.Div(id='display-selected-values'),
    dcc.Graph(id='my-graph', figure={}
              )
        ])  
    
if __name__ == '__main__':
    app.run_server(debug=True)