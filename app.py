import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv('data_class15.csv')

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


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Table', value='tab-1'),
        dcc.Tab(label='Graph', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))

def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('IST Energy yearly Consumption (kWh)'),
            generate_table(df)
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('IST Energy Yearly Consumption (kWh)'),
            dcc.Graph(
                id='yearly-data',
                figure={
                    'data': [
                        {'x': df.year, 'y': df.Total, 'type': 'bar', 'name': 'Total'},
                        {'x': df.year, 'y': df.Civil, 'type': 'bar', 'name': 'Civil'},
                        {'x': df.year, 'y': df.Central, 'type': 'bar', 'name': 'Central'},
                        {'x': df.year, 'y': df.NorthTower, 'type': 'bar', 'name': 'North Tower'},
                        {'x': df.year, 'y': df.SouthTower, 'type': 'bar', 'name': 'South Tower'},
                    ],
                    'layout': {
                        'title': 'IST yearly electricity consumption (MWh)'
                    }
                }
            ),
        ])


if __name__ == '__main__':
    app.run_server(debug=False)
