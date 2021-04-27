#https://austinlasseter.medium.com/how-to-deploy-a-simple-plotly-dash-app-to-heroku-622a2216eb73
#https://towardsdatascience.com/deploying-your-dash-app-to-heroku-the-magical-guide-39bd6a0c586c
#https://www.youtube.com/watch?v=b-M2KQ6_bM4
#https://blog.heroku.com/from-project-to-productionized-python
#https://community.plotly.com/t/deploying-your-dash-app-to-heroku-the-magical-guide/46723


import dash
import dash_core_components as dcc
import dash_html_components as html


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(children=[
    html.H1(children='IST Energy Monitor - Dashboard 2'),

html.Div(children='''
        Visualization of total electricity consumption at IST over the last years
    '''),

    dcc.Graph(
        id='yearly-data',
        figure={
            'data': [
                {'x': [2017, 2018, 2019], 'y': [9709, 10000, 0], 'type': 'bar', 'name': 'Total'},
                {'x': [2017, 2018, 2019], 'y': [1440, 1605, 0], 'type': 'bar', 'name': 'Civil'},
                {'x': [2017, 2018, 2019], 'y': [1658, 1598, 0], 'type': 'bar', 'name': 'Central'},
                {'x': [2017, 2018, 2019], 'y': [898, 1002, 0], 'type': 'bar', 'name': 'North Tower'},
                {'x': [2017, 2018, 2019], 'y': [1555, 1523, 0], 'type': 'bar', 'name': 'South Tower'},
            ],
            'layout': {
                'title': 'IST yearly electricity consumption (kWh)'
            }
        }
    ),



])

if __name__ == '__main__':
    app.run_server(debug=False)
