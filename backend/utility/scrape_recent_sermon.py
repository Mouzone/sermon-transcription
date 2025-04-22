from typing import Optional, Dict
import logging
from pyppeteer import launch
from bs4 import BeautifulSoup


async def scrapeRecentSermon() -> Optional[Dict[str, str]]:
    """
    1. Scrapes ArumdaunEM's livestreams page using Pyppeteer
    2. Finds the most recent COMPLETED livestream
    3. Returns the title and link to the video
        Returns None in case of error
    """
    browser = None
    try:
        browser = await launch(headless=True, args=["--no-sandbox"])
        page = await browser.newPage()

        # Set viewport and user agent
        await page.setViewport({"width": 1280, "height": 800})
        await page.setUserAgent(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like "
            "Gecko) Chrome/90.0.4430.212 Safari/537.36"
        )

        await page.goto(
            "https://www.youtube.com/@ArumdaunEM/streams",
            {"waitUntil": "networkidle2", "timeout": 30000},
        )

        # Wait for the video elements to load
        await page.waitForSelector("a#video-title-link", {"timeout": 10000})

        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")

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
        if browser:
            await browser.close()
