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
        
            ## Process
            
            This web app uses a random forest regressor to estimate out-of-pocket medical costs based on [Medicare Payment Data](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient.html). I hope that this creates a little more transparency in the health care market.
            
            Consumers often have no clue how much a diagnosis or procedure could end up costing them beforehand. The complicated nature of the human body usually means that doctors don't even have a clue how much it might end up costing you. This uncertainty and lack of transparency is just one of the reasons our health care costs in the United States is so high (about 17% of our GDP compared with the average of about 10-12%).
            
            I sorted the top 100 most common diagnoses and procedures into categories that most consumers can understand:
                * Cardiac/Circulatory
                * Cranial/Neurological
                * Digestive
                * Orthopedic
                * Respiratory
                * Other

            """
        ),

    ],
)

layout = dbc.Row([column1])