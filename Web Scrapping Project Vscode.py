import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

# URL of the website you want to scrape
url = "https://realpython.com/"

# Send a request to fetch the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the articles
    articles = soup.find_all('h2', class_='card-title')

    if articles:
        for article in articles:
            title = article.get_text().strip()
            print(title)
    else:
        print("Articles not found")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
