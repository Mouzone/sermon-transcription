import logging
from utility.scrape_recent_sermon import scrapeRecentSermon
from utility.download_sermon import download_sermon
from utility.transcribe import transcribe_audio
from utility.outline_sermon import process_transcript
from utility.store_sermon import store_sermon
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
        sermon_data = scrapeRecentSermon()

        # Step 2: Download audio
        filepath = download_sermon(sermon_data["link"])

        try:
            # Step 3: Transcribe audio
            transcript = transcribe_audio(filepath)

            # Step 4: Process transcript
            sermon = process_transcript(transcript)

            # Prepare final data
            del sermon["bible_reading"]
            sermon["title"] = sermon_data["title"]
            sermon["original_transcript"] = transcript

            # Step 5: Store data
            store_sermon(sermon)

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
