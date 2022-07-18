from dash import Input, Output, ALL, State, MATCH, ctx
from dash.exceptions import PreventUpdate
import vaex
from main_dash import app
import dash
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json

df = vaex.open('assets/data/data.hdf5')


@app.callback(
    Output('date-range', 'min_date_allowed'),
    Output('date-range', 'max_date_allowed'),
    Output('date-range', 'initial_visible_month'),
    Input({'type':'binary_filter','id':ALL, 'sub_type':'value'}, 'children'),
    prevent_initial_call=True
)
def update_date_picker(binary_filters):
    ### binary filters ###
    # getting a list of ids of all the binary filters
    binary_filters_id_list = [id['id']['id'] for id in dash.callback_context.inputs_list[0]]
    # making a copy of the original dataframe
    filtered_df = df
    # going through all the binary filters ids
    for index, binary_filter in enumerate(binary_filters_id_list):
        # checking if the binary filter been activated
        if binary_filters[index]:
            # Checking if the values are boolean if they are convert the variable to boolean instead of string
            if 'true' in binary_filters[index].lower() or 'false' in binary_filters[index].lower():
                binary_filters[index] = json.loads(binary_filters[index].lower())
            # filtering the dataframe by the binary filter
            filtered_df = filtered_df[filtered_df[binary_filter]==binary_filters[index]]
    # get the minimum and maximum dates, we have to convert them from numpy array to pandas datetime.
    min_date, max_date = pd.to_datetime(filtered_df['datetime'].min()), pd.to_datetime(filtered_df['datetime'].max())
    # Return the dates
    return min_date, max_date, max_date
