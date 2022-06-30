from dash import html, dcc
import dash_mantine_components as dmc
from dash import Input, Output, ALL, State, MATCH, ctx
from main_dash import app

def binary_filter(id, category1, category2):
    category1_id = id.copy()
    category1_id['index'] = '1'
    category2_id = id.copy()
    category2_id['index'] = '2'
    print(id)
    print()
    print(category1_id)
    print()
    print(category2_id)
    print()
    return html.Div(
        className='binary-filter',
        children=[
            dcc.Checklist(
                [''],
                inputClassName ='binary-filter__checkbox',
                className="fill-parent-div binary-filter__checklist",
                id=id
            ),
            html.Span(
                className='binary-filter__item binary-filter__item--1',
                children=category1,
                id = category1_id
            ),
            html.Span(
                className='binary-filter__item binary-filter__item--2',
                children=category2,
                id = category2_id
            ),
            html.Div(
                className='binary-filter__slider',
            )
        ]
    )


# @app.callback(
#     Output({'type':'binary_filter','id':MATCH}, 'value'), 
#     Input({'type':'binary_filter','id':MATCH}, 'value'), # input 0
#     prevent_initial_call=True
# )