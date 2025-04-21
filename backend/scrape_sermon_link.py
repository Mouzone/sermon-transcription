from requests_html import HTMLSession
from bs4 import BeautifulSoup
import logging


def scrapeSermonLink() -> str:
    """
    1. Scrapes ArumdaunEM's livestreams page
    2. Finds the most most recent COMPLETED livestream
    3. Returns the link to the video
        Returns None in case of error
    """
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

        if not href:
            raise ValueError("No href found for the recent sermon")

        return f"https://www.youtube.com{href}"

    except Exception as e:
        logging.error(f"Error during scraping: {str(e)}")
        return None

    finally:
        session.close()
