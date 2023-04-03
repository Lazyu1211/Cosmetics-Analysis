from dash import Dash,html,dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from utill import get_data

def render(app):
    df = get_data()
    fig = px.scatter(
            df, 
            x="Price", 
            y="Rank",
            title="Rank with Price",
            color="Price"
            )
    return html.Div(dcc.Graph(figure=fig), id="scatter")