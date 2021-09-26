import pandas as pd


def email_(file_name):
    df = pd.read_csv('email.csv')
    for index, row in 'email.csv'.iterrows():
        print(['Company name; ', df])
