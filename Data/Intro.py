import pandas as pd
df = pd.read_csv('survey_results_public.csv', index_col='ResponseId')
# schema_df = pd.read_csv('survey_results_schema.csv', index_col='Column')
pd.set_option('display.max_columns', 48)
pd.set_option('display.max_rows', 48)
df.head()
high_salary = (df['ConvertedCompYearly'] > 70000)
filt = df['LanguageHaveWorkedWith'].str.contains('Python', na=False)
df.loc[filt, 'LanguageHaveWorkedWith']
