person = {
    "first": "Corey",
    "last": "Schafer",
    "email": "CoreyMSchafer@gmail.com"
}

people = {
    "first": "Corey",
    "last": "Schafer",
    "email": "CoreyMSchafer@gmail.com"
}

people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

import pandas as pd

df = pd.DataFrame(people)
df
df.columns = ['first_name', 'last_name', 'email']
df.columns = [x.lower() for x in df.columns]
df.rename(columns={'first_name': 'first', 'last_name': 'last'}, inplace=True)
df.loc[2] = ['John', 'Smith', 'JohnDoe@email.com']
df.loc[2, ['last', 'email']] = ['Doe', 'JohnDoe@email.com']
df.loc[2, 'last'] = 'Smith'
filt = (df['email'] == 'JohnDoe@email.com')
df.loc[filt, 'last'] = 'Smith'
df['email'] = df['email']. str.lower()
df['email'].apply(len)


def update_email(email):
    return email.upper()


df['email'] = df['email'].apply(update_email)
df['email'] = df['email'].apply(lambda x: x.lower())
df.apply(len, axis='columns')
(len)(df['email'])
df.apply(pd.Series.min)
df.apply(lambda x: x.min())
df.applymap(len)
df.applymap(str.lower)
df['first'].map({'Corey': 'Chris', 'Jane': 'Mary'})
df['first'] = df['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'})
