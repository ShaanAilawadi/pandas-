import pandas as pd
df = pd.read_csv('email.csv')
def row(emails):

    for index, row in df.iterrows():
        print(row['email'])
