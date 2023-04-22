import pandas as pd
import requests

# Create a DataFrame from a list
names_list = 'João Maria José'.split()
data_frame = pd.DataFrame(names_list, columns=['names'])


print(data_frame)
print(data_frame['names'])


# Read a url

url = 'https://en.wikipedia.org/wiki/Minnesota'
getUrl = requests.get(url)
text = getUrl.text
dfs = pd.read_html(text, encoding="UTF-8")
