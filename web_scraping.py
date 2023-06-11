import requests
from bs4 import BeautifulSoup

# Get the URL from the user
url = input("Enter the URL of the website: ")

# Send an HTTP request to the specified website
# Set verify to False to disable SSL certificate verification (Note: This can be a security risk)
response = requests.get(url, verify=False)  # Disable SSL certificate verification for testing purposes

# If the request is successful, continue
if response.status_code == 200:
    # You can use the content
    content = response.content

    # Parse the HTML content
    soup = BeautifulSoup(content, "html.parser")

    # Get all unique tag names in the HTML
    all_tags = set(tag.name for tag in soup.find_all())

    # Display all tag names for user reference
    tag_names_string = ', '.join(f'"{tag}"' for tag in all_tags)
    print(f"Available tag names: {tag_names_string}")

    # Get the tag from the user
    tag_name = input("Enter the HTML tag you want to select: ")

    # Select the HTML tags based on user input
    tags = soup.find_all(tag_name)

    # Iterate over the tags
    for tag in tags:
        # Get the tag content or attributes
        print(tag.text)
        print(tag_name+":", tag["href"])
