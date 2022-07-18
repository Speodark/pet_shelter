from dash import html
from components.kpi import kpi
from components.binary_filter import binary_filter

def sub_header(df, className=''):
    return html.Div(
        className = 'sub-header ' + className,
        children=[
            kpi(
                text='Animal Count', 
                value=len(df),
                className='sub-header__animal-count'
            ),
            kpi(
                text='Adopted', 
                value=len(df[df.outcome_type == 'Adoption']),
                className='sub-header__adopted'
            ),
            binary_filter(
                id = 'sex',
                categories=['Male','Female'],
                colors=['pink','#2B80FF'],
                className='sub-header__gender'
            ),
            binary_filter(
                id = 'castrated',
                categories=['True','False'],
                colors=['green','red'],
                className='sub-header__castrated'
            )
        ]
    )