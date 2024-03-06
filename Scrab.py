import requests
from bs4 import BeautifulSoup

def fetch_wikipedia_content(url):
    try:
        response = requests.get(url)
        print(response)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        # Extract text content from HTML
        text_content = soup.get_text()
        return text_content
    except requests.exceptions.RequestException as e:
        print("Error fetching content:", e)
        return None

def main():
    while True:
        # Ask the user for a Wikipedia URL
        url = input("Enter a Wikipedia URL (or 'exit' to quit): ")
        if url.lower() == 'exit':
            break

        # Fetch and display text content from the provided URL
        text_content = fetch_wikipedia_content(url)
        print(type(text_content))
        if text_content:
            print("\nText content from", url, ":\n", text_content[:10])  # Display only first 500 characters of content
        

if __name__ == "__main__":
    main()