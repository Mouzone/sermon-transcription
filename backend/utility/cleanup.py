import os
from utility.logging import setup_logger

logger = setup_logger(__name__)


def cleanup(filepath):
    try:
        if filepath and os.path.exists(filepath):
            os.remove(filepath)
            logger.info(f"Cleaned up file: {filepath}")
    except Exception as e:
        logger.warning(f"Cleanup failed for {filepath}: {str(e)}")
