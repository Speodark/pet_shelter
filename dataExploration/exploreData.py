import vaex 
import pandas as pd
import numpy as np
import re
import plotly.figure_factory as ff
import plotly.io as pio
pio.renderers.default = 'browser'

df_csv = pd.read_csv('data.csv',parse_dates=['date_of_birth', 'datetime'])
df_csv = df_csv.replace(np.nan,'Unknown', regex=True)
df_csv = df_csv.drop(['Unnamed: 0'], axis=1)
df_csv.to_csv('data.csv')
df2 = vaex.from_csv('data.csv', convert=True, chunk_size=5_000_000)

df_csv['datetime'] = pd.to_datetime(df_csv['datetime']).dt.date

df = pd.read_csv('aac_shelter_outcomes.csv',parse_dates=['date_of_birth', 'datetime'])
df = df.drop_duplicates()
# get rid of unknown gender 
df = df.replace('Unknown', np.nan, regex=True)


# making the gender column
df = df[df['sex_upon_outcome'].notna()]
sex = []
for sex_upon_outcome in df.sex_upon_outcome:
    if 'Male' in sex_upon_outcome:
        sex.append('Male')
    elif 'Female' in sex_upon_outcome:
        sex.append('Female')
    else:
        notin.append(sex_upon_outcome)
df['sex'] = sex

# making the castrated column
castrated = []
for sex_upon_outcome in df.sex_upon_outcome:
    if 'neutered' in sex_upon_outcome.lower() or 'spayed' in sex_upon_outcome.lower():
        castrated.append(True)
    elif 'intact' in sex_upon_outcome.lower():
        castrated.append(False)
    else:
        print(sex_upon_outcome)
df['castrated'] = castrated

df = df.drop(['monthyear', 'sex_upon_outcome'], axis=1)
df_csv = df_csv.drop(['Unnamed: 0'], axis=1)
df_csv.to_csv('data.csv')




df['got_to_shelter_year'] = df.age_upon_outcome.copy()

df_adopted = df[df['outcome_type'] == 'Adoption']
# make the age_upon_outcome
temp = df_adopted.age_upon_outcome 


df_csv.age_upon_outcome = df_csv.age_upon_outcome.replace(np.nan,'0 weeks', regex=True)
years = []
for came_to_shelter in df_csv.age_upon_outcome:
    print(came_to_shelter)
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
df_csv.age_upon_outcome = years

fig = ff.create_distplot([years], ['distplot'])
fig.show()
