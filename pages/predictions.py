import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

from joblib import load
pipeline = load('assets/medicare.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown("## Inputs"),
        dcc.Markdown("#### Medical Problem"),
        dcc.Dropdown(
            id = 'diagnosis',
            options = [
                {'label':'Cardiac/Circulatory', 'value':'Circulatory'},
                {'label':'Cranial/Neurological', 'value':'Neurological'},
                {'label':'Digestive', 'value':'Digestive'},
                {'label':'Orthopedic', 'value':'Orthopedic'},
                {'label':'Respiratory', 'value':'Respiratory'},
                {'label':'Other', 'value':'Other'}
            ],
            value = 'Digestive'
        ),
        dcc.Markdown("#### State"),
        dcc.Dropdown(
            id='state',
            options = [
                {'label':'AL', 'value':'AL'},
                {'label':'AK', 'value':'AK'},
                {'label':'AZ', 'value':'AZ'},
                {'label':'AR', 'value':'AR'},
                {'label':'CA', 'value':'CA'},
                {'label':'CO', 'value':'CO'},
                {'label':'CT', 'value':'CT'},
                {'label':'DC', 'value':'DC'},
                {'label':'DE', 'value':'DE'},
                {'label':'FL', 'value':'FL'},
                {'label':'GA', 'value':'GA'},
                {'label':'HI', 'value':'HI'},
                {'label':'ID', 'value':'ID'},
                {'label':'IL', 'value':'IL'},
                {'label':'IN', 'value':'IN'},
                {'label':'IA', 'value':'IA'},
                {'label':'KS', 'value':'KS'},
                {'label':'KY', 'value':'KY'},
                {'label':'LA', 'value':'LA'},
                {'label':'ME', 'value':'ME'},
                {'label':'MD', 'value':'MD'},
                {'label':'MA', 'value':'MA'},
                {'label':'MI', 'value':'MI'},
                {'label':'MN', 'value':'MN'},
                {'label':'MS', 'value':'MS'},
                {'label':'MO', 'value':'MO'},
                {'label':'MT', 'value':'MT'},
                {'label':'NE', 'value':'NE'},
                {'label':'NV', 'value':'NV'},
                {'label':'NH', 'value':'NH'},
                {'label':'NJ', 'value':'NJ'},
                {'label':'NM', 'value':'NM'},
                {'label':'NY', 'value':'NY'},
                {'label':'NC', 'value':'NC'},
                {'label':'ND', 'value':'ND'},
                {'label':'OH', 'value':'OH'},
                {'label':'OK', 'value':'OK'},
                {'label':'OR', 'value':'OR'},
                {'label':'PA', 'value':'PA'},
                {'label':'RI', 'value':'RI'},
                {'label':'SC', 'value':'SC'},
                {'label':'SD', 'value':'SD'},
                {'label':'TN', 'value':'TN'},
                {'label':'TX', 'value':'TX'},
                {'label':'UT', 'value':'UT'},
                {'label':'VT', 'value':'VT'},
                {'label':'VA', 'value':'VA'},
                {'label':'WA', 'value':'WA'},
                {'label':'WV', 'value':'WV'},
                {'label':'WI', 'value':'WI'},
                {'label':'WY', 'value':'WY'},
            ],    
            value = 'AL'
        )
    ],
)

column2 = dbc.Col(
    [
        html.H2('Expected out-of-pocket Cost'),
        html.Div(id='prediction-content', className='lead')
    ]
)

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('diagnosis', 'value'), Input('state', 'value')],
)
def predict(diagnosis, state):
    df = pd.DataFrame(
        columns=['diagnosis', 'state'], 
        data=[[diagnosis, state]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'${y_pred:.0f}'

layout = dbc.Row([column1, column2])