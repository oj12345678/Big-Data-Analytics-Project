import requests
from bs4 import BeautifulSoup

def scrape_top_headlines(url, num_headlines=5):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the headlines using appropriate tags and classes
        # Replace 'your_headline_tag' and 'your_headline_class' with the actual values
        headline_tags = soup.find_all('your_headline_tag', class_='your_headline_class')

        # Extract the text content of the headlines
        headlines = [tag.text.strip() for tag in headline_tags[:num_headlines]]

        if headlines:
            return headlines
        else:
            return ["Headlines not found on the page."]

    else:
        return f"Failed to retrieve the page. Status code: {response.status_code}"

# https://timesofindia.indiatimes.com/ the actual URL of the news website
url = 'https://www.wionews.com//'
top_headlines = scrape_top_headlines(url, num_headlines=5)

print("Top 5 Headlines:")
for i, headline in enumerate(top_headlines, start=1):
    print(f"{i}. {headline}")
