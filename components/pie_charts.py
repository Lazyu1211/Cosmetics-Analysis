from dash import Dash, html, dcc
import plotly.express as px
from utill import get_com, get_dry, get_normal, get_Oily, get_Sensitive

def render(app):
    df = get_com()
    fig = px.pie(df, values = 'Price', names = df['Combination'], color_discrete_sequence=['#29CDFF', '#FF6019'], title = 'Combination with Mean Price')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart")

def render1(app):
    df = get_dry()
    fig = px.pie(df, values = 'Price', names = df['Dry'], color_discrete_sequence=['#29CDFF', '#FF6019'], title = 'Dry with Mean Price')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart1")

def render2(app):
    df = get_normal()
    fig = px.pie(df, values = 'Price', names = df['Normal'], color_discrete_sequence=['#29CDFF', '#FF6019'], title = 'Normal with Mean Price')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart2")

def render3(app):
    df = get_Oily()
    fig = px.pie(df, values = 'Price', names = df['Oily'], color_discrete_sequence=['#29CDFF', '#FF6019'], title = 'Oily with Mean Price')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart3")

def render4(app):
    df = get_Sensitive()
    fig = px.pie(df, values = 'Price', names = df['Sensitive'], color_discrete_sequence=['#29CDFF', '#FF6019'], title = 'Sensitive with Mean Price')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart4")