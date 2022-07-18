import vaex

# Animal count
df = vaex.open('data.hdf5')
# Adopted
adopted = len(df[df.outcome_type == 'Adoption'])
# Age range
min_age, max_age = df.age_upon_outcome.min(), df.age_upon_outcome.max()
# outcome
outcome = df.groupby(['outcome_type'],agg='count').to_pandas_df()
# Animal type
animal_type = df.groupby(['animal_type'],agg='count').to_pandas_df()
# Outcome by type and date
outcome_type_date = df.groupby(['outcome_type','datetime'],agg='count').to_pandas_df()