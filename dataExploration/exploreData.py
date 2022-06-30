import vaex 
import pandas as pd
import numpy as np
import re
import plotly.figure_factory as ff

df = pd.read_csv('aac_shelter_outcomes.csv')
df = df.drop_duplicates()
df['got_to_shelter_year'] = df.age_upon_outcome.copy()
df = df[df['age_upon_outcome'].notna()]

# make the age_upon_outcome
temp = df.age_upon_outcome
years = []
for came_to_shelter in df.age_upon_outcome:
    if 'weeks' in came_to_shelter or 'week' in came_to_shelter:
        years.append(
            round(
                float(re.sub("[^0-9]","",came_to_shelter))/52.143,
                4
            )
        )
    elif 'days' in came_to_shelter or 'day' in came_to_shelter:
        years.append(
            round(
                float(re.sub("[^0-9]","",came_to_shelter))/365,
                4
            )
        )
    elif 'months' in came_to_shelter or 'month' in came_to_shelter:
        years.append(
            round(
                float(re.sub("[^0-9]","",came_to_shelter))/12,
                4
            )
        )
    elif 'years' in came_to_shelter or 'year' in came_to_shelter:
        years.append(
            round(
                float(re.sub("[^0-9]","",came_to_shelter)),
                4
            )
        )
 
hist_data = [x]
group_labels = ['distplot']
print(df.outcome_type.unique())

fig = ff.create_distplot(hist_data, group_labels)
fig.show()