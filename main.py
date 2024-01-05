import requests
#from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import pandas as pd

#Url of the page
url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_India'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')

# since there are 2 tables in the page , we are interested only in the 2nd table and hence choosing 2nd table 
table=soup.find_all('table',class_='wikitable sortable')[1]

#Getting the titles from the table
world_titles=table.find_all('th')
world_titles=[x.text.strip() for x in world_titles]

#updating the the number of columns with the titles we got into the dataframe
df=pd.DataFrame(columns=world_titles)

#getting all the columns data 
column_data=table.find_all('tr')

for row in column_data[1:]:
    row_data=row.find_all('td')
    row_data=[x.text.strip() for x in row_data]
    length=len(df)
    df.loc[length]=row_data

#writing the data onto a csv file
df.to_csv('wiki.csv',index=False)
