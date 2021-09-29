import pandas as pd
df = pd.read_csv('email.csv')


def email(filename):
    for index, row in df.iterrows():
        print(index, row['email'])
