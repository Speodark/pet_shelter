from dash import html, dcc
from datetime import datetime as dt
import dash_datetimepicker

def header(df, className = ''):
    return html.Div(
        className = 'header ' + className,
        children=[
            dcc.DatePickerRange(
                id='my-date-picker-range',  # ID to be used for callback
                calendar_orientation='horizontal',  # vertical or horizontal
                day_size=39,  # size of calendar image. Default is 39
                end_date_placeholder_text="Return",  # text that appears when no end date chosen
                with_portal=False,  # if True calendar will open in a full screen overlay portal
                first_day_of_week=0,  # Display of calendar when open (0 = Sunday)
                reopen_calendar_on_clear=True,
                is_RTL=False,  # True or False for direction of calendar
                clearable=True,  # whether or not the user can clear the dropdown
                number_of_months_shown=2,  # number of months shown when calendar is open
                min_date_allowed=dt(2018, 1, 1),  # minimum date allowed on the DatePickerRange component
                max_date_allowed=dt(2020, 6, 20),  # maximum date allowed on the DatePickerRange component
                initial_visible_month=dt(2020, 5, 1),  # the month initially presented when the user opens the calendar
                start_date=dt(2018, 8, 7).date(),
                end_date=dt(2020, 5, 15).date(),
                display_format='MMM Do, YY',  # how selected dates are displayed in the DatePickerRange component.
                month_format='MMMM, YYYY',  # how calendar headers are displayed when the calendar is opened.
                minimum_nights=2,  # minimum number of days between start and end date
                persistence=True,
                persisted_props=['start_date'],
                persistence_type='session',  # session, local, or memory. Default is 'local'
                updatemode='singledate',  # singledate or bothdates. Determines when callback is triggered
                stay_open_on_select = True,
                className='header__date-picker-range'
            ),
            html.P(children='Animal Shelter', className='header__title'),
            html.Div(
                children=html.Button(
                    children=[
                        html.Span('Export'),
                        html.Span(className='arrow arrow__down header__export--arrow')
                    ],
                    className='header__export--btn'
                ),
                className='header__export'
            )
            
        ]
    )