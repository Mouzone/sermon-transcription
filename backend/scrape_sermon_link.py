from requests_html import HTMLSession
from bs4 import BeautifulSoup
import logging


def scrape_sermon_link():
    session = HTMLSession()
    try:
        r = session.get("https://www.youtube.com/@ArumdaunEM/streams", timeout=10)
        r.raise_for_status()  # Raise an exception for HTTP errors

        # Render JavaScript with longer timeout
        r.html.render(timeout=20, sleep=3)

        # Parse with BeautifulSoup
        soup = BeautifulSoup(r.html.html, "html.parser")

        # More robust element finding
        recent_sermon = soup.find("a", id="video-title-link")
        if not recent_sermon:
            raise ValueError("Could not find the recent sermon element")

        # Get attributes safely
        href = recent_sermon.get("href")
        title = recent_sermon.get("title")

        if not href:
            raise ValueError("No href found for the recent sermon")

        recent_sermon_data = {
            "link": f"https://www.youtube.com{href}",
            "title": title,
        }

        return recent_sermon_data

    except Exception as e:
        logging.error(f"Error during scraping: {str(e)}")
        return None

    finally:
        session.close()


print(scrape_sermon_link())
