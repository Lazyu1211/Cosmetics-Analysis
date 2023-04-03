from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_brand, get_price, get_label, get_treat, get_Moisturizer, get_Eyecream, get_Sunprotect, get_FaceMask, get_Cleanser

def render(app):
    df = get_brand()

    @app.callback(
        Output("bar_volume","children"),
        Input("brand_dropdown","value")
    )
    def update_bar_chart(dropdown):
        filtered_data = df.query("Brand_Name in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div(
                dbc.Alert("No Brand selected", color="danger")
                ,id="bar_volume")
            
        fig = px.bar(
            filtered_data,
            x="Brand_Name", 
            y="Amount",
            orientation='v',
            color = "Brand_Name",
            title = "Top 10 Cosmetics Brands"
        )
        return html.Div(dcc.Graph(figure=fig) , id="bar_volume")
    return html.Div(id="bar_volume")

def render1(app):
    df = get_price()

    @app.callback(
        Output("bar_volume1","children"),
        Input("price_dropdown","value")
    )
    def update_bar_chart(dropdown):
        filtered_data = df.query("Brand_Name in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div(
                dbc.Alert("No Brand selected", color="danger")
                ,id="bar_volume1")
            
        fig = px.bar(
            filtered_data,
            x="Brand_Name", 
            y="Average_Price",
            orientation='v',
            color = "Brand_Name",
            title = "Top 10 Cosmetics Brands by Price"
        )
        return html.Div(dcc.Graph(figure=fig) , id="bar_volume1")
    return html.Div(id="bar_volume1")

def render2(app):
    df = get_label()
    fig = px.bar(
        df,
        x = "Label",
        y = "Price",
        color= "Label",
        title="Label with Average Price")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume2")

def render3(app):
    df = get_treat()

    @app.callback(
        Output("bar_volume3","children"),
        Input("treat_dropdown","value")
    )
    def update_bar_chart(dropdown):
        filtered_data = df.query("Brand in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div(
                dbc.Alert("No Brand selected", color="danger")
                ,id="bar_volume3")
            
        fig = px.bar(
            filtered_data,
            x="Brand", 
            y="Price",
            orientation='v',
            color = "Brand",
            title = "Top 10 Cosmetics Treatment Brands by Price"
        )
        return html.Div(dcc.Graph(figure=fig) , id="bar_volume3")
    return html.Div(id="bar_volume3")

def render4(app):
    df = get_Moisturizer()

    @app.callback(
        Output("bar_volume4","children"),
        Input("moi_dropdown","value")
    )
    def update_bar_chart(dropdown):
        filtered_data = df.query("Brand in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div(
                dbc.Alert("No Brand selected", color="danger")
                ,id="bar_volume4")
            
        fig = px.bar(
            filtered_data,
            x="Brand", 
            y="Price",
            orientation='v',
            color = "Brand",
            title = "Top 10 Cosmetics Moisturizer Brands by Price"
        )
        return html.Div(dcc.Graph(figure=fig) , id="bar_volume4")
    return html.Div(id="bar_volume4")

def render5(app):
    df = get_Eyecream()

    @app.callback(
        Output("bar_volume5","children"),
        Input("eye_dropdown","value")
    )
    def update_bar_chart(dropdown):
        filtered_data = df.query("Brand in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div(
                dbc.Alert("No Brand selected", color="danger")
                ,id="bar_volume5")
            
        fig = px.bar(
            filtered_data,
            x="Brand", 
            y="Price",
            orientation='v',
            color = "Brand",
            title = "Top 10 Cosmetics Eye Cream Brands by Price"
        )
        return html.Div(dcc.Graph(figure=fig) , id="bar_volume5")
    return html.Div(id="bar_volume5")

def render6(app):
    df = get_Sunprotect()

    @app.callback(
        Output("bar_volume6","children"),
        Input("sun_dropdown","value")
    )
    def update_bar_chart(dropdown):
        filtered_data = df.query("Brand in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div(
                dbc.Alert("No Brand selected", color="danger")
                ,id="bar_volume6")
            
        fig = px.bar(
            filtered_data,
            x="Brand", 
            y="Price",
            orientation='v',
            color = "Brand",
            title = "Top 10 Cosmetics Sun Protect Brands by Price"
        )
        return html.Div(dcc.Graph(figure=fig) , id="bar_volume6")
    return html.Div(id="bar_volume6")

def render7(app):
    df = get_FaceMask()

    @app.callback(
        Output("bar_volume7","children"),
        Input("face_dropdown","value")
    )
    def update_bar_chart(dropdown):
        filtered_data = df.query("Brand in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div(
                dbc.Alert("No Brand selected", color="danger")
                ,id="bar_volume7")
            
        fig = px.bar(
            filtered_data,
            x="Brand", 
            y="Price",
            orientation='v',
            color = "Brand",
            title = "Top 10 Cosmetics Face Mask Brands by Price"
        )
        return html.Div(dcc.Graph(figure=fig) , id="bar_volume7")
    return html.Div(id="bar_volume7")

def render8(app):
    df = get_Cleanser()

    @app.callback(
        Output("bar_volume8","children"),
        Input("cle_dropdown","value")
    )
    def update_bar_chart(dropdown):
        filtered_data = df.query("Brand in @dropdown")
        if filtered_data.shape[0]==0:
            return html.Div(
                dbc.Alert("No Brand selected", color="danger")
                ,id="bar_volume8")
            
        fig = px.bar(
            filtered_data,
            x="Brand", 
            y="Price",
            orientation='v',
            color = "Brand",
            title = "Top 10 Cosmetics Cleanser Brands by Price"
        )
        return html.Div(dcc.Graph(figure=fig) , id="bar_volume8")
    return html.Div(id="bar_volume8")