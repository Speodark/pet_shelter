import vaex
from dash import html, dcc
from components.card import card
from pages.callbacks import *
from layout.header import header
from layout.sub_header import sub_header
from components.horizontal_bar_chart import horizontal_bar_chart
from components.stacked_bar_chart import stacked_bar_chart
import pandas as pd


# The overview tab 
def overview_tab():
    temp_df = {
        'outcome':['Transfer','adoption','Transfer','adoption','Transfer','adoption'],
        'date':['15/5/2002','18/9/2020','12/10/2015','15/5/2002','18/9/2020','12/10/2015'],
        'value':[40,20,30,40,10,30]
    }
    temp_df = pd.DataFrame(temp_df)
    return html.Div(
        children=[
            # Outcome graph
            dcc.Graph(
                figure=horizontal_bar_chart(
                    [20,30,40],
                    ["hello love here","dear","guy"]
                ),
                className="dashboard__overview--outcome"
            ),
            # Animal Type graph
            dcc.Graph(
                figure=horizontal_bar_chart(
                    [20,30,40],
                    ["hello love here","dear","guy"]
                ),
                className="dashboard__overview--animal-type"
            ),
            # Animal Type graph
            dcc.Graph(
                figure=stacked_bar_chart(
                    df = temp_df,
                    x_axis = 'date',
                    y_axis='value',
                    category='outcome'
                ),
                className="dashboard__overview--outcome-time"
            ),
            # Age slider
            html.Div(
                children=[
                    html.Span("Age Range"),
                    dcc.RangeSlider(
                        min=0,
                        max=20,
                        step=1,
                        value=[5,15],
                        id='ranger', 
                        className="dashboard__overview--age-range__slider"
                    )
                ],
                className="dashboard__overview--age-range"
            )
            
        ],
        className='dashboard__overview'
    )


# All the tabs
def tabs():
    return html.Div(
        children=dcc.Tabs(
            children=[
                # First content page
                dcc.Tab(
                    label="OverView",
                    children=overview_tab()
                ),
                # Drilldown Page
                dcc.Tab(
                    label="DrillDown",
                    children=[
                        
                    ],
                    selected_className="dashboard__overview"
                )
            ]
        ),
        className="dashboard__tabs"
    )


def dashboard():
    return html.Div(
        className='dashboard',
        children=[
            header(className='dashboard__header'),
            sub_header(className='dashboard__sub-header'),
            tabs()
        ]
    )