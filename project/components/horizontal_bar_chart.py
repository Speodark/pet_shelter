import plotly.graph_objects as go

def horizontal_bar_chart(values, categories, title=None):
    fig = go.Figure(
        go.Bar(
            x=values,
            y=categories,
            orientation='h'
        )        
    )
    fig.update_layout(
        plot_bgcolor="#fff",
        paper_bgcolor="#fff",
        margin={"t": 30, "b": 0, "r": 20, "l": 0, "pad": 0},
        title_text = title
    )
    fig.update_yaxes(title_text='outcome')
    return fig