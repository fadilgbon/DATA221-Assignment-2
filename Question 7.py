import requests
from bs4 import BeautifulSoup


def scrape_wiki_data(): # define the scraping function
    url = "https://en.wikipedia.org/wiki/Data_science" # target Wikipedia page

    headers = { # custom User-Agent header
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers) # send GET request
        response.raise_for_status() # raise error if request failed
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}") # print error message
        return # stop execution if request fails

    soup = BeautifulSoup(response.text, 'html.parser') # parse HTML content

    page_title = soup.title.string if soup.title else "No title found" # extract page title
    print(f"Page Title: {page_title}\n") # print page title

    content_div = soup.find('div', id='mw-content-text') # find main content area

    if content_div: # check if content area exists
        paragraphs = content_div.find_all('p') # get all paragraph tags

        first_valid_paragraph = None # placeholder for first long paragraph
        for p in paragraphs: # iterate through paragraphs
            text = p.get_text(strip=True) # extract text without surrounding whitespace

            if len(text) >= 50: # check if paragraph is long enough
                first_valid_paragraph = p.get_text().strip() # store full paragraph text
                break # stop after finding the first valid one

        if first_valid_paragraph: # check if a valid paragraph was found
            print("First Valid Paragraph:") # label output
            print(first_valid_paragraph) # print the paragraph
        else:
            print("No paragraph with at least 50 characters was found.") # fallback message
    else:
        print("Main content div not found.") # notify if missing


if __name__ == "__main__": # run only when executed directly
    scrape_wiki_data() # call the scraping function
