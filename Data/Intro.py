import pandas as pd
df = pd.read_csv('survey_results_public.csv', index_col='ResponseID')
schema_df = pd.read_csv('survey_results_schema.csv', index_col='Column')
pd.set_option('display.max_columns', 48)
pd.set_option('display.max_rows', 48)
df.head()
schema_df.loc['Ethnicity']
schema_df.sort_index(inplace=True)
