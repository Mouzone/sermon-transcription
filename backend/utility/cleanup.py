import os


def cleanup(filepath):
    try:
        if filepath and os.path.exists(filepath):
            os.remove(filepath)
            logger.info(f"Cleaned up file: {filepath}")
    except Exception as e:
        logger.warning(f"Cleanup failed for {filepath}: {str(e)}")
