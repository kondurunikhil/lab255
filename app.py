from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div(children=[
    html.Div([
    html.H4('population plot with respect to country with adjustable axis'),
    html.Button("Switch Axis", n_clicks=0, 
                id='button'),
    dcc.Graph(id="graph"),
]),
html.Div([
    html.H4('Case percentage with respect to country in bar graph'),
    html.Button("Switch Axis", n_clicks=0, 
                id='newButton'),
    dcc.Graph(id="newGraph"),
]),
html.Div([
    html.H4('Number of confirmed cases with respect to country with Scatter plot'),
    html.Button("Switch Axis", n_clicks=0, 
                id='newScatterButton'),
    dcc.Graph(id="newGraphScatter"),
])
])

@app.callback(
    Output("graph", "figure"), 
    Input("button", "n_clicks"))
def display_graph(n_clicks):
    df = pd.read_csv('./dataset.csv') # replace with your own data source

    if n_clicks % 2 == 0:
        x, y = 'country', 'year_2018'
    else:
        x, y = 'year_2018', 'country'

    fig = px.line(df, x=x, y=y)    
    return fig

@app.callback(
    Output("newGraph", "figure"), 
    Input("newButton", "n_clicks"))
def display_graph(n_clicks):
    df2 = pd.read_csv('./Case_percent_demo_info.csv') # replace with your own data source

    if n_clicks % 2 == 0:
        x, y = 'country_name', 'case_percent'
    else:
        x, y = 'case_percent', 'country_name'

    fig = px.bar(df2, x=x, y=y)    
    return fig



@app.callback(
    Output("newGraphScatter", "figure"), 
    Input("newScatterButton", "n_clicks"))
def display_graph(n_clicks):
    df3 = pd.read_csv('./Case_percent_demo_info.csv') # replace with your own data source

    if n_clicks % 2 == 0:
        x, y = 'country_name', 'september_confirmed_cases'
    else:
        x, y = 'september_confirmed_cases', 'country_name'

    fig = px.scatter(df3, x=x, y=y)    
    return fig


app.run_server(debug=True)