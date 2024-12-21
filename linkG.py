########### import libaries
import pandas as pd
import requests
from bs4 import BeautifulSoup

#### sending GET request to website
## Website URL
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
if page.status_code == 200:
    print("webpage content successfully fetched")
else:
    print("failed to fetch the webpage content.\n check your url")
###parsing the HTML content with Beautiful Soup
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)
table = soup.find('table', class_ = "wikitable sortable")
table_count = len(soup.find_all('table'))
print(f"Length of the table is {table_count}".format(table_count))
table = soup.find_all('table')[0]
column_title = table.find_all('th')
print(column_title)

column_table_title = [title.text.strip()for title in column_title]
print(column_table_title)
##store data in pandas
df = pd.DataFrame(columns = column_table_title)
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length]=individual_row_data

print(df)
dff = pd.DataFrame(data=df)
fileName = input('PLease enter file Name:   ')
savedData = df.to_csv(fileName+'.csv', index = True)
