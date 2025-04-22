from typing import Dict
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def scrapeNewest() -> Dict[str, str]:
    """
    1. Scrapes ArumdaunEM's livestreams page using Selenium
    2. Finds the most recent COMPLETED livestream
    3. Returns the title and link to the video
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML"
        ", like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    )

    driver = None
    try:
        driver = webdriver.Chrome(service=Service(), options=options)
        driver.set_window_size(1280, 800)

        driver.get("https://www.youtube.com/@ArumdaunEM/streams")

        # Wait for the videos elements to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a#video-title-link"))
        )

        soup = BeautifulSoup(driver.page_source, "html.parser")
        recent_sermon = soup.find("a", id="video-title-link")
        if not recent_sermon:
            raise ValueError("Could not find the recent sermon element")

        href = recent_sermon.get("href")
        title = recent_sermon.get("title")

        if not href:
            raise ValueError("No href found for the recent sermon")

        return {"title": title, "link": f"https://www.youtube.com{href}"}

    except Exception as e:
        logger.error(f"Failed to scrape recent sermon: {str(e)}")
        raise SermonProcessingError("Sermon scraping failed") from e

    finally:
        if driver:
            driver.quit()
