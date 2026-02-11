import requests
from bs4 import BeautifulSoup


def scrape_wiki_headings(): # define the scraping function
    url = "https://en.wikipedia.org/wiki/Data_science" # target Wikipedia page

    headers = { # custom User-Agent header
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    exclude_list = ["References", "External links", "See also", "Notes"] # headings to ignore

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

    h2_tags = content_div.find_all('h2') # find all h2 headings

    valid_headings = [] # list to store cleaned headings

    for h2 in h2_tags:
        text = h2.get_text(strip=True) # extract heading text
        text = text.replace('[edit]', '').strip() # remove edit tag

        if any(word in text for word in exclude_list): # skip excluded headings
            continue

        if text and text != "Contents": # ensure heading is valid
            valid_headings.append(text) # store heading

    with open('headings.txt', 'w', encoding='utf-8') as f: # open output file
        for heading in valid_headings:
            f.write(heading + '\n') # write each heading

    print(f"Successfully saved {len(valid_headings)} headings to headings.txt") # success message


if __name__ == "__main__": # run only if executed directly
    scrape_wiki_headings() # call the function
