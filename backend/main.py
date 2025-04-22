import logging
from utility.scrape_newest import scrapeNewest
from utility.download import download
from utility.transcribe import transcribe
from utility.outline import outline
from utility.store import store
from utility.cleanup import cleanup

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("sermon_processor.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


class SermonProcessingError(Exception):
    """Custom exception for sermon processing errors"""

    pass


def main():
    try:
        logger.info("Starting sermon processing pipeline")

        # Step 1: Get sermon data
        logger.info("Scraping recent sermon data")
        sermon_data = scrapeNewest()

        # Step 2: Download audio
        filepath = download(sermon_data["link"])

        try:
            # Step 3: Transcribe audio
            transcript = transcribe(filepath)

            # Step 4: Process transcript
            sermon = outline(transcript)

            # Prepare final data
            del sermon["bible_reading"]
            sermon["title"] = sermon_data["title"]
            sermon["original_transcript"] = transcript

            # Step 5: Store data
            store(sermon)

            logger.info("Sermon processing completed successfully")

        except Exception as e:
            logger.error(f"Sermon processing failed: {str(e)}")
            raise

        finally:
            # Cleanup downloaded files
            cleanup(filepath)

    except SermonProcessingError as e:
        logger.error(f"Sermon processing pipeline failed: {str(e)}")
        # Here you could add notification logic (email, Slack, etc.)
        raise
    except Exception as e:
        logger.critical(
            f"Unexpected error in sermon processing: {str(e)}", exc_info=True
        )
        raise


if __name__ == "__main__":
    main()
