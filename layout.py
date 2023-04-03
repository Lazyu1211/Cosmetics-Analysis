from dash import Dash,html,dcc
import dash_bootstrap_components as dbc
from components import bar_charts, dropdown, scatter, pie_charts

image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgcXN1b1b_7dI0hs8RD_p6lBTV3DDn-qjugIEyj5NJtmyganUK6LTeBzjQZouR8J02ftc&usqp=CAU"
image_path1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJeoXUQfVHIRsANNjrnYBG11nqDPo6RdyDug&usqp=CAU"

def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.H1(
                "Cosmetics Analysis", className="header-title", style={'margin-top': '10px', 'text-align': 'center'}
              ),
        html.P(children="✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨", className="header-emoji", style={'margin-top': '10px', 'text-align': 'left'}),
        html.Img(src=image_path, style={"width": "660px", "height": "400px"}),
        html.Img(src=image_path1, style={"width": "660px", "height": "400px"}),
        html.P(children="✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨", className="header-emoji", style={'margin-top': '10px', 'text-align': 'left'})
,       
    ],className="mt-4"),
        dbc.Row([
            html.H2(
                "Top 10 Cosmetics Brands in the Dataset",
                className="header-description", style={'margin-top': '10px', 'text-align': 'center'}
                ),
            dbc.Col(dropdown.render(app),lg=12, style={'margin-top': '30px', 'text-align': 'left'}),
            html.H6(
                "Top Three Brands",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(63, 79, step=None, marks={63:'SHISEIDO', 66:'SEPHORA COLLECTION', 79:'CLINIQUE'}, value=5,id='my-slider', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container'),
            dbc.Col(bar_charts.render(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
                        html.H2(
                "Top 10 Cosmetics Brands by Price",
                className="header-description", style={'margin-top': '50px', 'text-align': 'center'}
                ),
            dbc.Col(dropdown.render1(app),lg=12, style={'margin-top': '30px', 'text-align': 'left'}),
            html.H6(
                "Top Three Brands",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(169, 184, step=None, marks={169:'LIGHTSTIM', 171:'BIOEFFECT', 184:'LA MER'}, value=5,id='my-slider1', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container1'),
            dbc.Col(bar_charts.render1(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(scatter.render(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
             html.H6(
                "Labels Average Price",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(32, 80, step=None, marks={32.6:'Cleanser', 63.6:'Eye cream', 42.6:'Face Mask',69:"Moisturizer", 45.9:"Sun protect",79.2:"Treatment"}, value=5,id='my-slider2', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container2'),
            dbc.Col(pie_charts.render(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render1(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render2(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render3(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render4(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render2(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            html.H2(
                "Top 10 Cosmetics Treatment Brands by Price",
                className="header-description", style={'margin-top': '50px', 'text-align': 'center'}
                ),
            dbc.Col(dropdown.render2(app),lg=12, style={'margin-top': '30px', 'text-align': 'left'}),
            html.H6(
                "Top Three Brands",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(198, 263, step=None, marks={213:'LANCER', 198:'BIOEFFECT', 263:'LA MER'}, value=5,id='my-slider3', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container3'),
            dbc.Col(bar_charts.render3(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
            html.H2(
                "Top 10 Cosmetics Moisturizer Brands by Price",
                className="header-description", style={'margin-top': '50px', 'text-align': 'center'}
                ),
            dbc.Col(dropdown.render3(app),lg=12, style={'margin-top': '30px', 'text-align': 'left'}),
            html.H6(
                "Top Three Brands",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(129, 204, step=None, marks={129:'DIOR', 189:'SK_II', 204:'LA MER'}, value=5,id='my-slider4', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container4'),
            dbc.Col(bar_charts.render4(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
            html.H2(
                "Top 10 Cosmetics Eye Cream Brands by Price",
                className="header-description", style={'margin-top': '50px', 'text-align': 'center'}
                ),
            dbc.Col(dropdown.render4(app),lg=12, style={'margin-top': '30px', 'text-align': 'left'}),
            html.H6(
                "Top Three Brands",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(165, 228, step=None, marks={215:'GUERLAIN', 165:'SK_II', 228:'LA MER'}, value=5,id='my-slider5', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container5'),
            dbc.Col(bar_charts.render5(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
            html.H2(
                "Top 10 Cosmetics Sun Protect Brands by Price",
                className="header-description", style={'margin-top': '50px', 'text-align': 'center'}
                ),
            dbc.Col(dropdown.render5(app),lg=12, style={'margin-top': '30px', 'text-align': 'left'}),
            html.H6(
                "Top Three Brands",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(90, 100, step=None, marks={90:'EVE LOM', 100:'KAPLAN MD', 95:'LA MER'}, value=5,id='my-slider6', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container6'),
            dbc.Col(bar_charts.render6(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
            html.H2(
                "Top 10 Cosmetics Face Mask Brands by Price",
                className="header-description", style={'margin-top': '50px', 'text-align': 'center'}
                ),
            dbc.Col(dropdown.render6(app),lg=12, style={'margin-top': '30px', 'text-align': 'left'}),
            html.H6(
                "Top Three Brands",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(137, 179, step=None, marks={170:'LANCER', 137:'SK_II', 179:'LA MER'}, value=5,id='my-slider7', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container7'),
            dbc.Col(bar_charts.render7(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'}),
            html.H2(
                "Top 10 Cosmetics Cleanser Brands by Price",
                className="header-description", style={'margin-top': '50px', 'text-align': 'center'}
                ),
            dbc.Col(dropdown.render7(app),lg=12, style={'margin-top': '30px', 'text-align': 'left'}),
            html.H6(
                "Top Three Brands",
                className="header-description", style={'margin-top': '30px', 'text-align': 'center'}
                ),
            dcc.Slider(68, 83, step=None, marks={68:'DR.BRANDT SKINCARE', 74:'SK_II', 83:'LA MER'}, value=5,id='my-slider8', tooltip={'always_visible': True, 'placement': 'top'}),html.Div(id='slider-output-container8'),
            dbc.Col(bar_charts.render8(app),lg=12,style={'margin-top': '30px', 'text-align': 'center'})
        ],className="mt-4"),
    ])