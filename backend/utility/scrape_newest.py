from typing import Dict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from utility.logging import setup_logger, SermonProcessingError

logger = setup_logger(__name__)


def scrapeNewest() -> Dict[str, str]:
    """
    Scrapes ArumdaunEM's livestreams page using Selenium
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1280,800")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    )

    # For newer Selenium versions (4.6+)
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
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
        driver.quit()
