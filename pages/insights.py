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
            
            The color of each box represents what medicare beneficiaries can expect to pay out-of-pocket for a given diagnosis in a given state. From the plot, we can see that Orthopedics (column 6) is consistently the most expensive while Respiratory issues (column 3) are consistently the least expensive.
            
            Rows 9, 12 and 45 correspond to DC, Hawaii, and Utah. These are a few of the brightest rows in our plot, indicating that the model predicted higher expenses for these states. 
            
            The most expensive prediction was for an Orthopedic diagnosis in Hawaii at $3426.66, while the least expensive prediction was for a respiratory issue in Mississippi at $1035.20.
            
            The single-feature PDP gives us a closer look at how one's diagnosis alone influences your out-of-pocket costs.
            
            The minimum at 3 (Respiratory) and maximum at 6 (Orthopedic) confirm our suspicion that Respiratory issues are the least expensive while Orthopedic issues are the most expensive. Surprisingly, Neurological (1) diagnoses didn't come with a considerably higher price than average, while Circulatory (4) and Digestive (5) were slightly expensive.
            
            ## Key
            
            ### Diagnosis
            
            * Neurological:1
            * Other:2
            * Respiratory:3
            * Circulatory:4
            * Digestive:5
            * Orthopedic:6
            
            ## State

            * AL:1
            * AK:2
            * AZ:3
            * AR:4
            * CA:5
            * CO:6
            * CT:7
            * DE:8
            * DC:9
            * FL:10
            * GA:11
            * HI:12
            * ID:13
            * IL:14
            * IN:15
            * IA:16
            * KS:17
            * KY:18
            * LA:19
            * ME:20
            * MD:21
            * MA:22
            * MI:23
            * MN:24
            * MS:25
            * MO:26
            * MT:27
            * NE:28
            * NV:29
            * NH:30
            * NJ:31
            * NM:32
            * NY:33
            * NC:34
            * ND:35
            * OH:36
            * OK:37
            * OR:38
            * PA:39
            * RI:40
            * SC:41
            * SD:42
            * TN:43
            * TX:44
            * UT:45
            * VT:46
            * VA:47
            * WA:48
            * WV:49
            * WI:50
            * WY:51


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