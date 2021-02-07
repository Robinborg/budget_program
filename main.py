import pandas as pd
import matplotlib
from datetime import datetime

data = {
    'Januari': ['300', '300', '300', '300'],
    'february': ['0', '0', '0', '0'],
    'mars':  ['0', '0', '0', '0'],
    'april': ['0', '0', '0', '0'],
    'may': ['0', '0', '0', '0'],
    'june': ['0', '0', '0', '0'],
    'july': ['0', '0', '0', '0'],
    'august': ['0', '0', '0', '0'],
    'september': ['0', '0', '0', '0'],
    'october': ['0', '0', '0', '0'],
    'november': ['0', '0', '0', '0'],
    'decemeber': ['0', '0', '0', '0'],

}

expense = pd.DataFrame(data, index=["First_week", "Second_week", "Third_week", "Fourth_week"])
income = expense.copy()

# expense['Januari'] = expense['Januari'].replace(['1'],'10')
# print(expense)

date_for_the_day = datetime.date.today()
mothly_income = 1600
# weeks = ['First_week', 'Second_week', 'Third_week', 'Fourth_week']

def real_expenditure():
    which_week = input("Which week is it:\n")
    weekly_expenses = input("What did you spend this week:\n")

     








