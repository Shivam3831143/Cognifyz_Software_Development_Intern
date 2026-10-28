import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; StudentLearningProject/1.0)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the webpage title
        if soup.title:
            title = soup.title.get_text(strip=True)
        else:
            title = "No title found"

        print("\n===== SCRAPING RESULTS =====")
        print(f"Website: {url}")
        print(f"Page title: {title}")

        # Extract the first 10 headings
        headings = soup.find_all(["h1", "h2", "h3"])

        if headings:
            print("\nPage headings:")
            for index, heading in enumerate(headings[:10], start=1):
                print(f"{index}. {heading.get_text(' ', strip=True)}")
        else:
            print("\nNo headings found.")

    except requests.RequestException as error:
        print(f"\nUnable to access the website: {error}")


def main():
    print("===== WEB SCRAPING TOOL =====")

    url = input(
        "Enter a website URL (including https://): "
    ).strip()

    if not url.startswith(("https://", "http://")):
        print("Invalid URL. Please start with http:// or https://.")
        return

    scrape_website(url)


if __name__ == "__main__":
    main()