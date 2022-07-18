import vaex
from dash import html, dcc
from components.card import card
from pages.callbacks import *
from layout.header import header
from layout.sub_header import sub_header
from components.horizontal_bar_chart import horizontal_bar_chart
from components.stacked_bar_chart import stacked_bar_chart
import pandas as pd
import numpy as np

# The overview tab 
def overview_tab(df):
    temp_df = {
        'outcome':['Transfer','adoption','Transfer','adoption','Transfer','adoption'],
        'date':['15/5/2002','18/9/2020','12/10/2015','15/5/2002','18/9/2020','12/10/2015'],
        'value':[40,20,30,40,10,30]
    }
    temp_df = pd.DataFrame(temp_df)
    outcome = df.groupby(['outcome_type'],agg='count').to_pandas_df()
    outcome = outcome.sort_values(by=['count'])
    animal_type = df.groupby(['animal_type'],agg='count').to_pandas_df()
    animal_type = animal_type.sort_values(by=['count'])
    outcome_type_date = df.groupby(['outcome_type','datetime'],agg='count').to_pandas_df()
    outcome_type_date = outcome_type_date.replace(np.nan,'Unknown', regex=True)
    return html.Div(
        children=[
            # Outcome graph
            card(
                header='Outcome',
                children=dcc.Graph(
                    figure=horizontal_bar_chart(
                        categories=outcome['outcome_type'],
                        values=outcome['count'],
                    ),
                    responsive=True, 
                    className="fill-parent-div sm-padding",
                ),
                className="dashboard__overview--outcome center_items_vertical"
            ),
            # Animal Type graph
            card(
                header='Animal Type',
                children=dcc.Graph(
                    figure=horizontal_bar_chart(
                        categories=animal_type['animal_type'],
                        values=animal_type['count'],
                    ),
                    responsive=True, 
                    className="fill-parent-div sm-padding",
                ),
                className="dashboard__overview--animal-type center_items_vertical"
            ),
            # Animal Type graph
            card(
                header='Amount of outcome by Type and Date',
                children=dcc.Graph(
                    figure=stacked_bar_chart(
                        df = outcome_type_date,
                        x_axis = 'datetime',
                        y_axis='count',
                        category='outcome_type'
                    ),
                    responsive=True, 
                    className="fill-parent-div sm-padding",
                ),
                className="dashboard__overview--outcome-time center_items_vertical"
            ),
            # Age slider
            html.Div(
                children=[
                    html.Span("Age upon outcome Range"),
                    dcc.RangeSlider(
                        min=int(df.age_upon_outcome.min()),
                        max=int(df.age_upon_outcome.max()),
                        step=1,
                        value=[int(df.age_upon_outcome.min()),int(df.age_upon_outcome.max())],
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
def tabs(df):
    return html.Div(
        children=dcc.Tabs(
            children=[
                # First content page
                dcc.Tab(
                    label="OverView",
                    children=overview_tab(df)
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
    df = vaex.open('assets/data/data.hdf5')
    return html.Div(
        className='dashboard',
        children=[
            header(
                df = df,
                className='dashboard__header'
            ),
            sub_header(
                df = df,
                className='dashboard__sub-header'
            ),
            tabs(df)
        ]
    )