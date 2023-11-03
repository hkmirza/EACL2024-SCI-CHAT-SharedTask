import requests
from bs4 import BeautifulSoup

# URL of the podcast episode transcript
url = 'https://freakonomics.com/podcast/introducing-a-new-freakonomics-of-medicine-podcast-ep-465/'

# Send a GET request to the webpage
response = requests.get(url)
# parse the entire data getting from the web page
soup = BeautifulSoup(response.content, 'html.parser')

# Extract title of page
page_title = soup.title.text
# print(page_title)
# print(soup) # run this if you want to explore other contents from the web page

# Find the div with class is equal to "feature_content"
# feature_content cntains the description of the topic in a paragraph

feature_div = soup.find('div', class_='feature_content')

if feature_div:
    # Find the paragraph within the div
    paragraph = feature_div.find('p')

    if paragraph:
        # Extract the text content from the paragraph
        text_content = paragraph.get_text()

        # Specify the file path to save the text file and file name for e.g title-text.txt
        file_path = r"C:\Users\mhaid\title-text.txt"

        # Save the text content to a file
        with open(file_path, 'w') as output_file:
            output_file.write(page_title + '\n'+ text_content)

        print(f"Text saved to {file_path}.")
    else:
        print("No <p> tag found inside the div.")
else:
    print("Feature content div not found.")


## Find the div with id is equal to "transcript"
# transcript cntains the script of the podcast 
transcript_div = soup.find('div', id='transcript')


if transcript_div:
    # Find all paragraphs within the div
    paragraphs = transcript_div.find_all('p')

    # Extract text content from paragraphs
    text_content = '\n'.join(paragraph.get_text() for paragraph in paragraphs)

    # Specify the file path to save the text file and file name for e.g transcript-file.txt
    file_path = r"C:\Users\mhaid\transcript-file.txt"

    # Save the text content to a file
    with open(file_path, 'w') as output_file:
        output_file.write(text_content)

    print(f"Text saved to {file_path}.")
else:
    print("Transcript div not found.")







