# pages/page1.py
import pandas as pd
import plotly.express as px
from dash import html, dcc
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout
from appshell.data_loader import fig_line_chart, fig_3d_bubble, fig_column_chart, fig_map, fig_yearly_trend

# Define the layout for page1
layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.H2(
                    "Fire Incidents Analysis",
                    style={
                        "color": "rgb(255, 107, 107)",
                        "text-align": "center",
                        "margin-top": "20px",
                    },
                ),
                dcc.Tabs(
                    [
                        dcc.Tab(
                            label="Line Chart",
                            children=[
                                dcc.Graph(
                                    id="example-graph1",
                                    figure=fig_line_chart,
                                    style={
                                        "width": "100%",
                                        "height": "100%",
                                        "margin-top": "20px",
                                        "display": "block",
                                    },
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="3D Bubble Chart",
                            children=[
                                dcc.Graph(
                                    id="example-graph2",
                                    figure=fig_3d_bubble,
                                    style={
                                        "width": "100%",
                                        "height": "100%",
                                        "margin-top": "20px",
                                        "display": "block",
                                    },
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Column Chart",
                            children=[
                                dcc.Graph(
                                    id="example-graph3",
                                    figure=fig_column_chart,
                                    style={
                                        "width": "100%",
                                        "height": "100%",
                                        "margin-top": "20px",
                                        "display": "block",
                                    },
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Map",
                            children=[
                                dcc.Graph(
                                    id="example-graph4",
                                    figure=fig_map,
                                    style={
                                        "width": "100%",
                                        "height": "100%",
                                        "margin-top": "20px",
                                        "display": "block",
                                    },
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Yearly Trend",
                            children=[
                                dcc.Graph(
                                    id="example-graph5",
                                    figure=fig_yearly_trend,
                                    style={
                                        "width": "100%",
                                        "height": "100%",
                                        "margin-top": "20px",
                                        "display": "block",
                                    },
                                )
                            ],
                        ),
                    ]
                ),
            ],
            style={
                "width": "80%",
                "float": "left",
                "height": "calc(100vh - 100px)",
                "padding": "20px",
            },
        ),
    ],
    style={"margin-top": "100px"},
)
