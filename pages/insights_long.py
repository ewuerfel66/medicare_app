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
            The figure below shows how your diagnosis and state combine to influence prices. This plot is encoded, but you can check the diagnosis and state using the key to the right:
            
            From the plot, we can see that Orthopedics (column 6) is consistently the most expensive while Respiratory issues (column 3) are consistently the least expensive.

            """
        ),
        html.Img(src='assets/pdp_interact.png', className='img-fluid')
    ],
    md=4,
)

column3 = dbc.Col(
    [
        dcc.Markdown(
            """
            
        ## Diagnosis
            
        * Neurological    1
        * Other           2
        * Respiratory     3
        * Circulatory     4
        * Digestive       5
        * Orthopedic      6
        
        ## State

        * AL      1
        * AK      2
        * AZ      3
        * AR      4
        * CA      5
        * CO      6
        * CT      7
        * DE      8
        * DC      9
        * FL     10
        * GA     11
        * HI     12
        * ID     13
        * IL     14
        * IN     15
        * IA     16
        * KS     17
        * KY     18
        * LA     19
        * ME     20
        * MD     21
        * MA     22
        * MI     23
        * MN     24
        * MS     25
        * MO     26
        * MT     27
        * NE     28
        * NV     29
        * NH     30
        * NJ     31
        * NM     32
        * NY     33
        * NC     34
        * ND     35
        * OH     36
        * OK     37
        * OR     38
        * PA     39
        * RI     40
        * SC     41
        * SD     42
        * TN     43
        * TX     44
        * UT     45
        * VT     46
        * VA     47
        * WA     48
        * WV     49
        * WI     50
        * WY     51
        * NaN    52

            """
        )
    ]
)

layout = dbc.Row([column1, column3])