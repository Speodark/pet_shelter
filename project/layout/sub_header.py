from dash import html
from components.kpi import kpi
from components.binary_filter import binary_filter

def sub_header():
    return html.Div(
        className = 'sub_header',
        children=[
            kpi('Animal Count', '70,535'),
            kpi('Adopted', '22,050'),
            binary_filter(
                id = {'type':'binary_filter','id':'gender'},
                category1="Female",
                category2="Men"
            ),
            binary_filter(
                id = {'type':'binary_filter','id':'castrated'},
                category1="Men",
                category2="Female"
            )
        ]
    )