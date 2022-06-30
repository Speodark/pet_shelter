import vaex
from dash import html, dcc
from components.card import card
from pages.callbacks import *
from layout.header import header
from layout.sub_header import sub_header


def context_tabs():
    return html.Div(
        className='content_tabs'
    )


def dashboard():
    return html.Div(
        className='dashboard',
        children=[
            header(),
            sub_header(),
            context_tabs()
        ]
    )