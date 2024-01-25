from bs4 import BeautifulSoup
import requests
import pandas as pd

years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 
         2018, 2019, 2020, 2021, 2022, 2023]

def get_stat(year):
    web = f'https://www.statmuse.com/nba/player/russell-westbrook-3933/game-log?seasonYear={year}'
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml') # extract data


    # Initialize a list to store all the tables' data
    all_tables_data = []

    # Find all divs that contain tables
    tables = soup.find_all('div', class_='mb-5')

    # Iterate over each div to find tables within them
    for table in tables:
        tbody = table.find('tbody')                # assuming there is only one table per div
        if tbody:                                  # Continue if the table body is found
            all_rows = tbody.find_all('tr')                 # Find all rows in the table body
            for row in all_rows:                            # Extract data from each row
                cells = row.find_all('td')
                row_data = [cell.get_text(strip=True) for cell in cells]
                all_tables_data.append(row_data)
    print(all_tables_data)

get_stat(2020)