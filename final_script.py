import pandas as pd
import numpy as np

def convert_currency(val):
    """
    125000.00
    Convert the string number value to a float
     - Remove $
     - Remove commas
     - Convert to float type
    """
    new_val = val.replace(',','').replace('$', '')
    return float(new_val)

def convert_percent(val):
    """
    Convert the percentage string to an actual floating point percent
    """
    new_val = val.replace('%', '')
    return float(new_val) / 100
    
df_3 = pd.read_csv("https://github.com/chris1610/pbpython/blob/master/data/sales_data_types.csv?raw=True", 
                   dtype={'Customer Number':'int'},
                   converters={'2016':convert_currency,
                               '2017': convert_currency,
                               'Percent Growth': convert_percent,
                               'Jan Units': lambda x: pd.to_numeric(x, errors='coerce'),
                               'Active': lambda x: np.where(x == "Y", True, False)
                              })

df_3["Jan Units"] = pd.to_numeric(df_3['Jan Units'], errors='coerce').fillna(0)

df_3["Start_Date"] = pd.to_datetime(df_3[['Month', 'Day', 'Year']])
print(df_3)
