# Task 6: Interactive Web Scraping

## Internship
Cognifyz Technologies — Software Development Internship

## Description
This Python project extracts information from a user-provided website URL. It uses the Requests library to retrieve webpage content and BeautifulSoup to parse HTML.

## Features
- Accepts a website URL from the user.
- Extracts the webpage title.
- Finds and displays up to 10 headings (`h1`, `h2`, and `h3`).
- Handles network errors and invalid URL formats.
- Uses a request timeout to prevent waiting indefinitely.

## Technologies Used
- Python 3
- Requests
- BeautifulSoup4

## Installation
Install the required libraries:

```bash
python -m pip install requests beautifulsoup4
```

## How to Run
From the project root directory, execute:

```bash
python -u Level_3/Task_6_Web_Scraping/main.py
```

Enter a website URL when prompted, for example:

```text
https://example.com
```

## Testing
Tested successfully using `https://example.com`. The program displayed the page title as `Example Domain`. No headings were found on that page, which is an acceptable result.

## Responsible Web Scraping
Only scrape websites that permit automated access. Respect their terms of service, robots policies, and rate limits.

## Learning Outcomes
Learned how to send HTTP requests, parse HTML content, extract webpage information, and handle request errors.