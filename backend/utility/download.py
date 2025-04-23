import yt_dlp
import os

from utility.logging import setup_logger, SermonProcessingError

logger = setup_logger(__name__)


def download(link: str) -> str:
    """Download sermon audio with retries and error handling"""
    yt_opts = {
        "verbose": True,
        "format": "bestaudio/best",
        "outtmpl": "sermons/%(title)s.%(ext)s",
        "retries": 3,
        "cookies": "../youtube_cookies.txt",
    }

    try:
        logger.info(f"Attempting to download sermon from {link}")
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            ydl.download([link])

        # Get downloaded filename
        filename = os.listdir("./sermons")[0]
        filepath = os.path.join("./sermons", filename)
        logger.info(f"Successfully downloaded sermon to {filepath}")
        return filepath

    except yt_dlp.DownloadError as e:
        logger.error(f"Failed to download sermon video: {str(e)}")
        raise SermonProcessingError("Sermon download failed") from e
    except Exception as e:
        logger.error(f"Unexpected error during download: {str(e)}")
        raise SermonProcessingError("Sermon download failed") from e
