import pandas as pd

pd.Series(data=5)


# Create a Series from a list
names_list = 'João Maria José'.split()
pd.Series(names_list)


# Create a Series from a dictionary
names_dict = {
    'name1': 'João',
    'name2': 'Maria',
    'name3': 'José'
}
pd.Series(names_dict)
