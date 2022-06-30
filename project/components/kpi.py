from dash import html

def kpi(text, value, className = ""):
    return html.Div(
        className='kpi ' + className,
        children=[
             html.Span(
                value,
                className='kpi__value'
             ),
             html.Span(
                text,
                className='kpi__text'
             )
        ] 
    )