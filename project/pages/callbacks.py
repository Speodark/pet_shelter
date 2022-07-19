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


# filtering by the binary filters
def filter_by_binary_filters(ids, binary_filters, filtered_df):
    # going through all the binary filters ids
    for index, binary_filter in enumerate(ids):
        # checking if the binary filter been activated
        if binary_filters[index]:
            # Checking if the values are boolean if they are convert the variable to boolean instead of string
            if 'true' in binary_filters[index].lower() or 'false' in binary_filters[index].lower():
                binary_filters[index] = json.loads(binary_filters[index].lower())
            # filtering the dataframe by the binary filter
            filtered_df = filtered_df[filtered_df[binary_filter]==binary_filters[index]]
    # Returning the df
    return filtered_df


# filtering by the bar charts selected data
def filter_by_bar_chart_data(ids, bar_charts_data, filtered_df): 
    # going through all the bar charts ids
    for index, bar_chart_id in enumerate(ids):
        # checking if there are selected data
        if bar_charts_data[index]:
            categories = []
            # going through each bar in the selected bar charts to get the choosen categories
            for bar in bar_charts_data[index]['points']:
                categories.append(bar['y'])
            # filtering the dataframe by the bar charts
            filtered_df = filtered_df[filtered_df[bar_chart_id].isin(categories)]
    return filtered_df

    
@app.callback(
    Output('date-range', 'min_date_allowed'),
    Output('date-range', 'max_date_allowed'),
    Output('date-range', 'initial_visible_month'),
    Input({'type':'binary_filter','id':ALL, 'sub_type':'value'}, 'children'),
    Input({'type':'bar_chart','id':ALL},'selectedData'),
    prevent_initial_call=True
)
def update_date_picker(binary_filters, bar_charts_data):
    # making a copy of the original dataframe
    filtered_df = df


    # getting a list of ids of all the binary filters
    binary_filters_ids = [id['id']['id'] for id in dash.callback_context.inputs_list[0]]
    # filtering by the binary filters
    filtered_df = filter_by_binary_filters(binary_filters_ids, binary_filters, filtered_df)


    # getting a list of ids of all the bar charts
    bar_Charts_ids = [id['id']['id'] for id in dash.callback_context.inputs_list[1]]
    # filtering by the bar charts selected data
    filtered_df = filter_by_bar_chart_data(bar_Charts_ids, bar_charts_data, filtered_df)
    

    # get the minimum and maximum dates, we have to convert them from numpy array to pandas datetime.
    min_date, max_date = pd.to_datetime(filtered_df['datetime'].min()), pd.to_datetime(filtered_df['datetime'].max())
    # Return the dates
    return min_date, max_date, max_date
