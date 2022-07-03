from dash import html
from components.kpi import kpi
from components.binary_filter import binary_filter

def sub_header(className=''):
    return html.Div(
        className = 'sub-header ' + className,
        children=[
            kpi(
                text='Animal Count', 
                value='70,535',
                className='sub-header__animal-count'
            ),
            kpi(
                text='Adopted', 
                value='22,050',
                className='sub-header__adopted'
            ),
            binary_filter(
                id = 'gender',
                categories=["Men",'Female'],
                className="sub-header__gender"
            ),
            binary_filter(
                id = 'castrated',
                categories=["Men",'Female'],
                className="sub-header__castrated"
            )
        ]
    )