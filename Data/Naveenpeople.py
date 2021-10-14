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
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'wrongemail@email.com']
}

import pandas as pd

df = pd.DataFrame(people)
df
filt = (df['last'] == 'Schafer') & (df['first'] == 'John')
# df.loc[filt]

for i in range(3):
    person = df.iloc[i]
    if person['first'] in person['email']:
        print(f"{person['first']}'s name is in {person['email']}")
    else:
        print(f"{person['first']} is an idiot")

print(f"{df.iloc[i]['first']}'s email is {df.iloc[i]['email']} ")
