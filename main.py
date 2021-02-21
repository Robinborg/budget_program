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
def choose_day(number_for_day):
    choice_of_days = {
     1:'Monday',        
     2:'Tuesday',        
     3:'Wednesday',        
     4:'Thursday',       
     5:'Friday',        
     6:'Saturday',        
     7:'Sunday',        
    }    
    return choice_of_days.get(number_for_day, "Invalid day")
choose_day(4)
if __name__ == '__main__':
    print(choose_day(4))
    print(choose_day(5))
