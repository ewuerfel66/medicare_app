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
            The two-feature Partial Dependence Plot (PDP) to the right shows how your diagnosis and state combine to influence prices.
            
            The color of each box represents the expected cost for a given diagnosis in a given state. From the plot, we can see that Orthopedics (column 6) is consistently the most expensive while Respiratory issues (column 3) are consistently the least expensive.
            
            Rows 9, 12 and 45 correspond to DC, Hawaii, and Utah. These are a few of the brightest rows in our plot, indicating that the model predicted higher expenses for these states.
            
            The most expensive prediction was for an Orthopedic diagnosis in Hawaii, while the least expensive prediction was for a respiratory issue in Mississippi.
            
            The single-feature PDP gives us a closer look at how one's diagnosis alone influences your out-of-pocket costs.
            
            The minimum at 3 (Respiratory) and maximum at 6 (Orthopedic) confirm our suspicion that Respiratory issues are the least expensive while Orthopedic issues are the most expensive. Surprisingly, Neurological (1) diagnoses didn't come with a considerably higher price than average, while Circulatory (4) and Digestive (5) were slightly expensive.

            """
        )
    ],
    md=4,
)

column3 = dbc.Col(
    [
        html.Img(src='assets/pdp_interact.png', className='img-fluid'),
        html.Img(src='assets/diagnosis_pdp.png', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column3])