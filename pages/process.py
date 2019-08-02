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
            
            This web app uses a random forest regressor to estimate out-of-pocket medical costs based on [Medicare Payment Data](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient.html).
            
            Consumers often have no clue how much a diagnosis or procedure could end up costing them beforehand. The complicated nature of the human body usually means that doctors don't even have a clue how much it might end up costing you. This uncertainty and lack of transparency is just one of the reasons our health care costs in the United States are so high (about 17% of our GDP compared with the average of about 10-12%).
            
            This tool takes in a category of medical diagnosis and your health care provider's state, then returns an estimate of the out-of-pocket costs one would expect with Medicare coverage. 
            
            To create this, I sorted the top 100 most common diagnoses and procedures into the general categories:
                * Cardiac/Circulatory
                * Cranial/Neurological
                * Digestive
                * Orthopedic
                * Respiratory
                * Other

            These categories were tuned to be general enough so that one could reasonably guess which category your diagnosis might fall into without a doctor's opinion, yet detailed enough to capture the wide variance among out-of-pocket costs.
            
            Out-of-pocket costs can be found by subtracting medicare coverage from net price for each diagnosis. Using the category of diagnosis and the provider's state, I trained a random forest regressor to predict the out-of-pocket costs.
            
            Due to the simplicity of the inputs, this model has a mean absolute error of about $680. So take these estimates with a grain of salt. This tool does well to get you in the ballpark of what you might expect to pay. Models trained with uncategorized diagnoses (assumes the consumer knows their exact diagnosis) only reduced mean absolute error to about $630, so we didn't lose much resolution by categorizing the diagnoses.
            
            There's a remarkable lack of transparency in the health care system, which is further confounded by the inherent uncertainty in the nature of medicine. Hopefully this tool can provide a bit more information to Medicare beneficiaries about their expected costs.
            
            """
        ),

    ],
)

layout = dbc.Row([column1])