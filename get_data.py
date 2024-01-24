from bs4 import BeautifulSoup
import requests
import pandas as pd

years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 
         2018, 2019, 2020, 2021, 2022, 2023]

web = f'https://www.statmuse.com/nba/player/russell-westbrook-3933/game-log?seasonYear=2009'
response = requests.get(web)
content = response.text
soup = BeautifulSoup(content, 'lxml') # extract data

table_body = soup.find('tbody') #Look for table
all_rows_data = []

if table_body:
    all_rows = table_body.find_all('tr') 

    for row in all_rows:
        cells = row.find_all('td')
        row_data = [cell.get_text(strip=True) for cell in cells]
        all_rows_data.append(row_data)

print(all_rows_data)

