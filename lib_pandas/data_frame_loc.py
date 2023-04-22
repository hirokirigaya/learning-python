import pandas as pd

names_list = 'João Maria José'.split()
dfs = pd.DataFrame(names_list, columns=['name'])

dfs['age'] = 30
dfs = dfs._append({ 'name': 'Daniel', 'age': 20}, ignore_index=True)

print(dfs.loc[(dfs['age'] < 30)])