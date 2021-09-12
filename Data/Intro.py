import pandas as pd
df = pd.read_csv('survey_results_public.csv')
schema_df = pd.read_csv('survey_results_schema.csv')
pd.set_option('display.max_columns', 48)
pd.set_option('display.max_rows', 48)
df.head()
schema_df
df['Ethnicity']
df.loc[0:2, 'Gender':'Ethnicity']
