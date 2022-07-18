import plotly.express as px


def stacked_bar_chart(df, x_axis, y_axis, category):
    # x_labels = []
    # for label in categories:
    #     x_labels.append(label.replace(' ', '<br>'))
    fig = px.bar(
        df,
        x=x_axis,
        y=y_axis,
        color = category
    )
    fig.update_layout(
        plot_bgcolor="#fff",
        paper_bgcolor="#fff",
        legend=dict(
            orientation="h",
            yanchor="middle",
            y=1.1,
            xanchor="center",
            x=0.5,
            title={'text': None}
        ),
        margin={"t": 30, "b": 0, "r": 20, "l": 0, "pad": 0},
    )
    # fig.update_yaxes(title_text='')
    # fig.update_xaxes(
    #     title_text='', tickvals=categories, ticktext=x_labels)
    return fig