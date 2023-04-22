import pandas as pd
from datetime import date

# Create a DataFrame from a list
names_list = 'João Maria José'.split()

dfs = pd.DataFrame(names_list, columns=['name'])

extracted_data = date.today()
dfs['extracted_data'] = pd.to_datetime(extracted_data)

print(dfs.info())
