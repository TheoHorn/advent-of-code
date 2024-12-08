import requests
import os
from bs4 import BeautifulSoup

def fetch_webpage_content_with_cookies(url, session_cookie):
    """
    Fetch content from a given URL using a session cookie for authentication.

    :param url: The URL to fetch.
    :param session_cookie: The session cookie for authentication.
    :return: Content of the webpage or an error message.
    """
    if not url.startswith('https://'):
        return "Error: URL must start with 'https://'"
    
    headers = {"Cookie": f"session={session_cookie}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch the webpage. Details: {str(e)}"


def inputing(year=2024, day=1):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    with open('session_cookie.txt', 'r') as file:
        session_cookie = file.read().strip()

    # Fetch webpage content
    content = fetch_webpage_content_with_cookies(url, session_cookie)

    #strip useless lines at the end of the file
    content = content.strip()

    # Create directory if it doesn't exist
    os.makedirs(f'{year}/{day}', exist_ok=True)

    # Write content to the file, replacing it if it already exists
    with open(f'{year}/{day}/input.txt', 'w') as file:
        file.write(content)

    return content

def outputing(year=2024, day=1, part=1, answer=None):
    """
    Submit an answer to the Advent of Code website.

    :param year: The year of the challenge.
    :param day: The day of the challenge.
    :param part: The part of the challenge (1 or 2).
    :param answer: The answer to submit.
    :return: The response text or an error message.
    """
    if answer is None:
        return "Error: You must provide an answer."

    # Adjust the URL to include "day/answer" as the form action specifies
    url = f'https://adventofcode.com/{year}/day/{day}/answer'

    # Read session cookie from file
    try:
        with open('session_cookie.txt', 'r') as file:
            session_cookie = file.read().strip()
    except FileNotFoundError:
        return "Error: session_cookie.txt not found. Make sure it exists and contains your session cookie."

    # Prepare the payload and headers
    data = {'level': part, 'answer': answer}
    headers = {"Cookie": f"session={session_cookie}"}

    try:
        # Submit the form via POST
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        # Parse the response text to extract the <article> tag
        soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find('article')

        if article:
            return article.prettify()
        else:
            return "Error: <article> tag not found in the response."
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to submit the answer. Details: {str(e)}"
    

inputing(year=2024, day=8)
#print(outputing(year=2015, day=13, part=1, answer=822))