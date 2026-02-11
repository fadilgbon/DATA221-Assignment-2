import requests
from bs4 import BeautifulSoup
import csv


def scrape_machine_learning_table(): # define the scraping function
    url = "https://en.wikipedia.org/wiki/Machine_learning" # target URL

    headers = { # custom User-Agent header
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers) # send GET request
        response.raise_for_status() # raise error if request failed
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}") # print error message
        return # stop execution if request fails

    soup = BeautifulSoup(response.text, 'html.parser') # parse HTML content

    content_div = soup.find('div', id='mw-content-text') # find main content area
    if not content_div:
        print("Could not find the main content area.") # notify if missing
        return # stop execution

    tables = content_div.find_all('table') # find all tables in content

    for table in tables:
        rows = table.find_all('tr') # get all table rows

        data_rows = [r for r in rows if r.find('td')] # filter rows with data cells

        if len(data_rows) >= 3: # check if table has at least 3 data rows
            max_cols = 0 # track max number of columns
            all_table_data = [] # store all extracted rows

            for r in rows:
                cells = r.find_all(['td', 'th']) # get header or data cells
                row_content = [cell.get_text(separator=' ', strip=True) for cell in cells] # extract text
                if row_content:
                    all_table_data.append(row_content) # store row
                    max_cols = max(max_cols, len(row_content)) # update max columns

            first_row_has_th = bool(rows[0].find('th')) # check if first row has headers

            if first_row_has_th and all_table_data:
                headers_list = all_table_data.pop(0) # use first row as headers
            else:
                headers_list = [f"col{i + 1}" for i in range(max_cols)] # generate generic headers

            while len(headers_list) < max_cols:
                headers_list.append(f"col{len(headers_list) + 1}") # pad headers if needed

            final_rows = [] # list for cleaned rows
            for row in all_table_data:
                cleaned_row = [' '.join(cell.split()) for cell in row] # clean whitespace

                while len(cleaned_row) < len(headers_list):
                    cleaned_row.append("") # pad missing values

                final_rows.append(cleaned_row[:len(headers_list)]) # trim extra values

            with open('wiki_table.csv', 'w', newline='', encoding='utf-8') as f: # open CSV file
                writer = csv.writer(f) # create CSV writer
                writer.writerow(headers_list) # write header row
                writer.writerows(final_rows) # write all data rows

            print(f"Successfully scraped a table with {len(headers_list)} columns and {len(final_rows)} rows.") # success message
            return # stop after first valid table

    print("No table found with at least 3 data rows.") # fallback message


if __name__ == "__main__": # run script only when executed directly
    scrape_machine_learning_table() # call the scraping function
