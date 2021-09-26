import pandas as pd
df = pd.read_csv('email.csv')

for index, row in df.iterrows():
    print(row['email'])
