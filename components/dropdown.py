from dash import Dash, html, dcc
from dash.dependencies import Output,Input
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_brand_list, get_price_list, get_treat_list, get_Moisturizer_list, get_Eyecream_list, get_Sunprotect_list, get_FaceMask_list, get_Cleanser_list

def render(app):
    list_brand = get_brand_list()
    top10_brand = [{'label':i,'value':i} for i in list_brand]
    @app.callback(
    Output(component_id='brand_dropdown', component_property='value'),
    Input(component_id='select_all_button', component_property='n_clicks')
    )
    def update_top10_brand(n):
        return list_brand

    return html.Div(
        children=[
            html.H6("Select A Brand"),
            dcc.Dropdown(
                options=top10_brand,
                multi=True,
                id = "brand_dropdown"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button",
                n_clicks=0
            )
        ]
    )

def render1(app):
    list_brand_price = get_price_list()
    top10_brand = [{'label':i,'value':i} for i in list_brand_price]
    @app.callback(
    Output(component_id='price_dropdown', component_property='value'),
    Input(component_id='select_all_button1', component_property='n_clicks')
    )
    def update_top10_brand(n):
        return list_brand_price

    return html.Div(
        children=[
            html.H6("Select A Brand"),
            dcc.Dropdown(
                options=top10_brand,
                multi=True,
                id = "price_dropdown"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button1",
                n_clicks=0
            )
        ]
    )

def render2(app):
    list_treat = get_treat_list()
    top10_brand = [{'label':i,'value':i} for i in list_treat]
    @app.callback(
    Output(component_id='treat_dropdown', component_property='value'),
    Input(component_id='select_all_button2', component_property='n_clicks')
    )
    def update_top10_brand(n):
        return list_treat

    return html.Div(
        children=[
            html.H6("Select A Brand"),
            dcc.Dropdown(
                options=top10_brand,
                multi=True,
                id = "treat_dropdown"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button2",
                n_clicks=0
            )
        ]
    )

def render3(app):
    list_moi = get_Moisturizer_list()
    top10_brand = [{'label':i,'value':i} for i in list_moi]
    @app.callback(
    Output(component_id='moi_dropdown', component_property='value'),
    Input(component_id='select_all_button3', component_property='n_clicks')
    )
    def update_top10_brand(n):
        return list_moi

    return html.Div(
        children=[
            html.H6("Select A Brand"),
            dcc.Dropdown(
                options=top10_brand,
                multi=True,
                id = "moi_dropdown"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button3",
                n_clicks=0
            )
        ]
    )

def render4(app):
    list_eye = get_Eyecream_list()
    top10_brand = [{'label':i,'value':i} for i in list_eye]
    @app.callback(
    Output(component_id='eye_dropdown', component_property='value'),
    Input(component_id='select_all_button4', component_property='n_clicks')
    )
    def update_top10_brand(n):
        return list_eye

    return html.Div(
        children=[
            html.H6("Select A Brand"),
            dcc.Dropdown(
                options=top10_brand,
                multi=True,
                id = "eye_dropdown"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button4",
                n_clicks=0
            )
        ]
    )

def render5(app):
    list_sun = get_Sunprotect_list()
    top10_brand = [{'label':i,'value':i} for i in list_sun]
    @app.callback(
    Output(component_id='sun_dropdown', component_property='value'),
    Input(component_id='select_all_button5', component_property='n_clicks')
    )
    def update_top10_brand(n):
        return list_sun

    return html.Div(
        children=[
            html.H6("Select A Brand"),
            dcc.Dropdown(
                options=top10_brand,
                multi=True,
                id = "sun_dropdown"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button5",
                n_clicks=0
            )
        ]
    )

def render6(app):
    list_face = get_FaceMask_list()
    top10_brand = [{'label':i,'value':i} for i in list_face]
    @app.callback(
    Output(component_id='face_dropdown', component_property='value'),
    Input(component_id='select_all_button6', component_property='n_clicks')
    )
    def update_top10_brand(n):
        return list_face

    return html.Div(
        children=[
            html.H6("Select A Brand"),
            dcc.Dropdown(
                options=top10_brand,
                multi=True,
                id = "face_dropdown"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button6",
                n_clicks=0
            )
        ]
    )

def render7(app):
    list_cle = get_Cleanser_list()
    top10_brand = [{'label':i,'value':i} for i in list_cle]
    @app.callback(
    Output(component_id='cle_dropdown', component_property='value'),
    Input(component_id='select_all_button7', component_property='n_clicks')
    )
    def update_top10_brand(n):
        return list_cle

    return html.Div(
        children=[
            html.H6("Select A Brand"),
            dcc.Dropdown(
                options=top10_brand,
                multi=True,
                id = "cle_dropdown"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button7",
                n_clicks=0
            )
        ]
    )