from typing import Optional, Dict
from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup
import logging


async def scrapeRecentSermon() -> Optional[Dict[str, str]]:
    """
    1. Scrapes ArumdaunEM's livestreams page
    2. Finds the most most recent COMPLETED livestream
    3. Returns the link to the video
        Returns None in case of error
    """
    session = AsyncHTMLSession()
    try:
        r = await session.get("https://www.youtube.com/@ArumdaunEM/streams", timeout=10)
        r.raise_for_status()

        # Render JavaScript with longer timeout
        await r.html.arender(timeout=20, sleep=3)  # Note: arender instead of render

        # Rest of your code remains the same...
        soup = BeautifulSoup(r.html.html, "html.parser")
        recent_sermon = soup.find("a", id="video-title-link")
        if not recent_sermon:
            raise ValueError("Could not find the recent sermon element")

        href = recent_sermon.get("href")
        title = recent_sermon.get("title")

        if not href:
            raise ValueError("No href found for the recent sermon")

        return {"title": title, "link": f"https://www.youtube.com{href}"}

    except Exception as e:
        logging.error(f"Error during scraping: {str(e)}")
        return None
    finally:
        await session.close()
