import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            The figure below shows how your diagnosis and state combine to influence prices.
            
            From the plot, we can see that Orthopedics (column 6) is consistently the most expensive while Respiratory issues (column 3) are consistently the least expensive.

            """
        )
    ],
    md=4,
)

column3 = dbc.Col(
    [
        html.Img(src='assets/pdp_interact.png', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column3])