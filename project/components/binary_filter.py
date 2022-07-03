from dash import html, dcc
from dash import Input, Output, ALL, State, MATCH, ctx
from main_dash import app
import dash

# Points for the future
# i need a reset filter overall dashboard to affect the component
# 


def binary_filter(id, categories, className = ''):
    return html.Div(
        className='binary-filter ' + className,
        children=[
            html.Span(
                className='binary-filter__item binary-filter__item--1',
                children=categories[0],
                id= {'type':'binary_filter','id':id, 'sub_type':'category', 'index':categories[0]}
            ),
            html.Span(
                className='binary-filter__item binary-filter__item--2',
                children=categories[1],
                id= {'type':'binary_filter','id':id, 'sub_type':'category', 'index':categories[1]}
            ),
            html.Div(
                className='hide',
                children='',
                id= {'type':'binary_filter','id':id, 'sub_type':'value'}
            )
        ]
    )


@app.callback(
    Output({'type':'binary_filter','id':MATCH, 'sub_type':'category', 'index':ALL}, 'style'), 
    Output({'type':'binary_filter','id':MATCH, 'sub_type':'value'}, 'children'),
    Input({'type':'binary_filter','id':MATCH, 'sub_type':'category', 'index':ALL}, 'n_clicks'),
    State({'type':'binary_filter','id':MATCH, 'sub_type':'value'}, 'children'),
    prevent_initial_call=True
)
def binary_filter_callback(_, active_filter):
    triggered_category = ctx.triggered_id['index']
    categories_indexs = [category['id']['index'] for category in dash.callback_context.inputs_list[0]]
    if triggered_category in active_filter:   
        return [{},{}], ''
    else:
        return [{} if triggered_category==category else {'filter': 'blur(3px)'} for category in categories_indexs], triggered_category
