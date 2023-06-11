import requests
from bs4 import BeautifulSoup

# Get the URL from the user
url = input("Enter the URL of the website: ")

# Send an HTTP request to the specified website
response = requests.get(url)

# If the request is successful, continue
if response.status_code == 200:
    # You can use the content
    content = response.content

    # Parse the HTML content
    soup = BeautifulSoup(content, "html.parser")

    # Select the HTML tags you want to manipulate
    tags = soup.find_all("a")

    # Iterate over the tags
    for tag in tags:
        # Get the tag content or attributes
        print(tag.text)
        print(tag["href"])
