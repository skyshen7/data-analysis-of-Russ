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
    table_divs = soup.find_all('div', class_='mb-5')

    # Iterate over each div to find tables within them
    for div in table_divs:
        # Find the table within the div, assuming there is only one table per div
        #table = div.find('table')
    
        # Proceed if a table is found
        #if table:
            # Find the body of the table
        tbody = div.find('tbody')
        
            # Continue if the table body is found
        if tbody:
          ß      # Find all rows in the table body
        all_rows = tbody.find_all('tr')

                # Extract data from each row
        for row in all_rows:
            cells = row.find_all('td')
            row_data = [cell.get_text(strip=True) for cell in cells]
            all_tables_data.append(row_data)
    print(all_tables_data)

get_stat(2020)